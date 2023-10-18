import os
import sys
from typing import Dict, List, Set, Tuple, TextIO, Union, Iterable, Optional, Any

from .items import item_table, filler_items, get_item_names_per_category
from .locations import get_location_datas, EventId
from .regions import create_regions_and_locations
from BaseClasses import Region, Entrance, Tutorial, Item, ItemClassification, MultiWorld
from .options import AM2R_options, get_option_value, is_option_enabled
from worlds.AutoWorld import World, WebWorld


# todo something intelligent

class AM2RWeb(WebWorld):
    theme = "partyTime"
    tutorials = [
        Tutorial(
            tutorial_name="Multiworld Setup Tutorial",
            description="A guide to setting up the Archipelago AM2R software on your computer. This guide covers "
                        "single-player, multiworld, and related software.",
            language="English",
            file_name="AM2R_en.md",
            link="AM2R/en",
            authors=["Zed"]
        )
    ]


class AM2RWorld(World):
    """
    AM2R is a remake of the classic Metroid 2 game for the Game Boy that tries its best to keep the feel
    of the original as well as filling in some gaps to more closely tie into Metroid Fusion and brings some
    items from there as well.
    """
    game = "AM2R"
    data_version = 0
    web = AM2RWeb()
    option_definitions = AM2R_options

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {location.name: location.code for location in get_location_datas(None, None)}
    item_name_groups = get_item_names_per_category()

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)

    def generate_early(self) -> None:
        return

    def create_regions(self) -> None:
        create_regions_and_locations(self.multiworld, self.player)

    def create_items(self) -> None:
        self.create_and_assign_event_items()

        excluded_items: Set[str] = self.get_excluded_items()

        self.multiworld.itempool += self.get_item_pool(excluded_items)

    def set_rules(self) -> None:
        victory: str
        victory = "The Last Metroid is in Captivity"
        self.multiworld.completion_condition[self.player] = lambda state: state.has(victory, self.player)

    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {}

        for option_name in AM2R_options:
            slot_data[option_name] = self.get_option_value(option_name)

        return slot_data

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        return  # for if I ever need to write something into the

    def create_item(self, name: str) -> Item:
        data = item_table[name]

        if data.useful:
            classification = ItemClassification.useful
        elif data.progression:
            classification = ItemClassification.progression
        elif data.trap:
            classification = ItemClassification.trap
        else:
            classification = ItemClassification.filler

        item = Item(name, classification, data.code, self.player)

        if not item.advancement:
            return item

    def get_filler_item_name(self) -> str:
        trap_chance: int = self.get_option_value("Trap Fill Percentage")
        enabled_traps: List[str] = self.get_option_value("Traps")

        if self.multiworld.random.random() < (trap_chance / 100) and enabled_traps:
            return self.multiworld.random.choice(enabled_traps)
        else:
            return self.multiworld.random.choice(filler_items)

    def get_excluded_items(self) -> Set[str]:  # Set[str]
        excluded_items: Set[str] = set()

        if self.get_option_value("Metroids are Checks") < 2:
            excluded_items.add("Omega Metroid")
        if self.get_option_value("Metroids are Checks") < 1:
            excluded_items.add("Metroid")
            excluded_items.add("Omega Metroid")

        for item in self.multiworld.precollected_items[self.player]:
            if item.name not in self.item_name_groups["Ammo"]:
                excluded_items.add(item.name)
        return excluded_items

    def place_locked_items(self, excluded_items: Set[str], location: str, item:str) -> None:
        excluded_items.add(item)

        item = self.create_item(item)

        self.multiworld.get_location(location, self.player).place_locked_item(item)

    def get_item_pool(self, excluded_items: Set[str]) -> List[Item]:
        pool: List[Item] = []

        for name, data in item_table.items():
            if name not in excluded_items:
                for _ in range(data.count):
                    item = self.create_item(name)
                    pool.append(item)

        for _ in range(len(self.multiworld.get_unfilled_locations(self.player)) - len(pool)):
            item = self.create_item(self.get_filler_item_name())
            pool.append(item)

        return pool

    def create_and_assign_event_items(self) -> None:
        for location in self.multiworld.get_locations(self.player):
            if location.address == EventId:
                item = Item(location.name, ItemClassification.progression, EventId, self.player)
                location.place_locked_item(item)

    def get_personal_items(self) -> Dict[int, int]:
        personal_items: Dict[int, int] = {}

        for location in self.multiworld.get_locations(self.player):
            if location.address and location.item and location.item.code and location.item.player == self.player:
                personal_items[location.address] = location.item.code

        return personal_items

    def is_option_enabled(self, option: str) -> bool:
        return is_option_enabled(self.multiworld, self.player, option)

    def get_option_value(self, option: str) -> Union[int, Dict, List]:
        return get_option_value(self.multiworld, self.player, option)
