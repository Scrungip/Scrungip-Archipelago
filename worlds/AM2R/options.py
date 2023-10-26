from typing import Union, List, Dict
from BaseClasses import MultiWorld
from Options import AssembleOptions, Choice, DeathLink, DefaultOnToggle, Range, StartInventoryPool


class MetroidsRequired(Range):
    """Chose how many Metroids need to be killed or obtained to go through to the omega nest"""
    display_name = "Metroids Required for Omega Nest"
    range_start = 0
    range_end = 41
    default = 41


class MetroidsAreChecks(Choice):
    """Have each of the 46 non lab Metroids be treated as locations"""
    display_name = "Metroids are Checks"
    default = 0
    option_disabled = 0
    option_exclude_A6 = 1
    option_include_A6 = 2


class TrapFillPercentage(Range):
    """Adds in Slightly inconvenient Traps into the item pool Equipment Traps disable 1 random item for up to 3 minutes
    depending on the disabled item (more critical items will be disabled for less time).  Ice Traps seem rather
    self-explanatory, but they will freeze you upon receiving them with a full fanfare and an actual player freeze"""
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0


#class ItemSprites(OptionList):
#    """Changes Item Sprites.  Does not affect gameplay
#    Sprite Authors appear in the item description"""
#    display_name = "Item Sprites"
#    default = 0
#    option_default = 0
#    option_themed = 1
#    option_chiny = 2
#    option_ungrouped = 3
#    option_lies = 4


#class Visuals(Toggle):
#    """"""Re-colours all the visual elements with new fresh palettes.  Does not affect gameplay.
#    Courtesy of Abyssal""""""


#class StartingWeapons(Choice):
#    """Removes your Arm Cannon and makes it a findable item"""
#    display_name = "Starting Weapons"
#    default = 0
#    option_normal = 0
#    option_missiles_only = 1
#    option_beam_only = 2
#    option_none = 3


#class RandomizeBaby(Toggle):
#    """Randomizes the baby metroid as a cosmetic find"""
#    display_name = "Randomize Baby"


#class AreaRando(Choice):
#    """Activates Area Randomization and or Boss Randomization, also activates rolling saves as softlock prevention
#    Area Randomizer will shuffle various Areas arround in order to create a new expierence
#    Boss Randomization randomizes Arachnus, Torizo Ascended, and Genesis with each other also then randomizes
#    Temple Guardian, Tester and Serris
#    Both activates Both independently on their own"""
#    display_name = "Area Randomizer"
#
#    default = 0
#    option_disabled = 0
#    option_area = 1
#    option_boss = 2
#    option_both = 3


#  class IceMissiles(Toggle):
#  """Changes missiles to have Ice properties
#  Does not account for jumping off enemies
#  only counts as being able to freeze meboids and metroid larva"""
#  display_name = "Ice Missiles"


AM2R_options: Dict[str, AssembleOptions] = {
    "MetroidsRequired": MetroidsRequired,
    "MetroidsAreChecks": MetroidsAreChecks,
    "TrapFillPercentage": TrapFillPercentage,
    #  "Item Sprites": ItemSprites,
    #  "Starting Weapons": StartingWeapons,
    #  "Randomize Baby", RandomizeBaby
    #  "Area Rando": AreaRando,
    #  "Ice Missiles":  IceMissiles,
    #  "DeathLink": DeathLink,
}


def is_option_enabled(world: MultiWorld, player: int, name: str) -> bool:
    return get_option_value(world, player, name) > 0


def get_option_value(world: MultiWorld, player: int, name: str) -> Union[int, Dict, List]:
    option = getattr(world, name, None)
    if option is None:
        return 0

    return option[player].value
