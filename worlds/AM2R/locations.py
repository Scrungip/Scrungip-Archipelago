import typing

from BaseClasses import Location


class AM2RLocation(Location):
    game: str = "AM2R"

    def __int__(self, player: int, name: str, address: typing.Optional[int], parent):
        super(). __init__(player, name, address, parent)
        self.event = not address


# todo actual location numbers
location_table = {
    "Main Caves: Vertical Spike Room Upper": LocationData(2, "Main Caves"),  # spider + bomb
    "Main Caves: Vertical Spike Room Lower": LocationData(2, "Main Caves"),  # bomb
    "Main Caves: Crumble Spike Room": LocationData(2, "Main Caves"),  # jump
    "Main Caves: Maze": LocationData(2, "Main Caves"),
    "Main Caves: Shinespark Before the drop": LocationData(2, "Main Caves"),  # speed
    "Main Caves: Shinespark After the drop": LocationData(2, "Main Caves"),  # speed

    "Golden Temple: Bombs": LocationData(2, "Golden Temple"),
    "Golden Temple: Missile below Bombs": LocationData(2, "Golden Temple"),  # bomb
    "Golden Temple: Hidden Energy Tank": LocationData(2, "Golden Temple"),  # bomb
    "Golden Temple: Charge Beam": LocationData(2, "Golden Temple"),
    "Golden Temple: Armory 1": LocationData(2, "Golden Temple"),
    "Golden Temple: Armory 2": LocationData(2, "Golden Temple"),
    "Golden Temple: Armory 3": LocationData(2, "Golden Temple"),
    "Golden Temple: Armory Missile False Wall ": LocationData(2, "Golden Temple"),  # bomb
    "Golden Temple: Puzzle Room Missle 1": LocationData(2, "Golden Temple"),
    "Golden Temple: Puzzle Room Missle 2": LocationData(2, "Golden Temple"),
    "Golden Temple: Puzzle Room Energy Tank": LocationData(2, "Golden Temple"),
    "Golden Temple: Spider Ball": LocationData(2, "Golden Temple"),
    "Golden Temple: Celling Missile": LocationData(2, "Golden Temple"),  # canspider
    "Golden Temple: EMP room": LocationData(2, "Golden Temple"),  # super + ballspark

    "Guardian: Up Above": LocationData(2, "Guardian"),  # bomb + schmove
    "Guardian: Behind The Door": LocationData(2, "Guardian"),  # PB + schmove

    "Hydro Station: Clif": LocationData(2, "Hydro Station"),
    "Hydro Station: Morph Tunnel": LocationData(2, "Hydro Station"),
    "Hydro Station: Arachnus": LocationData(2, "Hydro Station"),  # bomb
    "Hydro Station: Turbine Room": LocationData(2, "Hydro Station"),  # bomb
    "Hydro Station: Not so Secret Tunel": LocationData(2, "Hydro Station"),  # schmove
    "Hydro Station: Water puzzle Beside Varia": LocationData(2, "Hydro Station"),  # bomb
    "Hydro Station: Varia Suit": LocationData(2, "Hydro Station"),  # bomb
    "Hydro Station: EMP room": LocationData(2, "Hydro Station"),  # super + speed
    "Hydro Station: Wave Beam": LocationData(2, "Inner Hydro Station"),
    "Hydro Station: Below Tower Pipe Upper": LocationData(2, "Inner Hydro Station"),  # schmove
    "Hydro Station: Below Tower Pipe Lower": LocationData(2, "Inner Hydro Station"),
    "Hydro Station: Dead End Missile ": LocationData(2, "Inner Hydro Station"),
    "Hydro Station: Hi Jump": LocationData(2, "Inner Hydro Station"),
    "Hydro Station: Behind Hi Jump Upper": LocationData(2, "Inner Hydro Station"),
    "Hydro Station: Behind Hi Jump": LocationData(2, "Inner Hydro Station"),

    "Hydro Nest: Below the Walkway": LocationData(2, "Hydro Nest"),  # Bomb
    "Hydro Nest: Speed Celling": LocationData(2, "Hydro Nest"),  # speed
    "Hydro Nest: Behind the Wall": LocationData(2, "Hydro Nest"), # PB + screw/speed

    "Industrial Complex Nest: Above Save": LocationData(2, "Industrial Complex Nest"),
    "Industrial Complex Nest: EMP room": LocationData(2, "Industrial Complex Nest"),  # PB + super
    "Industrial Complex Nest: Nest Super": LocationData(2, "Industrial Complex Nest"),  # super + schmove

    "Pre Industrial Complex: In the Sand": LocationData(2, "Pre Industrial Complex"),
    "Pre Industrial Complex: Space Jump": LocationData(2, "Pre Industrial Complex"),  # schmove
    "Pre Industrial Complex: Complex Side After Tunnel": LocationData(2, "Pre Industrial Complex"),
    "Pre Industrial Complex: Complex Side Tunnel": LocationData(2, "Pre Industrial Complex"),
    "Industrial Complex: Save Room": LocationData(2, "Pre Industrial Complex"),
    "Industrial Complex: Spazer": LocationData(2, "Pre Industrial Complex"),
    "Industrial Complex: Speed Booster": LocationData(2, "Pre Industrial Complex"),  # bomb

    "Industrial Complex: Gama Spark": LocationData(2, "Industrial Complex"),
    "Industrial Complex: Conveyor Belt Room": LocationData(2, "Industrial Complex"),
    "Industrial Complex: Guarded by the Alpha": LocationData(2, "Industrial Complex"),
    "Industrial Complex: Robot room in the Wall": LocationData(2, "Industrial Complex"),
    "Industrial Complex: Robot room un the Floor": LocationData(2, "Industrial Complex"),
    "Industrial Complex: First Supers": LocationData(2, "Industrial Complex"),

    "GFS Thoth: Research Camp": LocationData(2, "GFS Thoth"),
    "GFS Thoth: Hornoad room": LocationData(2, "GFS Thoth"),
    "GFS Thoth: Outside the Front of the Ship": LocationData(2, "GFS Thoth"),
    "GFS Thoth: Genesis": LocationData(2, "GFS Thoth"),

    "The Tower: Beside Hydro Pipe": LocationData(2, "The Tower"),
    "The Tower: Right Side of Tower": LocationData(2, "The Tower"),
    "The Tower: In the Ceiling": LocationData(2, "The Tower"),  # schmove + bomb
    "The Tower: Dark Maze": LocationData(2, "The Tower"),  #
    "The Tower: Outside the Dark Maze": LocationData(2, "The Tower"),
    "The Tower: Plasma Beam": LocationData(2, "The Tower"),
    "The Tower: Beside Tester": LocationData(2, "The Tower"),  # pb
    "The Tower: Left side of tower": LocationData(2, "The Tower"),  # pb
    "The Tower: Geothermal Reactor": LocationData(2, "The Tower"),
    "The Tower: Post Geothermal Chozo": LocationData(2, "The Tower"),  # pb
    "The Tower: Post Geothermal Shinespark": LocationData(2, "The Tower"),  # Pb + spped + super

    "Distribution Center: Main Room Shinespark": LocationData(2, "Distribution Center"),  # grav + screw
    "Distribution Center: After EMP Activation": LocationData(2, "Distribution Center"),  # screw
    "Distribution Center: Screw Attack": LocationData(2, "Distribution Center"),
    "Distribution Center: Before Gravity": LocationData(2, "Distribution Center"),  # bomb + charge/gravity / PB
    "Distribution Center: Gravity": LocationData(2, "Distribution Center"),  # can bomb
    "Distribution Center: Outside after Gravity": LocationData(2, "Distribution Center"),  # pb + space + grav
    "Distribution Center: Before Underwater Pipe": LocationData(2, "Distribution Center"),  # pb + speed
    "Distribution Center: Ice Beam": LocationData(2, "Distribution Center"),  # grav + speed / Supers
    "Distribution Center: Spiderball Spike Maze": LocationData(2, "Distribution Center"),  # spiderball
    "Distribution Center: Before Spike tunnel room": LocationData(2, "Distribution Center"),
    "Distribution Center: Spike Tunnel room Shinespark": LocationData(2, "Distribution Center"),  # grav + speed
    "Distribution Center: After Spike Tunnel Room": LocationData(2, "Distribution Center"),  # speed + grav + space + pb
    "Distribution Center: Speed Hallway": LocationData(2, "Distribution Center"),  # speed + grav

    "Deep Caves: Ball Spark": LocationData(2, "Deep Caves"),
    "Deep Caves: Behind the Bomb Block": LocationData(2, "Deep Caves"),
    "Deep Caves: After Omega": LocationData(2, "Deep Caves"),
}