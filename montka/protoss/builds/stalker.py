from sc2.data import Race
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId
from sharpy.plans import BuildOrder, SequentialList
from sharpy.plans.acts import *
from sharpy.plans.acts.protoss import *
from sharpy.plans.require import *

from montka.protoss.build import Build
from montka.protoss.common import protoss_tactics


def _plan() -> BuildOrder:
    return BuildOrder(
        # Sequential opener: Pylon → Gateway → Natural Nexus → Gas 1 → Cyber → Gas 2.
        SequentialList(
            ActUnit(UnitTypeId.PROBE, UnitTypeId.NEXUS, 14),
            GridBuilding(UnitTypeId.PYLON, 1),
            ActUnit(UnitTypeId.PROBE, UnitTypeId.NEXUS, 16),
            GridBuilding(UnitTypeId.GATEWAY, 1),
            ActUnit(UnitTypeId.PROBE, UnitTypeId.NEXUS, 18),
            Expand(2),
            BuildGas(1),
            GridBuilding(UnitTypeId.CYBERNETICSCORE, 1),
            BuildGas(2),
            GridBuilding(UnitTypeId.PYLON, 2),
            BuildOrder(
                # AutoPylon automatically places pylons to prevent supply blocks.
                AutoPylon(),
                # Warp Gate converts Gateways for instant warp-ins at any pylon.
                Tech(UpgradeId.WARPGATERESEARCH),
                [ProtossUnit(UnitTypeId.STALKER, 100)],
                # 7 gates provide enough warp-in cycles for sustained stalker production.
                [GridBuilding(UnitTypeId.GATEWAY, 8)],
            ),
        ),
        protoss_tactics(),
    )


build = Build(
    name="stalker",
    fn=_plan,
    weight=3,
    good_against=[Race.Terran, Race.Zerg],
    tags=["bio", "gateway"],
)
