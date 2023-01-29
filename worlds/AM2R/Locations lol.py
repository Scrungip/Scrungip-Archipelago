from typing import List, Tuple, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld
#from .Options import is_option_enabled
#not utilized yet but in the future maybe

EventId: Optional[int] = None


class LocationData(NamedTuple):
    region: str
    name: str
    code: Optional[int]
    rule: Callable = lambda state: True


def get_locations(world: Optional[MultiWorld], player: Optional[int]) -> Tuple[LocationData, ...]:
    location_table: List[LocationData] = [
        LocationData('Golden Temple', 'Conner', 0),
        LocationData('Golden Temple', 'Golden Temple: Missile below Bombs', 0),
        LocationData('Golden Temple', 'Golden Temple: Hidden Energy Tank', 0),  # bombs
        LocationData('Golden Temple', 'Golden Temple: Charge Beam', 0),
        LocationData('Golden Temple', 'Golden Temple: Armory Missile 1', 0),
        LocationData('Golden Temple', 'Golden Temple: Armory Missile 2', 0),
        LocationData('Golden Temple', 'Golden Temple: Armory Missile 3', 0),
        LocationData('Golden Temple', 'Golden Temple: Armory False Wall Missile', 0),  # bombs
        LocationData('Golden Temple', 'Golden Temple: Puzzle room Energy Tank', 0),
        LocationData('Golden Temple', 'Golden Temple: Puzzle room Missile 1', 0),
        LocationData('Golden Temple', 'Golden Temple: Puzzle room Missile 2', 0),
        LocationData('Golden Temple', 'Sensokaeru', 0),
        LocationData('Golden Temple', 'Gerald', 0),  # spider/space
        LocationData('Golden Temple', 'Golden Temple: EMP Room Super Missile', 0),  # Screw + Supers + Speed + EMP + spring
        LocationData('Golden Temple', 'Golden Temple: Above Guardian Missile', 0),  # Bombs + vertical/spider
        LocationData('Golden Temple', 'Golden Temple: Above Guardian Power Bombs', 0),  # power bombs + any vertical/spider
        LocationData('Main Caves', 'Main Caves: Vertical Spike Puzzle Missile upper', 0),  # Bombs + infinite vertical/spiderball
        LocationData('Main Caves', 'Main Caves: Vertical Spike Puzzle Missile lower', 0),  # Bombs
        LocationData('Main Caves', 'Main Caves: Crumble Spike Room Missile', 0),  # Bombs + Vertical
        LocationData('Main Caves', 'Main Caves: Speedboost Puzzle Skorp Missile', 0),  # speed
        LocationData('Main Caves', 'Main Caves: Speedboost Puzzle Pincherfly Missile', 0),  # speed
        LocationData('Hydro Station', 'Hydro Station: Clif Missile', 0),
        LocationData('Hydro Station', 'Hydro Station: Morph Tunnel Missile', 0),
        LocationData('Hydro Station', 'Ivy', 0),  # bombs
        LocationData('Hydro Station', 'Hydro Station: Turbine Room Missile', 0),  # bombs
        LocationData('Hydro Station', 'Hydro Station: Water Jet Beside Tower Pipe Missile', 0),  # vertical/spider
        LocationData('Hydro Station', 'Hydro Station: Water Puzzle Beside Varia', 0),  # Bombs + vertical/spider
        LocationData('Hydro Station', 'Hydro Station: Varia Suit', 0),  # bombs
        LocationData('Hydro Station', 'Hydro Station: EMP Room Super Missile', 0),  # Speed + Supers + EMP
        LocationData('Inner Hydro Station', 'Inner Hydro Station: Wave Beam', 0),
        LocationData('Inner Hydro Station', 'Inner Hydro Station: Below Tower Pipe Missile Upper', 0),  # spider/vertical
        LocationData('Inner Hydro Station', 'Inner Hydro Station: Below Tower Pipe Missile Lower', 0),
        LocationData('Inner Hydro Station', 'Inner Hydro Station: Dead End Missile', 0),
        LocationData('Inner Hydro Station', 'Ehseezed', 0),
        LocationData('Inner Hydro Station', 'Inner Hydro Station: Behind Hi Jump Energy Tank', 0),
        LocationData('Inner Hydro Station', 'Inner Hydro Station: Behind Hi Jump Missile', 0),  # vertical
        LocationData('Hydro Nest', 'Hydro Nest: Energy Tank', 0),  # bombs
        LocationData('Hydro Nest', 'Hydro Nest: Power Bombs', 0),  # screw/speed + powerbombs
        LocationData('Hydro Nest', 'Hydro Nest Missile', 0),  # speed
        LocationData('Pre Industrial Complex', 'Pre Industrial Complex: Maze Missile', 0),
        LocationData('Pre Industrial Complex', 'Pre Industrial Complex: Above Save Missile', 0),
        LocationData('Pre Industrial Complex', 'Basil', 0),
        LocationData('Pre Industrial Complex', 'Pre Industrial Complex EMP Room Power Bomb', 0),  # power bomb + EMP
        LocationData('Pre Industrial Complex', 'Pre Industrial Complex: Sand Missile', 0),
        LocationData('Pre Industrial Complex', 'Pre Industrial Complex: Space Jump', 0),  # vertical/Spider
        LocationData('Pre Industrial Complex', 'Industrial Complex: Save Room Missile', 0),
        LocationData('Pre Industrial Complex', 'Epsilon', 0),
        LocationData('Pre Industrial Complex', 'Xander', 0),  # bombs
        LocationData('Pre Industrial Complex', 'EnderMahan', 0),  # speed + supers + PB
        LocationData('Industrial Complex', 'Industrial Complex: Gama Metroid Spark Missile', 0),  # speed
        LocationData('Industrial Complex', 'Industrial Complex: Conveyor Belt Room Missile ', 0),  # speed
        LocationData('Industrial Complex', 'Industrial Complex: Alpha Metroid Energy Tank', 0),  # speed
        LocationData('Industrial Complex', 'Industrial Complex: Robot Room Missile', 0),  # speed
        LocationData('Industrial Complex', 'Industrial Complex: Robot Room Super Missile', 0),  # speed + Supers
        LocationData('Industrial Complex', 'Industrial Complex: First Super Missile', 0),  # speed
        LocationData('Industrial Complex', 'Industrial Complex: Complex Side Energy Tank', 0),
        LocationData('Industrial Complex', 'Industrial Complex: Complex Side Missile', 0),
        LocationData('Main Caves', 'Main Caves: Research Camp Super Missile', 0),
        LocationData('GFS Thoth', 'Sytrow ', 0),
        LocationData('GFS Thoth', 'rawsome1234', 0),
        LocationData('GFS Thoth', 'Pablo', 0),
        LocationData('The Tower', 'The Tower: Beside Hydro Pipe Missile', 0),  # Screw
        LocationData('The Tower', 'The Tower: Right Side Tower Missile', 0),
        LocationData('The Tower', 'The Tower: Ceiling Missile', 0),  # spider
        LocationData('The Tower', 'The Tower: Dark Maze Missile', 0),  # bomb
        LocationData('The Tower', 'The Tower: Dark Maze Energy Tank', 0),  # bomb
        LocationData('The Tower', 'NotQuiteHere', 0),  # Bomb
        LocationData('The Tower', 'The Tower: Beside Tester Super Missile', 0),  # Power Bombs
        LocationData('The Tower', 'The Tower: Left side Tower Power Bombs', 0),  # PB
        LocationData('The Tower', 'Lober', 0),
        LocationData('The Tower', 'The Tower: Post Geothermal Energy Tank', 0),  # PB
        LocationData('The Tower', 'The Tower: Post Geothermal Missile', 0),  # PB + Supers + Speed
        LocationData('Distribution Center', 'Distribution Center: EMP Screw Puzzle Super Missile', 0),  # speed + screw
        LocationData('Distribution Center', 'Distribution Center: Screw Attack', 0),  # Space/Speed
        LocationData('Distribution Center', 'Distribution Center: Before Gravity', 0),  # Bombs + charge / Bomb + grav / PB
        LocationData('Distribution Center', 'Distribution Center: Gravity Suit', 0),  # bombs
        LocationData('Distribution Center', 'BHHarbinger', 0), # Speed
        LocationData('Distribution Center', 'Distribution Center: Outside Power Bombs', 0),  # PB + Space
        LocationData('Distribution Center', 'Distribution Center: Ice Beam', 0),  # speed/super
        LocationData('Distribution Center', 'Distribution Center: Spiderball Puzzle Missile', 0),  # Spiderball
        LocationData('Distribution Center', 'Distribution Center: Before Speed Puzzle Missile', 0),  # speed = screw/pb
        LocationData('Distribution Center', 'Distribution Center: Speed Puzzle Super Missile', 0),  # speed
        LocationData('Distribution Center', 'Distribution Center: Speed Puzzle Energy Tank', 0), # speed + space + bomb
        LocationData('Distribution Center', 'Distribution Center: Speed Hallway Missile', 0), # speed
        LocationData('Distribution Center', 'Distribution Center: Main Room Speed Missile', 0),
        LocationData('Deep Caves', 'Deep Caves: Ball Spark Puzzle Missile ', 0),
        LocationData('Deep Caves', 'Deep Caves: Hidden Missile ', 0),
        LocationData('Deep Caves', 'Nick', 0),
    ]