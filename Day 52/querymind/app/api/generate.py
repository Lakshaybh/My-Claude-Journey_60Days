import json

from fastapi import APIRouter, HTTPException
from groq import APIError

from app.core.groq_client import call_ai_for_sql
from app.models.schemas import GenerateRequest, GenerateResponse
from app.prompts.sql_prompt import extract_json

router = APIRouter()


@router.post("/api/generate", response_model=GenerateResponse)
def generate_sql(request: GenerateRequest):
    try:
        raw_response = call_ai_for_sql(request.schema_text, request.question)
    except APIError:
        raise HTTPException(
            status_code=502,
            detail="AI service is temporarily unavailable. Please try again.",
        )

    try:
        parsed = extract_json(raw_response)
        sql = parsed["sql"]
        explanation = parsed["explanation"]
    except (json.JSONDecodeError, KeyError, TypeError):
        raise HTTPException(
            status_code=500,
            detail="Could not generate a valid response. Please try rephrasing your question.",
        )

    return GenerateResponse(sql=sql, explanation=explanation, warning=None)
