from typing import Dict, Union
from Options import Toggle, DefaultOnToggle, DeathLink, Choice, Range, Option, OptionDict


class MetroidsRequired(Range):
    """Chose how many Metroids need to be killed or obtained to go through to the omega nest"""
    display_name = "Metroids Required"
    range_start = 0
    range_end = 42
    default = 42


class MetroidsAreChecks(Toggle):
    """Have each of the 47 non lab Metroids be treated as checks"""
    display_name = "Metroids are Checks"


class TrapFillPrecentage(Range):
    """Adds in Slightly inconvenient Traps into the item pool Equipment Traps disable 1 random item for up to 3 minutes
    depending on the disabled item (more critical items will be disabled for less time).  Ice Traps seem rather
    self-explanatory, but they will freeze you upon receiving them with a full fanfare and an actual player freeze"""
    display_name = "Trap Fill Percentage"
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


class IceTrap(BaseTrapWeight):
    """Play the full item fanfare and then freezes the player"""
    display_name = "Ice Trap"


class ShortBeam(BaseTrapWeight):
    """Makes your beam shots expire rapidly lasts 10 minutes"""
    display_name = "Short Beam"


class EMPTrap(BaseTrapWeight):
    """Activates an EMP effect on you for 30 secconds"""
    display_name = "EMP Trap"


AM2R_options: Dict[str, Option] = {
    "MetroidsRequired": MetroidsRequired,
    "MetroidsAreChecks": MetroidsAreChecks,
    "TrapFillPercentage": TrapFillPrecentage,
    "IceTrap": IceTrap,
    "EquipmentTrap": EquipmentTrap,
    "ShortBeam": ShortBeam,
    "EMPTrap": EMPTrap,
    "DeathLink": DeathLink
}
