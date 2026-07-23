from fastapi import APIRouter

from app.models.schemas import GenerateRequest, GenerateResponse

router = APIRouter()


@router.post("/api/generate", response_model=GenerateResponse)
def generate_sql(request: GenerateRequest):
    # STUB for Day 3 (foundation only). Real Claude call wired up on Day 4
    # per the Implementation Blueprint — see app/prompts/sql_prompt.py.
    return GenerateResponse(
        sql="-- SQL generation not implemented yet (coming Day 4)",
        explanation="This is placeholder data confirming the route works end-to-end.",
        warning=None,
    )
