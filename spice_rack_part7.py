# === Stage 7: Генерация идентификаторов ===
# Project: SpiceRack
import re
import uuid
from collections.abc import Iterable


PROJECT_ID_PREFIX = "spicerack"


def _is_reserved(identifier: str) -> bool:
    return identifier in {"id", "spices", "mixes"}


def generate_unique_id(prefix: str = PROJECT_ID_PREFIX) -> str:
    return f"{prefix}-{uuid.uuid4().hex}"


def is_valid_identifier(identifier: str, reserved: Iterable[str] | None = None) -> bool:
    reserved = set(reserved or {"id", "spices", "mixes"})
    if not identifier:
        return False
    if identifier in reserved:
        return False
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", identifier):
        return False
    return True


def has_duplicate_ids(items: Iterable[str], prefix: str = PROJECT_ID_PREFIX) -> bool:
    seen: dict[str, int] = {}
    for identifier in items:
        if identifier.startswith(prefix):
            seen[identifier] = seen.get(identifier, 0) + 1
    return any(count > 1 for count in seen.values())


def generate_unique_id_with_check(
    prefix: str = PROJECT_ID_PREFIX,
    existing: Iterable[str] | None = None,
) -> str:
    unique = True
    while unique:
        candidate = f"{prefix}-{uuid.uuid4().hex}"
        if candidate not in (existing or []):
            unique = False
    return candidate


def resolve_duplicate_id(
    identifiers: Iterable[str],
    prefix: str = PROJECT_ID_PREFIX,
) -> str:
    resolved: list[str] = []
    for identifier in identifiers:
        if identifier.startswith(prefix):
            resolved.append(identifier)
        else:
            resolved.append(generate_unique_id_with_check(prefix, resolved))
    if has_duplicate_ids(resolved):
        raise ValueError("Duplicate identifiers detected")
    return resolved[0] if resolved else generate_unique_id_with_check(prefix, resolved)
