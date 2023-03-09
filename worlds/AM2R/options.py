from dataclasses import dataclass
from typing import Dict, Union, Protocol, runtime_checkable

from Options import Option, Range, DeathLink, SpecialRange, Toggle, Choice


@runtime_checkable
class AM2ROption(Protocol):
    internal_name: str


@dataclass
class AM2ROptions:
    options: Dict[str, Union[bool, int]]

    def __getitem__(self, item: Union[str, AM2ROption]) -> Union[bool, int]:
        if isinstance(item, AM2ROption):
            item = item.internal_name

        return self.options.get(item, None)


class MetroidsRequired(Range):
    """Chose how many Metroids need to be killed or obtained to go through to the omega nest"""
    display_name = "Metroids Required"
    internal_name = "metroids_required"
    range_start = 0
    range_end = 41
    default = 41


class MetroidsAreChecks(Toggle):
    """Have each of the 46 non lab Metroids be treated as checks"""
    display_name = "Metroids are Checks"
    internal_name = "metroids_are_checks"


class TrapFillPrecentage(Range):
    """Adds in Slightly inconvenient Traps into the item pool Equipment Traps disable 1 random item for up to 3 minutes
    depending on the disabled item (more critical items will be disabled for less time).  Ice Traps seem rather
    self-explanatory, but they will freeze you upon receiving them with a full fanfare and an actual player freeze"""
    display_name = "Trap Fill Percentage"
    internal_name = "trap_fill_percentage"
    range_start = 0
    range_end = 100
    default = 50


class BaseTrapWeight(Choice):
    """Base Class for Trap Weights"""
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 4
    default = 1


class EquipmentTrap(BaseTrapWeight):
    """Disables 1 of your items for a period of time depending on the item type"""
    display_name = "Equipment Trap"
    internal_name = "equipment_trap"


class IceTrap(BaseTrapWeight):
    """Play the full item fanfare and then freezes the player"""
    display_name = "Ice Trap"
    internal_name = "ice_trap"


class ShortBeam(BaseTrapWeight):
    """Makes your beam shots expire rapidly lasts 10 minutes"""
    display_name = "Short Beam"
    internal_name = "short_beam"


class EMPTrap(BaseTrapWeight):
    """Activates an EMP effect on you for 30 secconds"""
    display_name = "EMP Trap"
    internal_name = "emp_trap"


#  class AreaRando(Choice):
    #  """Activates Area Randomization and or Boss Randomization, also activates rolling saves as softlock prevention
    #  Area Randomizer will shuffle various Areas arround in order to create a new expierence
    #  Boss Randomization randomizes Arachnus, Torizo Ascended, and Genesis with each other also then randomizes
    #  Temple Guardian, Tester and Serris
    #  Both activates Both independently on their own"""
    #  display_name = "Area Randomizer"
    #  internal_name = "area_rando"
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
    #  internal_name = "boss_rando"


class IceMissiles(Toggle):
    """Changes missiles to have Ice properties """
    display_name = "Ice Missiles"
    internal_name = "ice_missiles"


AM2R_options: Dict[str, type(Option)] = {
    option.internal_name: option
    for option in [
        MetroidsRequired,
        MetroidsAreChecks,
        TrapFillPrecentage,
        IceTrap,
        EquipmentTrap,
        ShortBeam,
        EMPTrap,
        #  AreaRando,
        #  BossRando,
        IceMissiles,
    ]
}
default_options = {option.internal_name: option.default for option in AM2R_options.values()}
AM2R_options["death_link"] = DeathLink


def fetch_options(world, player: int) -> AM2ROptions:
    return AM2ROptions({option: get_option_value(world, player, option) for option in AM2R_options})


def get_option_value(world, player: int, name: str) -> Union[bool, int]:
    assert name in AM2R_options, f"{name} is not a valid option for AM2R."

    value = getattr(world, name)

    if issubclass(AM2R_options[name], Toggle):
        return bool(value[player].value)
    return value[player].value
