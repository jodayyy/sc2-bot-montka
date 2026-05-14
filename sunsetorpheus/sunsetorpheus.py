import random
from sc2 import Race
from sharpy.knowledges import KnowledgeBot
from sharpy.plans import BuildOrder


CHOSEN_RACE = random.choice([Race.Terran, Race.Zerg, Race.Protoss])


class SunsetOrpheus(KnowledgeBot):
    def __init__(self):
        super().__init__("SunsetOrpheus")
        self.race = CHOSEN_RACE

    async def create_plan(self) -> BuildOrder:
        if self.knowledge.my_race == Race.Terran:
            from sunsetorpheus.terran.plan import terran_plan
            return terran_plan()
        elif self.knowledge.my_race == Race.Zerg:
            from sunsetorpheus.zerg.plan import zerg_plan
            return zerg_plan()
        else:
            from sunsetorpheus.protoss.plan import protoss_plan
            return protoss_plan()


def run():
    from sc2.player import Bot
    return Bot(CHOSEN_RACE, SunsetOrpheus())
