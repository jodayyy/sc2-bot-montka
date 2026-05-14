from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId
from sharpy.plans import BuildOrder, Step, SequentialList, StepBuildGas
from sharpy.plans.acts import *
from sharpy.plans.acts.terran import *
from sharpy.plans.require import *
from sharpy.plans.tactics import *
from sharpy.plans.tactics.terran import *


def terran_plan() -> BuildOrder:
    opener = [
        Step(Supply(13), GridBuilding(UnitTypeId.SUPPLYDEPOT, 1, priority=True)),
        GridBuilding(UnitTypeId.BARRACKS, 1, priority=True),
        StepBuildGas(1, Supply(15)),
        TerranUnit(UnitTypeId.REAPER, 1, only_once=True, priority=True),
        Expand(2),
        GridBuilding(UnitTypeId.SUPPLYDEPOT, 2, priority=True),
        BuildAddon(UnitTypeId.BARRACKSREACTOR, UnitTypeId.BARRACKS, 1),
        GridBuilding(UnitTypeId.FACTORY, 1),
        BuildAddon(UnitTypeId.FACTORYTECHLAB, UnitTypeId.FACTORY, 1),
        AutoDepot(),
    ]

    buildings = [
        Step(None, GridBuilding(UnitTypeId.BARRACKS, 2)),
        BuildGas(2),
        Step(None, BuildAddon(UnitTypeId.BARRACKSTECHLAB, UnitTypeId.BARRACKS, 1)),
        Step(None, GridBuilding(UnitTypeId.STARPORT, 1)),
        Step(None, GridBuilding(UnitTypeId.BARRACKS, 3)),
        Step(None, BuildAddon(UnitTypeId.BARRACKSTECHLAB, UnitTypeId.BARRACKS, 2)),
        Step(Supply(40), Expand(3)),
        Step(None, GridBuilding(UnitTypeId.BARRACKS, 5)),
        Step(None, BuildAddon(UnitTypeId.BARRACKSREACTOR, UnitTypeId.BARRACKS, 3)),
        Step(None, BuildAddon(UnitTypeId.STARPORTREACTOR, UnitTypeId.STARPORT, 1)),
        BuildGas(4),
    ]

    tech = [
        Step(None, Tech(UpgradeId.PUNISHERGRENADES)),
        Step(None, Tech(UpgradeId.STIMPACK)),
        Step(None, Tech(UpgradeId.SHIELDWALL)),
    ]

    scv = [
        Step(None, MorphOrbitals(), skip_until=UnitReady(UnitTypeId.BARRACKS, 1)),
        Step(None, ActUnit(UnitTypeId.SCV, UnitTypeId.COMMANDCENTER, 22),
             skip=UnitExists(UnitTypeId.COMMANDCENTER, 2)),
        Step(None, ActUnit(UnitTypeId.SCV, UnitTypeId.COMMANDCENTER, 44)),
    ]

    air = [
        Step(UnitReady(UnitTypeId.STARPORT, 1), TerranUnit(UnitTypeId.MEDIVAC, 2, priority=True)),
        Step(UnitReady(UnitTypeId.STARPORT, 1), TerranUnit(UnitTypeId.MEDIVAC, 4, priority=True)),
    ]

    marines = [
        Step(UnitExists(UnitTypeId.REAPER, 1, include_killed=True), TerranUnit(UnitTypeId.MARINE, 2)),
        BuildOrder([
            TerranUnit(UnitTypeId.MARAUDER, 20, priority=True),
            TerranUnit(UnitTypeId.MARINE, 20),
            Step(Minerals(250), TerranUnit(UnitTypeId.MARINE, 100)),
        ]),
    ]

    tactics = [
        MineOpenBlockedBase(),
        PlanCancelBuilding(),
        LowerDepots(),
        PlanZoneDefense(),
        Step(None, CallMule(50), skip=Time(5 * 60)),
        Step(None, CallMule(100), skip_until=Time(5 * 60)),
        DistributeWorkers(),
        Step(None, SpeedMining(), lambda ai: ai.client.game_step > 5),
        ManTheBunkers(),
        Repair(),
        ContinueBuilding(),
        PlanZoneGatherTerran(),
        PlanZoneAttack(26),
        PlanFinishEnemy(),
    ]

    return BuildOrder([scv, opener, buildings, tech, air, marines, tactics])
