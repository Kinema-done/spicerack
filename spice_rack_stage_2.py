# === Stage 2: Проверка полей ===
# Project: SpiceRack
import re
from datetime import date


def normalize_text(value):
    text = str(value).strip()
    text = re.sub(r"\s+", " ", text)
    text = text[0].upper() + text[1:] if text else text
    return text


def normalize_origin(value):
    origin = str(value).strip()
    origin = re.sub(r"\s+", " ", origin)
    origin = origin[0].upper() + origin[1:] if origin else origin
    return origin


def normalize_shape(value):
    shape = str(value).strip()
    shape = re.sub(r"\s+", " ", shape)
    shape = shape[0].upper() + shape[1:] if shape else shape
    return shape


def normalize_shelf_life(value):
    shelf_life = str(value).strip()
    shelf_life = re.sub(r"\s+", " ", shelf_life)
    shelf_life = shelf_life[0].upper() + shelf_life[1:] if shelf_life else shelf_life
    return shelf_life


def validate_name(name):
    if not name:
        return "Название не может быть пустым."
    normalized = normalize_text(name)
    if len(normalized) < 2:
        return "Название слишком короткое, введите минимум два символа."
    return normalized


def validate_origin(origin):
    if not origin:
        return "Происхождение не может быть пустым."
    normalized = normalize_origin(origin)
    if len(normalized) < 2:
        return "Происхождение слишком короткое, введите минимум два символа."
    return normalized


def validate_shape(shape):
    if not shape:
        return "Форма не может быть пустой."
    normalized = normalize_shape(shape)
    if len(normalized) < 2:
        return "Форма слишком короткая, введите минимум два символа."
    return normalized


def validate_shelf_life(shelf_life):
    if not shelf_life:
        return "Срок годности не может быть пустым."
    normalized = normalize_shelf_life(shelf_life)
    if len(normalized) < 2:
        return "Срок годности слишком короткий, введите минимум два символа."
    return normalized


def validate_spice(name, origin, shape, shelf_life):
    errors = []
    name = validate_name(name)
    if name != str(name):
        errors.append("Название должно быть строкой.")
    origin = validate_origin(origin)
    if origin != str(origin):
        errors.append("Происхождение должно быть строкой.")
    shape = validate_shape(shape)
    if shape != str(shape):
        errors.append("Форма должна быть строкой.")
    shelf_life = validate_shelf_life(shelf_life)
    if shelf_life != str(shelf_life):
        errors.append("Срок годности должен быть строкой.")
    if errors:
        return errors
    return [name, origin, shape, shelf_life]
