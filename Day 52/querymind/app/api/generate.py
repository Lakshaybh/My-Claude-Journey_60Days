import json
import logging

from fastapi import APIRouter, Depends, HTTPException

from app.core.groq_client import call_ai_for_sql
from app.core.rate_limit import enforce_rate_limit
from app.models.schemas import GenerateRequest, GenerateResponse
from app.prompts.sql_prompt import extract_json
from app.prompts.validator import build_warning

logger = logging.getLogger("querymind")

router = APIRouter()


@router.post(
    "/api/generate",
    response_model=GenerateResponse,
    dependencies=[Depends(enforce_rate_limit)],
)
def generate_sql(request: GenerateRequest):
    try:
        raw_response = call_ai_for_sql(request.schema_text, request.question)
    except Exception:
        logger.exception("AI provider call failed")
        raise HTTPException(
            status_code=502,
            detail="AI service is temporarily unavailable. Please try again.",
        )

    try:
        parsed = extract_json(raw_response)
        sql = parsed["sql"]
        explanation = parsed["explanation"]
    except (json.JSONDecodeError, KeyError, TypeError):
        logger.warning("Could not parse AI response as valid JSON: %r", raw_response[:500])
        raise HTTPException(
            status_code=500,
            detail="Could not generate a valid response. Please try rephrasing your question.",
        )

    warning = build_warning(sql, request.schema_text)

    return GenerateResponse(sql=sql, explanation=explanation, warning=warning)
