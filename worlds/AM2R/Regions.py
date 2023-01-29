from typing import List, Set, Dict, Tuple, Optional, Callable
from BaseClasses import MultiWorld, Region, Entrance, Location, RegionType
from .Options import is_option_enabled
from .Locations import LocationData


def create_regions(world: MultiWorld, player: int, locations: Tuple[LocationData, ...], location_cache: List[Location]):
    locations_per_region = get_locations_per_region(locations)

    regions = [
        create_region(world, player, locations_per_region, location_cache, 'Menu'),
        create_region(world, player, locations_per_region, location_cache, 'Main Caves'),
        create_region(world, player, locations_per_region, location_cache, 'Golden Temple'),
        create_region(world, player, locations_per_region, location_cache, 'Hydro Station'),
        create_region(world, player, locations_per_region, location_cache, 'Inner Hydro Station'),
        create_region(world, player, locations_per_region, location_cache, 'Hydro Nest'),
        create_region(world, player, locations_per_region, location_cache, 'Pre Industrial Complex'),
        create_region(world, player, locations_per_region, location_cache, 'Industrial Complex'),
        create_region(world, player, locations_per_region, location_cache, 'Mining Facility'),
        create_region(world, player, locations_per_region, location_cache, 'Pipes'),
        create_region(world, player, locations_per_region, location_cache, 'The Tower'),
        create_region(world, player, locations_per_region, location_cache, 'Distribution Center'),
        create_region(world, player, locations_per_region, location_cache, 'Deep Caves'),
    ]

    if __debug__:
        throwIfAnyLocationIsNotAssignedToARegion(regions, locations_per_region.keys())

    world.regions += regions

    names: Dict[str, int] = {}
    connect(world, player, names, 'Main Caves', 'Golden Temple')
    connect(world, player, names, 'Main Caves', 'Hydro Station')
    connect(world, player, names, 'Main Caves', 'Pre Industrial Complex')
    connect(world, player, names, 'Main Caves', 'The Tower')
    connect(world, player, names, 'Main Caves', 'Distribution Center')
    connect(world, player, names, 'Main Caves', 'Deep Caves')
    connect(world, player, names, 'Main Caves', 'GFS Thoth',
            lambda state: state.has('Power Bombs', player))
    connect(world, player, names, 'Golden Temple', 'Main Caves')
    connect(world, player, names, 'Golden Temple', 'Pipes',
            lambda state: state.has('Screw Attack', player))
    connect(world, player, names, 'Hydro Station', 'Main Caves')
    connect(world, player, names, 'Hydro Station', 'Inner Hydro Station',
            lambda state: state._AM2R_can_bomb(world, player))
    connect(world, player, names, 'Inner Hydro Station', 'Hydro Station',
            lambda state: state._AM2R_can_bomb(world, player))
    connect(world, player, names, 'Hydro Station', 'The Tower',
            lambda state: state.has('Screw Attack', player))
    connect(world, player, names, 'Hydro Station', 'Hydro Nest',
            lambda state: state._AM2R_can_jump(world, player))
    connect(world, player, names, 'Pre Industrial Complex', 'Main Caves')
    connect(world, player, names, 'Pre Industrial Complex', 'Mining Facility',
            lambda state: state.has('Super Missiles'))
    connect(world, player, names, 'Pre Industrial Complex', 'Industrial Complex',
            lambda state: state.has('Speed Booster'))
    connect(world, player, names, 'Pre Industrial Complex', 'Pipes',
            lambda state: state.has('Screw Attack', player))
    connect(world, player, names, 'Industrial Complex', 'Pre Industrial Complex',
            lambda state: state.has('Speed Booster', player))
    connect(world, player, names, 'Mining Facility', 'Pre Industrial Complex')
    connect(world, player, names, 'The Tower', 'Main Caves')
    connect(world, player, names, 'The Tower', 'Pipes',
            lambda state: state.has('Screw Attack', player))
    connect(world, player, names, 'Distribution Center', 'Main Caves')
    connect(world, player, names, 'Distribution Center', 'Pipes')
    connect(world, player, names, 'Pipes', 'Golden Temple')
    connect(world, player, names, 'Pipes', 'Pre Industrial Complex')
    connect(world, player, names, 'Pipes', 'The Tower')
    connect(world, player, names, 'Pipes', 'Distribution Center')
    connect(world, player, names, 'Deep Caves', 'Main Caves')
    connect(world, player, names, 'GFS Thoth', 'Main Caves')

def throwIfAnyLocationIsNotAssignedToARegion(regions: List[Region], regionNames: Set[str]):
    existingRegions = set()

    for region in regions:
        existingRegions.add(region.name)

    if (regionNames - existingRegions):
        raise Exception(
            "AM2R: the following regions are used in locations: {}, but no such region exists".format(
                regionNames - existingRegions))


def create_location(player: int, location_data: LocationData, region: Region,
                    location_cache: List[Location]) -> Location:
    location = Location(player, location_data.name, location_data.code, region)
    location.access_rule = location_data.rule

    if id is None:
        location.event = True
        location.locked = True

    location_cache.append(location)

    return location


def create_region(world: MultiWorld, player: int, locations_per_region: Dict[str, List[LocationData]],
                  location_cache: List[Location], name: str) -> Region:
    region = Region(name, RegionType.Generic, name, player)
    region.multiworld = world

    if name in locations_per_region:
        for location_data in locations_per_region[name]:
            location = create_location(player, location_data, region, location_cache)
            region.locations.append(location)

    return region


def connect(world: MultiWorld, player: int, used_names: Dict[str, int], source: str, target: str,
            rule: Optional[Callable] = None):
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)

    if target not in used_names:
        used_names[target] = 1
        name = target
    else:
        used_names[target] += 1
        name = target + (' ' * used_names[target])

    connection = Entrance(player, name, sourceRegion)

    if rule:
        connection.access_rule = rule

    sourceRegion.exits.append(connection)
    connection.connect(targetRegion)


def get_locations_per_region(locations: Tuple[LocationData, ...]) -> Dict[str, List[LocationData]]:
    per_region: Dict[str, List[LocationData]] = {}

    for location in locations:
        per_region.setdefault(location.region, []).append(location)

    return per_region
