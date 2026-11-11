# === Stage 4: Редактирование записей ===
# Project: SpiceRack
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SpiceEditable:
    """Модель разрешаемых для редактирования полей специи.

    Хранит только те поля, которые допускают изменение, и валидацию
    для каждого из них. Позволяет менять название, происхождение,
    форму и срок годности, но не идентификатор сущности.
    """

    id: Optional[str] = None
    name: Optional[str] = None
    origin: Optional[str] = None
    form: Optional[str] = None
    shelf_life: Optional[str] = None
    allowed_fields: tuple = (
        "name",
        "origin",
        "form",
        "shelf_life",
    )

    def validate(self) -> list:
        """Возвращает список сообщений об ошибках для допустимых полей.

        Проверяет, что введённые значения не пустые и соответствуют
        ограничениям по типу и формату. Идентификатор не проверяется,
        так как изменение идентификатора не допускается.
        """

        errors: list = []

        if self.name is not None and self.name.strip() == "":
            errors.append("Название не может быть пустым")

        if self.origin is not None and self.origin.strip() == "":
            errors.append("Происхождение не может быть пустым")

        if self.form is not None and self.form.strip() == "":
            errors.append("Форма не может быть пустой")

        if self.shelf_life is not None and self.shelf_life.strip() == "":
            errors.append("Срок годности не может быть пустым")

        if self.shelf_life is not None and not self._is_valid_shelf_life(
            self.shelf_life
        ):
            errors.append("Срок годности должен быть в формате ДД.ММ.ГГГГ")

        return errors

    @staticmethod
    def _is_valid_shelf_life(value: str) -> bool:
        """Проверяет формат срока годности ДД.ММ.ГГГГ.

        Убеждается, что строка имеет правильный формат с разделителями
        и значения дня, месяца и года находятся в допустимых пределах.
        """

        parts = value.split(".")
        if len(parts) != 3:
            return False

        try:
            day = int(parts[0])
            month = int(parts[1])
            year = int(parts[2])
        except ValueError:
            return False

        if not (1 <= day <= 31):
            return False

        if not (1 <= month <= 12):
            return False

        if not (1900 <= year <= 2100):
            return False

        return True
