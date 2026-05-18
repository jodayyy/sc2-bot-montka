from sc2.data import Race

from kauyon.protoss.builds import BUILDS
from kauyon.protoss.macro import Macro
from kauyon.protoss.production import Production
from kauyon.protoss.combat import Combat
from kauyon.protoss.defense import Defense


class ProtossPlan:
    def __init__(self, ai, enemy_race: Race):
        self.ai = ai
        self.enemy_race = enemy_race
        self._config: dict = {}
        self._macro: Macro = None
        self._production: Production = None
        self._combat: Combat = None
        self._defense: Defense = None

    async def on_start(self) -> None:
        self._macro = Macro(self.ai, self._config)
        self._production = Production(self.ai, self._config)
        self._combat = Combat(self.ai, self._config)
        self._defense = Defense(self.ai, self._config)

    async def on_step(self, iteration: int) -> None:
        self._macro.on_step()
        self._production.on_step()
        self._combat.on_step()
        self._defense.on_step()
