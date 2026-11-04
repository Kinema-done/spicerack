# === Stage 1: Каркас модуля ===
# Project: SpiceRack
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass(frozen=True)
class Spice:
    name: str
    origin: str
    form: str
    shelf_life_days: int
    created: date = field(default_factory=date.today)


def demo_spices() -> List[Spice]:
    return [
        Spice(name="Куркума", origin="Индия", form="Порошок", shelf_life_days=240),
        Spice(name="Чеснок", origin="Индия", form="Чесночные дольки", shelf_life_days=15),
        Spice(name="Имбирь", origin="Китай", form="Свежий корень", shelf_life_days=30),
        Spice(name="Паприка", origin="Испания", form="Порошок", shelf_life_days=180),
        Spice(name="Кориандр", origin="Индия", form="Семена", shelf_life_days=120),
    ]


def main() -> None:
    spices = demo_spices()
    print("SpiceRack — каталог специй")
    print("=" * 24)
    for spice in spices:
        print(f"- {spice.name} ({spice.origin})")
        print(f"  Форма:        {spice.form}")
        print(f"  Срок годности: {spice.shelf_life_days} дней")
        print(f"  Добавлено:    {spice.created.isoformat()}")
    print(f"Всего записей: {len(spices)}")


if __name__ == "__main__":
    main()
