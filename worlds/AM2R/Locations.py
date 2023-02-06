import functools
from enum import IntEnum
from typing import Dict, List, Union, Set, NamedTuple, Optional
from BaseClasses import Location
from .Options import TotalLocations


class AM2RLocation(Location):
    game: str = "AM2R"


class LocationData(NamedTuple):
    id: int
    ltype: Optional[str] = ""
    flag: int = 0

location_region_mapping: Dict[str, Dict[str, LocationData]] = {  # todo actual location numbers
    "Golden Temple":{
        "Golden Temple: Bombs": LocationData(2),
        "Golden Temple: Missile below Bombs": LocationData(2),  # bomb
        "Golden Temple: Hidden Energy Tank": LocationData(2),  # bomb
        "Golden Temple: Charge Beam": LocationData(2),
        "Golden Temple: Armory 1": LocationData(2),
        "Golden Temple: Armory 2": LocationData(2),
        "Golden Temple: Armory 3": LocationData(2),
        "Golden Temple: Armory Missile False Wall ": LocationData(2),  # bomb
        "Golden Temple: Puzzle Room Missle 1": LocationData(2),
        "Golden Temple: Puzzle Room Missle 2": LocationData(2),
        "Golden Temple: Puzzle Room Energy Tank": LocationData(2),
        "Golden Temple: Spider Ball": LocationData(2),
        "Golden Temple: Celling Missile": LocationData(2),  # canspider
        "Golden Temple: EMP room": LocationData(2),  # super + ballspark
        "Golden Temple: Above Guardian Missiles": LocationData(2), # bomb + schmove
        "Golden Temple: Above Guardian Power Bomb": LocationData(2), # PB + schmove
    },
    "Main Caves":{
        "Main Caves: Vertical Spike Room Upper": LocationData(2),  # spider + bomb
        "Main Caves: Vertical Spike Room Lower": LocationData(2),  # bomb
        "Main Caves: Crumble Spike Room": LocationData(2),  #jump
        "Main Caves: Shinespark Before the drop": LocationData(2),  # speed
        "Main Caves: Shinespark After the drop": LocationData(2),  # speed
        "Main Caves: Research Camp": LocationData(2),
    },
    "Hydro Station":{
        "Hydro Station: Clif": LocationData(2),
        "Hydro Station: Morph Tunnel": LocationData(2),
        "Hydro Station: Arachnus": LocationData(2),  # bomb
        "Hydro Station: Turbine Room Missile": LocationData(2),  # bomb
        "Hydro Station: Not so Secret Tunel": LocationData(2),  # schmove
        "Hydro Station: Water puzzle Beside Varia": LocationData(2),  # bomb
        "Hydro Station: Varia Suit": LocationData(2),  # bomb
        "Hydro Station: EMP room": LocationData(2),  # super + speed
    },
    "Inner Hydro Station":{  # bomb
        "Hydro Station: Wave Beam": LocationData(2),
        "Hydro Station: Below Tower Pipe Upper": LocationData(2),  # schmove
        "Hydro Station: Below Tower Pipe Lower": LocationData(2),
        "Hydro Station: Dead End Missile ": LocationData(2),
        "Hydro Station: Hi Jump": LocationData(2),
        "Hydro Station: Behind Hi Jump Upper": LocationData(2),
        "Hydro Station: Behind Hi Jump": LocationData(2),
        "Hydro Station: Clif": LocationData(2),
    },
    "Hydro Nest":{  # Jump
        "Hydro Nest: Below the Walkway": LocationData(2),  # Bomb
        "Hydro Nest: Speed Celling": LocationData(2),  # speed
        "Hydro Nest: Behind the Wall": LocationData(2), # PB + screw/speed
    },
    "Pre Industrial Complex":{
        "Pre Industrial Complex: Maze": LocationData(2),
        "Pre Industrial Complex: Above Save": LocationData(2),
        "Pre Industrial Complex: Nest Super": LocationData(2),  # super + schmove
        "Pre Industrial Complex: EMP room": LocationData(2),  # PB + super
        "Pre Industrial Complex: In the Sand": LocationData(2),
        "Pre Industrial Complex: Space Jump": LocationData(2),  # schmove
        "Pre Industrial Complex: Complex Side After Tunnel": LocationData(2),
        "Pre Industrial Complex: Complex Side Tunnel": LocationData(2),
        "Industrial Complex: Save Room": LocationData(2),
        "Industrial Complex: Spazer": LocationData(2),
        "Industrial Complex: Speed Booster": LocationData(2),  # bomb
    },
    "Industrial Complex":{
        "Industrial Complex: Gama Spark": LocationData(2),
        "Industrial Complex: Conveyor Belt Room": LocationData(2),
        "Industrial Complex: Guarded by the Alpha": LocationData(2),
        "Industrial Complex: Robot room in the Wall": LocationData(2),
        "Industrial Complex: Robot room un the Floor": LocationData(2),
        "Industrial Complex: First Supers": LocationData(2, "Super Missile", ammo.static),  # todo static ammo
    },
    "GFS Thoth":{  # PB
        "GFS Thoth: Hornoad room": LocationData(2),
        "GFS Thoth: Outside the Front of the Ship": LocationData(2),
        "GFS Thoth: Genesis": LocationData(2),
    },
    "The Tower":{
        "The Tower: Beside Hydro Pipe": LocationData(2),
        "The Tower: Right Side of Tower": LocationData(2),
        "The Tower: In the Ceiling": LocationData(2),  # schmove + bomb
        "The Tower: Dark Maze": LocationData(2),  #
        "The Tower: Outside the Dark Maze": LocationData(2),
        "The Tower: Plasma Beam": LocationData(2),
        "The Tower: Beside Tester": LocationData(2),  # pb
        "The Tower: Left side of tower": LocationData(2),  # pb
        "The Tower: Geothermal Reactor": LocationData(2, "Power Bombs", ammo.static),  # todo static ammo
        "The Tower: Post Geothermal Chozo": LocationData(2),  # pb
        "The Tower: Post Geothermal Shinespark": LocationData(2),  # Pb + spped + super
    },
    "Distribution Center":{
        "Distribution Center: Main Room Shinespark": LocationData(2),  # grav + screw
        "Distribution Center: After EMP Activation": LocationData(2),  # screw
        "Distribution Center: Screw Attack": LocationData(2),
        "Distribution Center: Before Gravity": LocationData(2),  # bomb + charge/gravity / PB
        "Distribution Center: Gravity": LocationData(2),  # can bomb
        "Distribution Center: Outside after Gravity": LocationData(2),  # pb + space + grav
        "Distribution Center: Before Underwater Pipe": LocationData(2),  # pb + speed
        "Distribution Center: Ice Beam": LocationData(2),  # grav + speed / Supers
        "Distribution Center: Spiderball Spike Maze": LocationData(2),  # spiderball
        "Distribution Center: Before Spike tunnel room": LocationData(2),
        "Distribution Center: Spike Tunnel room Shinespark": LocationData(2), # grav + speed
        "Distribution Center: After Spike Tunnel Room": LocationData(2), # speed + grav + space + pb
        "Distribution Center: Speed Hallway": LocationData(2),  # speed + grav
    },
    "Deep Caves":{  # can down
        "Deep Caves: Ball Spark": LocationData(2),
        "Deep Caves: Behind the Bomb Block": LocationData(2),
        "Deep Caves: After Omega": LocationData(2),

    }
}
