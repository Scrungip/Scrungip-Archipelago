from typing import Dict, Set, Tuple, NamedTuple


class ItemData(NamedTuple):
    category: str
    code: int
    count: int = 1
    progression: bool = False
    useful: bool = False
    trap: bool = False


item_table: Dict[str, ItemData] = {
    "Missile": ItemData("Ammo", 8678000, 44),
    "Super Missile": ItemData("Ammo", 8678001, 10),
    "Power Bomb": ItemData("Ammo", 8678002, 10),
    "Energy Tank": ItemData("Ammo", 8678003, 10),
    #  "Arm Cannon": ItemData("Equipment", 8678004, progression=True),
    #  "Morph Ball": ItemData("Equipment", 8678005, progression=True),
    #  "Power Grip": ItemData("Equipment", 8678006, progression=True),
    "Bombs": ItemData("Equipment", 8678007, progression=True),
    "Spider Ball": ItemData("Equipment", 8678008, progression=True),
    "Hi Jump": ItemData("Equipment", 8678009, progression=True),
    "Spring Ball": ItemData("Equipment", 8678010, progression=True),
    "Space Jump": ItemData("Equipment", 8678011, progression=True),
    "Speed Booster": ItemData("Equipment", 8678012, progression=True),
    "Screw Attack": ItemData("Equipment", 8678013, progression=True),
    "Varia Suit": ItemData("Equipment", 8678014, useful=True),
    "Gravity Suit": ItemData("Equipment", 8678015, progression=True),
    "Charge Beam": ItemData("Beam", 8678016, useful=True),
    "Wave Beam": ItemData("Beam", 8678017, useful=True),
    "Spazer": ItemData("Beam", 8678018, useful=True),
    "Plasma Beam": ItemData("Beam", 8678019, useful=True),
    "Ice Beam": ItemData("Beam", 8678020, progression=True),
    "Equipment Trap": ItemData("Trap", 8678021, 0, trap=True),
    "Freeze Trap": ItemData("Trap", 8678022, 0, trap=True),
    "Short Beam": ItemData("Trap", 8678023, 0, trap=True),
    "EMP Trap": ItemData("Trap", 8678024, 0, trap=True),
    "Metroid": ItemData("Metroid", 8678025, progression=True),
    "Omega Metroid": ItemData("Metroid", 8678026, progression=True),
    # "The Baby": ItemData("Tiny", 8678027),
}

filler_items: Tuple[str, ...] = (
    "Missile",
    "Super Missile",
    "Power Bomb",
    "Energy Tank"
)


def get_item_names_per_category() -> Dict[str, Set[str]]:
    categories: Dict[str, Set[str]] = {}

    for name, data in item_table.items():
        categories.setdefault(data.category, set()).add(name)

    return categories
