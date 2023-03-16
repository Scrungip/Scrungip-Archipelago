from dataclasses import dataclass, field
from enum import IntFlag
from random import Random
from typing import Iterable, Dict, Protocol, Optional, List, Tuple

from BaseClasses import Region, Entrance
from . import options
from .options import AM2ROptions


class RegionFactory(Protocol):
    def __call__(self, name: str, regions: Iterable[str]) -> Region:
        raise NotImplementedError


class RandomizationFlag(IntFlag):
    NOT_RANDOMIZED = 0b0
    AREA_RANDO = 0b11111
    BOSS_RANDO = 0b11110
    PIPE_RANDO = 0b11100


@dataclass(frozen=True)
class RegionData:
    name: str
    exits: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class ConnectionData:
    name: str
    destination: str
    reverse: Optional[str] = None
    flag: RandomizationFlag = RandomizationFlag.NOT_RANDOMIZED

    def __post_init__(self):
        if self.reverse is None and " to " in self.name:
            origin, destination = self.name.split(" to ")
            super().__setattr__("reverse", f"{destination} to {origin}")


AM2R_regions = [
    RegionData('Menu', ['New Game']),
    RegionData('Main Caves', ['To Alpha', 'Fight Guardian', 'Reach A2', 'Reach Mines', 'Reach A3 Nest',
                              'Reach A4', 'Reach A5', 'Reach A6', 'Reach GFS']),
    RegionData('Guardian', ['Reach A1', 'Reach A1 Nest']),
    RegionData('Golden Temple', ['A1-Pipe Hell Pipe']),
    RegionData('Golden Temple Nest'),
    RegionData('Hydro Station', ['Reach A2 Nest', 'A2-A4 Pipe', 'A2-Lab Pipe', 'Fight Arachnus']),
    RegionData('Hydro Nest'),
    RegionData('Arachnus'),
    RegionData('Mines'),
    RegionData('Industrial Complex Nest', ['Reach A3']),
    RegionData('Pre Industrial Complex', ['To A3 Pipe', 'I find it quite simple', 'Fight Torizo Ascended']),
    RegionData('Torizo Ascended'),
    RegionData('Industrial Complex'),
    RegionData('The Tower', ['Reach Basement', 'Fight Tester']),
    RegionData('Geothermal'),
    RegionData('Tester', ['Leave Tester']),
    RegionData('Distribution Center', ['Reach EMP Win', 'Reach Bottom Hell', 'Reach Top Hell',
                                       'Fight Serris', ]),
    RegionData('Serris', ['Exit Stage Left']),
    RegionData('Pipe Hell', ['Grav Win Pipe', 'BL-BR Pipe', 'TL-TR Pipe']),
    RegionData('Gravity', ['Reach Outside Hell']),
    RegionData('EMP', ['Reach Pipe Hell Lose']),
    RegionData('GFS Thoth' ['Fight Genesis']),
    RegionData('Genesis'),
    RegionData('Deep Caves', ['reach Omega Nest']),
    RegionData('Omega Nest')
]

mandatory_connections = [
    ConnectionData('New Game', 'Main Caves'),
    ConnectionData('To Alpha', 'First Alpha', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Fight Guardian', 'Guardian', flag=RandomizationFlag.BOSS_RANDO_2),
    ConnectionData('Reach A1', 'Golden Temple', flag=RandomizationFlag.BOSS_RANDO_2),
    ConnectionData('Reach A2', 'Hydro Station', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Reach Mines', 'Mines', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Reach A3 Nest', 'Industrial Complex Nest', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Reach GFS', 'GFS Thoth', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Fight Genesis', 'Genesis', flag=RandomizationFlag.BOSS_RANDO_1),
    ConnectionData('Reach A4', 'The Tower', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Reach A5', 'Distribution Center', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Reach A6', 'Deep Caves', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Reach A1 Nest', 'Golden Temple Nest', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('A1-Pipe Hell Pipe', 'Pipe Hell', flag=RandomizationFlag.PIPE_RANDO),
    ConnectionData('Reach A2 Nest', 'Hydro Station Nest', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('A2-A4 Pipe', 'The Tower', flag=RandomizationFlag.PIPE_RANDO),
    ConnectionData('A2-Lab Pipe', 'Omega Nest', flag=RandomizationFlag.PIPE_RANDO),
    ConnectionData('Fight Arachnus', 'Arachnus', flag=RandomizationFlag.BOSS_RANDO_1),
    ConnectionData('Reach A3', 'Pre Industrial Complex', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('I find it quite simple', 'Industrial Complex', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Fight Torizo Ascended', 'Torizo Ascended', flag=RandomizationFlag.BOSS_RANDO_1),
    ConnectionData('Reach Basement', 'Geothermal', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Fight Tester', 'Tester', flag=RandomizationFlag.BOSS_RANDO_2),
    ConnectionData('Leave Tester', 'The Tower', flag=RandomizationFlag.BOSS_RANDO_2),
    ConnectionData('Reach EMP Win', 'EMP', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Reach Pipe Hell Lose', 'Pipe Hell', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Reach Bottom Hell', 'Pipe Hell', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Reach Top Hell', 'Pipe Hell', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Fight Serris', 'Serris', flag=RandomizationFlag.BOSS_RANDO_2),
    ConnectionData('Exit Stage Left', 'Distribution Center', flag=RandomizationFlag.BOSS_RANDO_2),
    ConnectionData('Grav Win Pipe', 'Gravity', flag=RandomizationFlag.PIPE_RANDO),
    ConnectionData('BL-BR Pipe', 'Pipe Hell', flag=RandomizationFlag.PIPE_RANDO),
    ConnectionData('TL-TR Pipe', 'Pipe Hell', flag=RandomizationFlag.PIPE_RANDO),
    ConnectionData('Reach Outside Hell', 'Pipe Hell', flag=RandomizationFlag.AREA_RANDO),
    ConnectionData('Reach Omega Nest', 'Omega Nest', flag=RandomizationFlag.AREA_RANDO)
]


#  def create_regions(region_factory: RegionFactory, random: Random, world_options: AM2ROptions) -> Tuple[Iterable[Region], Dict[str, str]]:
    #  regions: Dict[str: Region] = {region.name: region_factory(region.name, region.exits) for region in AM2R_regions}
    #  entrances: Dict[str: Entrance] = {entrance.name: entrance
                                      #  for region in regions.values()
                                      #  for entrance in region.exits}

    #  connections, randomized_data = randomize_connections(random, world_options)

    #  for connection in connections:
        #  if connection.name not in entrances:
            #  continue
        #  entrances[connection.name].connect(regions[connection.destination])

    #  return regions.values(), randomized_data


#  def randomize_connections(random: Random, world_options: AM2ROptions) -> Tuple[List[ConnectionData], Dict[str, str]]:  # todo this section
    #  connections_to_randomize = []
    #  if world_options[options.EntranceRandomization] == options.AreaRando.option_area:
        #  connections_to_randomize = [connection for connection in mandatory_connections if RandomizationFlag.AREA_RANDO in connection.flag]
    #  elif world_options[options.EntranceRandomization] == options.AreaRando.option_boss:
        #  connections_to_randomize = [connection for connection in mandatory_connections if RandomizationFlag.BOSS_RANDO in connection.flag]
    #  random.shuffle(connections_to_randomize)

    #  destination_pool = list(connections_to_randomize)
    #  random.shuffle(destination_pool)

    #  randomized_connections = []
    #  randomized_data = {}
    #  for connection in connections_to_randomize:
        #  destination = destination_pool.pop()
        #  randomized_connections.append(ConnectionData(connection.name, destination.destination, destination.reverse))
        #  randomized_data[connection.name] = destination.name
        #  randomized_data[destination.reverse] = connection.reverse

    #  return mandatory_connections, randomized_data
