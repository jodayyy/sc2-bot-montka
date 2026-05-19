# Memory Index

- [SC2 Bots project overview](project_sc2bots.md) — two Protoss ladder bots (Mont'ka aggressive, Kau'yon macro), ares-sc2 framework, structure, deployment via AI Arena
- [Comments for maintainability](feedback_comments.md) — always add inline comments when implementing features so any developer can maintain the code
- [Research before implementing](feedback_research.md) — research most efficient approach independently first; use Mont'ka only as ares API reference, not strategy reference
- [Build config override pattern](project_build_overrides.md) — defaults in common.py, build files override via config dict, modules always read config first with fallback
