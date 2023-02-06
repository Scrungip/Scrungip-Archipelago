import itertools
from typing import Dict, NamedTuple, Optional, List, Set
from BaseClasses import Item, ItemClassification, MultiWorld
from . import Regions, Locations


class ItemData(NamedTuple):
    code: Optional[int]
    group: str
    classification: ItemClassification = ItemClassification.progression
    required_num: int = 0


class AM2RItem(Item):
    game = str = "AM2R"

def create_item(player: int, name: str) -> Item:
    item_data = item_table[name]
    return AM2RItem(name, item_data.classification, item_data.code, player)


def create_all_items(world: MultiWorld, player: int) -> None:
    total_locations = world.total_locations[player].value
    itempool: List = []
    for item_name, count in required_items.items():
        itempool += [item_name] * count

    vic = world.victory_condition[player].value
    metroid_count = 0
    for i in range(metroid_count):
        itempool += ['Metroid']
    static_locations = 0


item_table: Dict[str, ItemData] = {  # todo item data numbers
    'Energy Tank': ItemData(1, 'Etank', ItemClassification.useful),  # 10
    'Missiles': ItemData(1, 'Ammo', ItemClassification.filler),
    'Super Missiles': ItemData(1, 'Ammo', ItemClassification.filler),
    'Power Bombs': ItemData(1, 'Ammo', ItemClassification.filler),
    'Morph Ball': ItemData(1, 'Equipment', ItemClassification.progression),  # possible future option
    'Power Grip': ItemData(1, 'Equipment', ItemClassification.progression),  # possible future option
    'Bombs': ItemData(1, 'Equipment', ItemClassification.progression),
    'Spider Ball': ItemData(1, 'Equipment', ItemClassification.progression),
    'Hi Jump': ItemData(1, 'Equipment', ItemClassification.progression),
    'Spring Ball': ItemData(1, 'Equipment', ItemClassification.progression),
    'Space Jump': ItemData(1, 'Equipment', ItemClassification.progression),
    'Speed Booster': ItemData(1, 'Equipment', ItemClassification.progression),
    'Screw Attack': ItemData(1, 'Equipment', ItemClassification.progression),
    'Varia Suit': ItemData(1, 'Suit', ItemClassification.useful),
    'Gravity Suit': ItemData(1, 'Suit', ItemClassification.progression),
    'Charge Beam': ItemData(1, 'Beam', ItemClassification.useful),
    'Wave Beam': ItemData(1, 'Beam', ItemClassification.useful),
    'S P A Z E R': ItemData(1, 'Beam', ItemClassification.useful),
    'Plasma Beam': ItemData(1, 'Beam', ItemClassification.useful),
    'Ice Beam': ItemData(1, 'Beam', ItemClassification.progression),
    'Metroid': ItemData(1, 'Metroid', ItemClassification.progression),
    'Equipment Trap': ItemData(1, 'Trap', ItemClassification.trap),
    'Freeze Trap': ItemData(1, 'Trap', ItemClassification.trap),
    'Short Beam': ItemData(1, 'Trap', ItemClassification.trap),
    'EMP Trap': ItemData(1, 'Trap', ItemClassification.trap),
}


def get_item_group(item_name: str) -> str:
    return item_table[item_name].group


def item_is_filler(item_name: str) -> bool:
    return item_table[item_name].classification == ItemClassification.filler


filler_items: List[str] = list(filter(item_is_filler, item_table.keys()))
item_name_to_id: Dict[str, int] = {name: data.code for name, data in item_table.items()}

item_name_groups: Dict[set, Set[str]] = {
    group: set(item_names)
    for group, item_names in itertools.groupby(item_table, get_item_group)
}

required_items: Dict[str, int] = {
    name: data.required_num
    for name, data in item_table.items() if data.required_num > 0
}
