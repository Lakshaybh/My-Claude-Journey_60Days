import json
import re

SYSTEM_PROMPT = """You are a SQL expert helping a data analyst write queries.

You will be given a database schema (as CREATE TABLE statements) and a question in plain English.

Rules:
1. Use ONLY the tables and columns that appear in the given schema. Never invent table or column names.
2. If the question cannot be fully answered from the given schema, still produce your best-effort SQL using only what's available, and mention the limitation in the explanation.
3. Respond with ONLY a single valid JSON object, with exactly these two keys:
   - "sql": the generated SQL query as a string
   - "explanation": a short, plain-English explanation (2-3 sentences) of what the query does, written for someone who does not know SQL
4. Do not wrap the JSON in markdown code fences. Do not add any text before or after the JSON object.
"""


def build_user_prompt(schema_text: str, question: str) -> str:
    return f"""Schema:
{schema_text}

Question:
{question}"""


def extract_json(raw_text: str) -> dict:
    """Claude is instructed to return pure JSON, but this defensively handles
    accidental markdown fences or stray text around the JSON object."""
    text = raw_text.strip()

    fence_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fence_match:
        text = fence_match.group(1)
    else:
        brace_match = re.search(r"\{.*\}", text, re.DOTALL)
        if brace_match:
            text = brace_match.group(0)

    return json.loads(text)
