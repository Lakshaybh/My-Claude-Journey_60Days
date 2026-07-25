import re


def extract_schema_tables(schema_text: str) -> set[str]:
    """Returns the set of table names (lowercase) declared in the pasted schema."""
    return {
        name.lower()
        for name in re.findall(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?(\w+)", schema_text, re.IGNORECASE)
    }


def find_unknown_tables(sql: str, schema_text: str) -> list[str]:
    """Returns table names referenced in the SQL (via FROM/JOIN) that don't
    appear in the pasted schema. Empty list means everything checks out."""
    known_tables = extract_schema_tables(schema_text)
    if not known_tables:
        return []

    referenced = re.findall(r"(?:FROM|JOIN)\s+(\w+)", sql, re.IGNORECASE)
    unknown = sorted({t for t in referenced if t.lower() not in known_tables})
    return unknown


def build_warning(sql: str, schema_text: str) -> str | None:
    """Returns a user-facing warning string if the SQL references a table
    not found in the schema, otherwise None."""
    unknown_tables = find_unknown_tables(sql, schema_text)
    if not unknown_tables:
        return None

    names = ", ".join(unknown_tables)
    return (
        f"This query references a table ({names}) that wasn't found in your "
        "pasted schema. Please double-check before using it."
    )
