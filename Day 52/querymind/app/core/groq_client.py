from groq import Groq

from app.core.config import GROQ_API_KEY
from app.prompts.sql_prompt import SYSTEM_PROMPT, build_user_prompt

_client = Groq(api_key=GROQ_API_KEY)

MODEL = "llama-3.3-70b-versatile"


def call_ai_for_sql(schema_text: str, question: str) -> str:
    response = _client.chat.completions.create(
        model=MODEL,
        max_tokens=1024,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(schema_text, question)},
        ],
    )
    return response.choices[0].message.content
