# === Stage 6: Связи между сущностями ===
# Project: SpiceRack
from collections import defaultdict


class Spice:
    def __init__(self, name, origin, form, shelf_life):
        self.name = name
        self.origin = origin
        self.form = form
        self.shelf_life = shelf_life


class SpiceMix:
    def __init__(self, name, recipe):
        self.name = name
        self.recipe = recipe


def build_index(mixes, spices):
    spice_by_name = {spice.name: spice for spice in spices}
    spice_mixes = defaultdict(list)
    for mix in mixes:
        for spice_name in mix.recipe:
            if spice_name in spice_by_name:
                spice_mixes[spice_name].append(mix)
            else:
                spice_mixes["__missing__"].append((mix, spice_name))
    return spice_by_name, spice_mixes


def get_mixes_for_spice(spice, mixes, spices):
    spice_by_name, spice_mixes = build_index(mixes, spices)
    return spice_mixes.get(spice.name, [])


def check_integrity(spices, mixes):
    spice_by_name, spice_mixes = build_index(mixes, spices)
    missing = spice_mixes.get("__missing__", [])
    return not missing, missing
