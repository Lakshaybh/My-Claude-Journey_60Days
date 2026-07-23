from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    schema_text: str = Field(..., min_length=1, max_length=8000)
    question: str = Field(..., min_length=1, max_length=500)


class GenerateResponse(BaseModel):
    sql: str
    explanation: str
    warning: str | None = None
