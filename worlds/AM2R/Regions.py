import typing

from BaseClasses import MultiWorld, Region, RegionType, Entrance
from .Locations import SMWLocation
from .Levels import level_info_dict
from .Names import LocationName, ItemName
from ..generic.Rules import add_rule, set_rule

#  Suck it Gatordile
def create_regions(world, player: int, active_locations):
    menu_region = create_region(world, player, active_locations, 'Menu', None)

    golden_temple_region = create_region(world, player, active_locations, LocationName.golden_temple_region, None)
    golden_temple_region = create_region(world, player, active_locations, LocationName.golden_temple_region, None)
