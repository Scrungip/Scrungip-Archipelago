from typing import Dict, Union
from Options import Toggle, DefaultOnToggle, DeathLink, Choice, Range, Option, OptionDict

class MetroidsRequired(Range):
    """Chose how many metroids need to be killed or obtained to go through to the omega nest"""
    display_name = "Metroids Required"
    range_start = 0
    range_end = 42
    default = 42


class MetroidsAreChecks(Toggle):
    """Have each of the 47 non lab metroids be treated as checks"""
    display_name = "Metroids are Checks"


AM2R_options: Dict[str, Option] = {
    "MetroidsRequired": MetroidsRequired,
    "MetroidsAreChecks": MetroidsAreChecks,
    "DeathLink": DeathLink,
}
