from typing import List, Tuple, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld, CollectionState
from .options import is_option_enabled
from .rules import AM2RLogic


EventId: Optional[int] = None


class LocationData(NamedTuple):
    region: str
    name: str
    code: Optional[int]
    rule: Callable[[CollectionState], bool] = lambda state: True

def get_location_datas(world: Optional[MultiWorld], player: Optional[int]):
    location_table = [LocationData, ...]
    logic = AM2RLogic(world, player)

    location_table: List[LocationData] = [
        LocationData("Main Caves", "Main Caves: Vertical Spike Room Upper",  8680000, lambda state: state.has("Spider Ball", player) and logic.AM2R_can_bomb(state)),  # spider + bomb
        LocationData("Main Caves", "Main Caves: Vertical Spike Room Lower",  8680001, logic.AM2R_can_bomb),  # bomb
        LocationData("Main Caves", "Main Caves: Crumble Spike Room",  8680002, logic.AM2R_can_jump),  # jump
        LocationData("Main Caves", "Main Caves: Maze",  8680003),
        LocationData("Main Caves", "Main Caves: Shinespark Before the drop",  8680004, lambda state: state.has("Speed Booster", player)),  # speed
        LocationData("Main Caves", "Main Caves: Shinespark After the drop",  8680005, lambda state: state.has("Speed Booster", player)),  # speed

        LocationData("Golden Temple", "Golden Temple: Bombs",  8680006),
        LocationData("Golden Temple", "Golden Temple: Missile below Bombs",  8680007, logic.AM2R_can_bomb),  # bomb
        LocationData("Golden Temple", "Golden Temple: Hidden Energy Tank",  8680008, logic.AM2R_can_bomb),  # bomb
        LocationData("Golden Temple", "Golden Temple: Charge Beam",  8680009),
        LocationData("Golden Temple", "Golden Temple: Armory 1",  8680010),
        LocationData("Golden Temple", "Golden Temple: Armory 2",  8680011),
        LocationData("Golden Temple", "Golden Temple: Armory 3",  8680012),
        LocationData("Golden Temple", "Golden Temple: Armory Missile False Wall ",  8680013, logic.AM2R_can_bomb),  # bomb
        LocationData("Golden Temple", "Golden Temple: Puzzle Room Missle 1",  8680014),
        LocationData("Golden Temple", "Golden Temple: Puzzle Room Missle 2",  8680015),
        LocationData("Golden Temple", "Golden Temple: Puzzle Room Energy Tank",  8680016),
        LocationData("Golden Temple", "Golden Temple: Spider Ball",  8680017),
        LocationData("Golden Temple", "Golden Temple: Celling Missile",  8680018, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider),  # canspider
        LocationData("Golden Temple", "Golden Temple: EMP room",  8680019, lambda state: state.has("Super Missile", player) and logic.AM2R_has_ballspark),  # super + ballspark

        LocationData("Guardian", "Guardian: Up Above",  8680020, lambda state: logic.AM2R_can_bomb(state) and logic.AM2R_can_schmove(state)),  # bomb + schmove
        LocationData("Guardian", "Guardian: Behind The Door",  8680021, lambda state: state.has("Power Bomb", player) and logic.AM2R_can_schmove(state)),  # PB + schmove

        LocationData("Hydro Station", "Hydro Station: Clif",  8680022),
        LocationData("Hydro Station", "Hydro Station: Morph Tunnel",  8680023),
        LocationData("Hydro Station", "Hydro Station: Turbine Room",  8680024, logic.AM2R_can_bomb),  # bomb
        LocationData("Hydro Station", "Hydro Station: Not so Secret Tunel",  8680025, logic.AM2R_can_schmove),  # schmove
        LocationData("Hydro Station", "Hydro Station: Water puzzle Beside Varia",  8680026, logic.AM2R_can_bomb),  # bomb
        LocationData("Hydro Station", "Hydro Station: Varia Suit",  8680027, logic.AM2R_can_bomb),  # bomb
        LocationData("Hydro Station", "Hydro Station: EMP room",  8680028, lambda state: state.has("Super Missile", player) and state.has("Speed Booster", player)),  # super + speed

        LocationData("Arachnus", "Arachnus: Boss", 8680029),

        LocationData("Inner Hydro Station", "Hydro Station: Wave Beam",  8680030, logic.AM2R_can_bomb),
        LocationData("Inner Hydro Station", "Hydro Station: Below Tower Pipe Upper",  8680031, lambda state: logic.AM2R_can_schmove(state) and logic.AM2R_can_bomb(state)),  # schmove
        LocationData("Inner Hydro Station", "Hydro Station: Below Tower Pipe Lower",  8680032,  logic.AM2R_can_bomb),
        LocationData("Inner Hydro Station", "Hydro Station: Dead End Missile ",  8680033,  logic.AM2R_can_bomb),
        LocationData("Inner Hydro Station", "Hydro Station: Hi Jump",  8680034),
        LocationData("Inner Hydro Station", "Hydro Station: Behind Hi Jump Upper",  8680035, lambda state: logic.AM2R_can_schmove(state) and logic.AM2R_can_bomb(state)),
        LocationData("Inner Hydro Station", "Hydro Station: Behind Hi Jump",  8680036, logic.AM2R_can_bomb),

        LocationData("Hydro Nest", "Hydro Nest: Below the Walkway",  8680037, logic.AM2R_can_bomb),  # Bomb
        LocationData("Hydro Nest", "Hydro Nest: Speed Celling",  8680038, lambda state: state.has("Speed Booster", player)),  # speed
        LocationData("Hydro Nest", "Hydro Nest: Behind the Wall",  8680039, lambda state: state.has("Power Bomb", player) and (state.has("Screw Attack") or state.has("Speed Booster"))),  # PB + screw/speed

        LocationData("Industrial Complex Nest", "Industrial Complex: Above Save",  8680040),
        LocationData("Industrial Complex Nest", "Industrial Complex: EMP Room",  8680041, lambda state: state.has("Power Bomb", player) and state.has("Super Missile", player)),  # PB + super
        LocationData("Industrial Complex Nest", "Industrial Complex Nest: Nest Shinespark",  8680042, lambda state: state.has("Super Missile", player) and state.has("Speed Booster", player)),  # super + schmove

        LocationData("Pre Industrial Complex", "Industrial Complex: In the Sand",  8680043),
        LocationData("Pre Industrial Complex", "Industrial Complex: Complex Side After Tunnel",  8680044, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Complex Side Tunnel",  8680045, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Save Room",  8680046, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Spazer",  8680047, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_spider(state)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Gama Spark",  8680048, lambda state: state.has("Speed Booster", player)),
        LocationData("Pre Industrial Complex", "Industrial Complex: Speed Booster",  8680049, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_bomb(state)),  # bomb

        LocationData("Torizo Ascended", "Torizo Ascended: Boss", 8680050, logic.AM2R_can_schmove),

        LocationData("Industrial Complex", "Industrial Complex: Conveyor Belt Room",  8680051, lambda state: state.has("Speed Booster", player)),
        LocationData("Industrial Complex", "Industrial Complex: Guarded by the Alpha",  8680052, lambda state: state.has("Speed Booster", player) or logic.AM2R_can_fly(state)),
        LocationData("Industrial Complex", "Industrial Complex: Robot room in the Wall",  8680053, lambda state: state.has("Speed Booster", player)),
        LocationData("Industrial Complex", "Industrial Complex: Robot room in the Floor", 8680054, lambda state: state.has("Super Missile", player) and (state.has("Speed Booster", player) or logic.AM2R_can_fly(state))),
        LocationData("Industrial Complex", "Industrial Complex: First Supers",  8680055),

        LocationData("GFS Thoth", "GFS Thoth: Research Camp",  8680056),
        LocationData("GFS Thoth", "GFS Thoth: Hornoad room",  8680057, lambda state: state.has("Power Bomb", player)),
        LocationData("GFS Thoth", "GFS Thoth: Outside the Front of the Ship",  8680058, lambda state: state.has("Power Bomb", player)),
        LocationData("GFS Thoth", "GFS Thoth: Genesis",  8680059, lambda state: state.has("Power Bomb", player)),

        LocationData("The Tower", "The Tower: Beside Hydro Pipe",  8680060, lambda state: state.has("Screw Attack", player)),
        LocationData("The Tower", "The Tower: Right Side of Tower",  8680061),
        LocationData("The Tower", "The Tower: In the Ceiling",  8680062, lambda state: logic.AM2R_can_bomb(state) and logic.AM2R_can_schmove(state)),  # schmove + bomb
        LocationData("The Tower", "The Tower: Dark Maze",  8680063, logic.AM2R_can_bomb),  # bomb
        LocationData("The Tower", "The Tower: Outside the Dark Maze",  8680064, logic.AM2R_can_bomb),
        LocationData("The Tower", "The Tower: Plasma Beam",  8680065, lambda state: logic.AM2R_can_bomb(state) and state.can_reach("Tester", "Region", player)),
        LocationData("The Tower", "The Tower: Beside Tester",  8680066, lambda state: state.has("Power Bomb", player)),  # pb
        LocationData("The Tower", "The Tower: Left side of tower",  8680067, lambda state: state.has("Power Bomb", player)),  # pb

        LocationData("Geothermal", "The Tower: Geothermal Reactor",  8680068),
        LocationData("Geothermal", "The Tower: Post Geothermal Chozo",  8680069, lambda state: state.has("Power Bomb", player)),  # pb
        LocationData("Geothermal", "The Tower: Post Geothermal Shinespark",  8680070, lambda state: state.has("Power Bomb", player) and state.has("Speed Booster", player) and state.has("", player)),  # Pb + spped + super

        LocationData("Underwater Distribution Center", "Distribution Center: Main Room Shinespark",  8680071, lambda state: state.has("Gravity Suit", player) and state.has("Speed Booster")),  # grav + screw
        LocationData("Underwater Distribution Center", "Distribution Center: Speed Hallway",  8680072, lambda state: state.has("Speed Booster", player) and state.has("Gravity Suit", player)),  # speed + grav

        LocationData("EMP", "Distribution Center: After EMP Activation",  8680073, lambda state: state.has("Screw Attack", player)),  # screw

        LocationData("Underwater Distro Connection", "Distribution Center: Spiderball Spike \"Maze\"",  8680074, lambda state: state.has("Spider_Ball", player)),  # spiderball
        LocationData("Underwater Distro Connection", "Distribution Center: Before Spikey Tunnel",  8680075),
        LocationData("Underwater Distro Connection", "Distribution Center: Spikey Tunnel Shinespark",  8680076, lambda state: state.has("Gravity Suit", player) and state.has("Speed Booster", player)),  # grav + speed
        LocationData("Underwater Distro Connection", "Distribution Center: After Spikey Tunnel",  8680078, lambda state: state.has("Power Bomb", player) and state.has("Speed Booster", player) and state.has("Gravity Suit", player) and state.has("Space_Jump", player)),  # speed + grav + space + pb

        LocationData("Pipe Hell R", "Distribution Center: Screw Attack", 8680080),
        LocationData("Pipe Hell Outside", "Distribution Center: Outside after Gravity", 8680081, lambda state: state.has("Power Bomb", player) and state.has("Space_Jump", player) and state.has("Gravity Suit", player)),  # pb + space + grav
        LocationData("Pipe Hell R", "Distribution Center: Before Underwater Pipe", 8680082, lambda state: state.has("Power Bomb", player) and state.has("Speed Booster", player)),  # pb + speed

        LocationData("Gravity", "Distribution Center: Before Gravity", 8680083, lambda state: (state.has("Bombs", player) and (state.has("ChargeBeam", player) or state.has("Gravity Suit", player))) or state.has("Power Bomb", player)),  # bomb + charge/gravity / PB
        LocationData("Gravity", "Distribution Center: Gravity", 8680084, logic.AM2R_can_bomb),  # can bomb

        LocationData("Ice Beam", "Serris: Ice Beam", 8680085, lambda state: state.has("Ice Beam", player) and (state.has("Super Missile", player) or state.has("Speed Booster", player))),  # speed / Supers

        LocationData("Deep Caves", "Deep Caves: Ball Spark",  8680086, logic.AM2R_has_ballspark),
        LocationData("Deep Caves", "Deep Caves: Behind the Bomb Block",  8680087, logic.AM2R_can_bomb),

        LocationData("Deep Caves", "Deep Caves: After Omega",  8680088),
        #metroids

        LocationData("First Alpha", "The Forgotten Alpha", 8680100),

        LocationData("Golden Temple", "Golden Temple: Metroid above Spider Ball", 8680101, logic.AM2R_can_spider),
        LocationData("Golden Temple Nest", "Golden Temple Nest: Metroid 1", 8680102, logic.AM2R_can_bomb),
        LocationData("Golden Temple Nest", "Golden Temple Nest: Metroid 2", 8680103, logic.AM2R_can_bomb),
        LocationData("Golden Temple Nest", "Golden Temple Nest: Metroid 3", 8680104, logic.AM2R_can_bomb),

        LocationData("Main Caves", "Main Caves: Metroid before Hydro Station", 8680105),
        LocationData("Hydro Station", "Hydro Station: Metroid Turbine Terror", 8680106),
        LocationData("Hydro Station", "Hydro Station: Metroid up above", 8680107, logic.AM2R_can_schmove),
        LocationData("Hydro Station", "Hydro Station: Metroid guarding the way inside", 8680108),

        LocationData("Hydro Nest", "Hydro Station Nest: Metroid 1", 8680109),
        LocationData("Hydro Nest", "Hydro Station Nest: Metroid 2", 8680110),
        LocationData("Hydro Nest", "Hydro Station Nest: Metroid 3", 8680111),
        LocationData("Hydro Nest", "Hydro Station Nest: Surprise!", 8680112),

        LocationData("Industrial Complex Nest", "Industrial Nest: Metroid 1", 8680113, lambda state: state.has("Speed Booster", player) or state.has("Super Missile", player)),
        LocationData("Industrial Complex Nest", "Industrial Nest: Metroid 2", 8680114, lambda state: state.has("Speed Booster", player) or state.has("Super Missile", player)),
        LocationData("Industrial Complex Nest", "Industrial Nest: Metroid 3", 8680115, lambda state: state.has("Speed Booster", player) or state.has("Super Missile", player)),
        LocationData("Industrial Complex Nest", "Industrial Nest: Metroid 4", 8680116, lambda state: state.has("Speed Booster", player) or state.has("Super Missile", player)),
        LocationData("Industrial Complex Nest", "Industrial Nest: Gama in your floors", 8680117, lambda state: logic.AM2R_can_bomb(state) and (state.has("Speed Booster", player) or state.has("Super Missile", player))),
        LocationData("Industrial Complex Nest", "Industrial Nest: At the end of the road", 8680118, lambda state: logic.AM2R_can_bomb(state) and state.has("Spider_Ball", player) and (state.has("Speed Booster", player) or state.has("Super Missile", player))),

        LocationData("Pre Industrial Complex", "Industrial Complex: Shinespark denier Gama", 8680119),
        LocationData("Pre Industrial Complex", "Industrial Complex: Gama Off to the Right", 8680120),

        LocationData("Industrial Complex", "Industrial Complex: Guardian of doom treadmill", 8680121),
        LocationData("Industrial Complex", "Industrial Complex: Super Missile Test Subject", 8680121),

        LocationData("GFS Thoth", "Dual Alphas: Fred", 8680123),
        LocationData("GFS Thoth", "Dual Alphas: George", 8680124),

        LocationData("Mines", "Mines: Alpha", 8680125, lambda state: state.has("Super Missile", player) and (logic.AM2R_can_fly(state) or state.has("Speed Booster", player))),
        LocationData("Mines", "Mines: Gama", 8680126, lambda state: state.has("Super Missile", player) and (logic.AM2R_can_fly(state) or state.has("Speed Booster", player))),

        LocationData("The Tower", "The Tower: Metroid 1", 8680127, logic.AM2R_can_spider),
        LocationData("The Tower", "The Tower: Metroid 2", 8680128, logic.AM2R_can_fly),
        LocationData("The Tower", "The Tower: Metroid 3", 8680129, logic.AM2R_can_schmove),
        LocationData("The Tower", "The Tower: Metroid 4", 8680130, logic.AM2R_can_bomb),
        LocationData("The Tower", "The Tower: Metroid 5", 8680131, logic.AM2R_can_fly),
        LocationData("The Tower", "The Tower: Metroid 6", 8680132, logic.AM2R_can_fly),

        LocationData("EMP", "EMP: Sir Zeta Commander of the Alpha Squadron", 8680133),

        LocationData("Pipe Hell R", "Alpha Squadron: Timmy", 8680134),
        LocationData("Pipe Hell R", "Alpha Squadron: Tommy", 8680135),
        LocationData("Pipe Hell R", "Alpha Squadron: Terry", 8680136),
        LocationData("Pipe Hell R", "Alpha Squadron: Telly", 8680137),
        LocationData("Pipe Hell R", "Alpha Squadron: Martin", 8680138),

        LocationData("Underwater Distro Connection", "Underwater: Gama Bros Mario", 8680139),
        LocationData("Underwater Distro Connection", "Underwater: Gama Bros Luigi", 8680140),

        LocationData("Deep Caves", "Deep Caves: Little Bro", 8680141),
        LocationData("Deep Caves", "Deep Caves: Big Sis", 8680142),
        LocationData("Deep Caves", "Omega Nest: Metroid 3", 8680143),
        LocationData("Deep Caves", "Omega Nest: Metroid 4", 8680144),
        LocationData("Deep Caves", "Omega Nest: Metroid 5", 8680145),

        LocationData("Research Station", "The Last Metroid is in Captivity", EventId),
    ]

    return tuple(location_table)
