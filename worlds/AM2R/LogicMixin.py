from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin
#from .Options import is_option_enabled


class AM2RLogic(LogicMixin):

    def _AM2R_can_bomb(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({'Bombs', 'Power Bombs'}, player)

    def _AM2R_can_jump(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({'Hi Jump', 'Space Jump', 'Bombs'}, player)

    def _AM2R_can_fly(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({'Bombs', 'Space Jump'}, player)
    def _AM2R_can_spider(self, world: MultiWorld, player: int) -> bool:
        return self.has('Spiderball', player) or self._AM2R_can_fly(world, player)

    def _AM2R_can_schmove(self, world: MultiWorld, player: int) -> bool:
        return self._AM2R_can_spider(world, player) or self.has('Hi Jump', player)

    def _AM2R_has_ballspark(self, world: MultiWorld, player: int) -> bool:
        return self.has_all({'Speed Booster', 'Spring Ball'}, player)


    def _AM2R_can_down(self,world: MultiWorld, player: int) -> bool:
        return self.has('Speed Booster', player) and self._AM2R_can_bomb(world, player) and self.has('Super Missiles')
