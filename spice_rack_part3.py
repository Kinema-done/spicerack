# === Stage 3: Хранилище в памяти ===
# Project: SpiceRack
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Spice:
    id: str
    name: str
    origin: str
    form: str
    shelf_life_days: int


class SpiceStore:
    def __init__(self) -> None:
        self._spices: Dict[str, Spice] = {}

    def add(self, spice: Spice) -> None:
        if spice.id in self._spices:
            raise ValueError(f"Специя с id={spice.id} уже существует")
        self._spices[spice.id] = spice

    def get(self, spice_id: str) -> Optional[Spice]:
        return self._spices.get(spice_id)

    def list_spices(self) -> List[Spice]:
        return list(self._spices.values())

    def __len__(self) -> int:
        return len(self._spices)


def main() -> None:
    store = SpiceStore()

    store.add(
        Spice(
            id="cumin",
            name="Куркума",
            origin="Индия",
            form="Порошок",
            shelf_life_days=730,
        )
    )
    store.add(
        Spice(
            id="cinnamon",
            name="Корица",
            origin="Шри-Ланка",
            form="Палочки",
            shelf_life_days=365,
        )
    )

    print(f"Всего специй: {len(store)}")

    for spice in store.list_spices():
        print(f"{spice.name} ({spice.origin}): {spice.form}, "
              f"хранить {spice.shelf_life_days} дней")

    found = store.get("cinnamon")
    if found:
        print(f"Найдена: {found.name}")
    else:
        print("Не найдена: не существует")


if __name__ == "__main__":
    main()
