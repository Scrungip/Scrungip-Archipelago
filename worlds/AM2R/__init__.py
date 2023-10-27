from typing import Dict
from .items import item_table
from .locations import get_location_datas, EventId
from .regions import create_regions_and_locations
from BaseClasses import Tutorial, Item
from .options import AM2R_options
from worlds.AutoWorld import World, WebWorld


class AM2RWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up the Archipelago AM2R software on your computer. This guide covers single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Zed"]
    )]


class AM2RWorld(World):
    """
    AM2R is a remake of the classic Metroid 2 game for the Game Boy that tries its best to keep the feel
    of the original as well as filling in some gaps to more closely tie into Metroid Fusion and brings some
    items from there as well.
    """
    game = "AM2R"
    option_definitions = options.AM2R_options
    web = AM2RWeb()

    item_name_to_id = items.item_name_to_id
    location_name_to_id = {location.name: location.code for location in get_location_datas(None, None)}

    item_name_groups = items.item_name_groups
    data_version = 0

    def fill_slot_data(self) -> Dict[str, object]:
        return {name: getattr(self.multiworld, name)[self.player].value for name in self.option_definitions}

    def create_regions(self) -> None:
        create_regions_and_locations(self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        return items.create_item(self.player, name)

    def create_items(self) -> None:
        self.multiworld.get_location("The Last Metroid is in Captivity", self.player).place_locked_item(self.create_item("The Galaxy is at Peace"))
        items.create_all_items(self.multiworld, self.player)

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has("The Galaxy is at Peace", self.player)
