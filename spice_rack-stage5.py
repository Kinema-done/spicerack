# === Stage 5: Связанная сущность ===
# Project: SpiceRack
"""SpiceRack: сущность "смесь" и функции добавления.

Смесь связана со специей по идентификатору.
"""


class Spice:
    """Специя: название, происхождение, форма, срок годности."""

    def __init__(self, name, origin, form, shelf_life):
        self.name = name
        self.origin = origin
        self.form = form
        self.shelf_life = shelf_life

    def __repr__(self):
        return f"Spice({self.name!r})"


class SpiceMix:
    """Смесь специй, связанная со специей по идентификатору."""

    def __init__(self, name, spice_id, shelf_life):
        self.name = name
        self.spice_id = spice_id
        self.shelf_life = shelf_life

    def __repr__(self):
        return f"SpiceMix({self.name!r}, spice_id={self.spice_id!r})"


class SpiceRack:
    """Каталог специй и смесей."""

    def __init__(self):
        self._spices = []
        self._mixes = []

    def add_spice(self, name, origin, form, shelf_life):
        spice = Spice(name, origin, form, shelf_life)
        self._spices.append(spice)
        return spice

    def add_mix(self, name, spice_id, shelf_life):
        mix = SpiceMix(name, spice_id, shelf_life)
        self._mixes.append(mix)
        return mix

    def get_spice_by_id(self, spice_id):
        for spice in self._spices:
            if spice.name == spice_id:
                return spice
        return None

    def get_mix_by_id(self, mix_id):
        for mix in self._mixes:
            if mix.name == mix_id:
                return mix
        return None
