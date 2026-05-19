---
name: SC2 Bots project overview
description: Core architecture, bot identities, framework, and deployment for the sc2-bots project
type: project
originSessionId: e0f99c8f-aaea-4a77-8703-5422e74bfebd
---
Two Protoss StarCraft II ladder bots built on **ares-sc2** (AresBot base class) and **python-sc2 (burnysc2)**.

## Bots

- **Mont'ka** (`montka/`) — fast/aggressive. Low base count, early attack wave, tempo-focused. Simpler plan: no worker defense, no Blink, no micro modules.
- **Kau'yon** (`kauyon/`) — slow/macro. Expands hard, full upgrade ladder, commits to fight only at critical mass. Has Blink micro, worker defense pull, richer config knobs.

## Framework

- `AresBot` from `ares-sc2` is the base class.
- Macro uses ares behaviors: `MacroPlan`, `ExpansionController`, `BuildWorkers`, `AutoSupply`, `BuildStructure`, `SpawnController`, `UpgradeController`, `GasBuildingController`, `Mining`.
- Entry point per bot: `<bot>/run.py` and `<bot>/<bot>.py` (the `Bot` class).
- `run_custom.py` at root for local play (pick map, difficulty, bot).

## Kau'yon Protoss — detailed layout (primary focus)

```
kauyon/protoss/
  plan.py        <- game loop: MacroPlan waterfall + chrono, micro, worker defense, attack state machine
  common.py      <- all default constants (PROBE_MAX, ATTACK_SUPPLY, EXPAND_AT_HARVESTERS, etc.)
  build.py       <- Build dataclass (name, fn, weight, good_against, tags)
  builds/
    __init__.py  <- BUILDS list (currently: [stalker])
    stalker.py   <- pure Stalker build: full weapon/armor upgrades + Blink; good_against Terran/Zerg
    _example.py  <- annotated reference template (NOT in BUILDS, weight=0)
  micro/
    __init__.py  <- MICRO list (currently: [StalkerMicro()])
    base.py      <- UnitMicro Protocol (unit_types + run())
    stalker.py   <- StalkerMicro: Blink retreat when HP+shield < threshold AND position unsafe
```

### Adding new builds
Copy `_example.py`, set only keys that differ from defaults, add to `builds/__init__.py` BUILDS list.

### Adding new micro modules
Create a class satisfying the `UnitMicro` protocol, append instance to `micro/__init__.py` MICRO list.

## Build system / Deployment

- `package_bot.py` at root zips either bot (flip `BOT` constant).
- Upload zip manually to [AI Arena](https://aiarena.net).
