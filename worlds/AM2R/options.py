from typing import Dict, Union, List
from BaseClasses import MultiWorld
from Options import Option, Range, DeathLink, SpecialRange, Toggle, Choice, OptionList


class MetroidsRequired(Range):
    """Chose how many Metroids need to be killed or obtained to go through to the omega nest"""
    display_name = "Metroids Required"
    range_start = 0
    range_end = 41
    default = 41


class MetroidsAreChecks(Toggle):
    """Have each of the 46 non lab Metroids be treated as locations"""
    display_name = "Metroids are Checks"


class TrapFillPrecentage(Range):
    """Adds in Slightly inconvenient Traps into the item pool Equipment Traps disable 1 random item for up to 3 minutes
    depending on the disabled item (more critical items will be disabled for less time).  Ice Traps seem rather
    self-explanatory, but they will freeze you upon receiving them with a full fanfare and an actual player freeze"""
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0


class Traps(OptionList):
    """List of traps that can be found in the pool"""
    display_name = "Trap Types"
    valid_keys = {"Equipment Trap", "Ice Trap", "Short Beam", "EMP Trap"}
    default = {"Equipment Trap", "Ice Trap", "Short Beam", "EMP Trap"}


#  class AreaRando(Choice):
    #  """Activates Area Randomization and or Boss Randomization, also activates rolling saves as softlock prevention
    #  Area Randomizer will shuffle various Areas arround in order to create a new expierence
    #  Boss Randomization randomizes Arachnus, Torizo Ascended, and Genesis with each other also then randomizes
    #  Temple Guardian, Tester and Serris
    #  Both activates Both independently on their own"""
    #  display_name = "Area Randomizer"

    #  default = 0
    #  option_disabled = 0
    #  option_area = 1
    #  option_boss = 2
    #  option_both = 3
    #  option_chaos = 4


#  class BossRando(Toggle):
    #  """Activates Boss Randomization randomizes Arachnus, Torizo Ascended, and Genesis with each other.
    #  then also randomizes Temple Guardian, Tester abd Serris"""
    #  display_name = "Boss Randomizer"


#  class IceMissiles(Toggle):
    #  """Changes missiles to have Ice properties """
    #  display_name = "Ice Missiles"


AM2R_options: Dict[str, type(Option)] = {
    "metroids_required": MetroidsRequired,
    "metroids_are_checks": MetroidsAreChecks,
    "trap_fill_precentage": TrapFillPrecentage,
    "traps": Traps,
    #  "area_rando":  AreaRando,
    #  "boss_rando":  BossRando,
    #  "ice_missiles":  IceMissiles,
    #  "DeathLink": DeathLink,
}


def is_option_enabled(world: MultiWorld, player: int, name: str) -> bool:
    return get_option_value(world, player, name) > 0


def get_option_value(world: MultiWorld, player: int, name: str) -> Union[int, Dict, List]:
    option = getattr(world, name, None)
    if option == None:
        return 0

    return option[player].value
