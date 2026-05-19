---
name: Build config override pattern
description: How build files override default constants from common.py via the config dict
type: project
originSessionId: 7558c67f-9622-468f-801f-9d9342dd4dc1
---
Defaults live in `common.py`. Build files can override any of them by passing values into the config dict. All modules (macro, production, combat, defense) read from config first, falling back to the common.py default if the key is absent.

**Why:** Different builds may need different values (e.g. a rush build wants fewer probes, an aggressive build attacks at lower supply). The build file is the single place to tune a strategy without touching shared defaults.

**How to apply:** When implementing any configurable value (e.g. PROBE_MAX, ATTACK_SUPPLY), always read it as `self.config.get("probe_max", PROBE_MAX)` rather than using the constant directly. Document overridable keys in `builds/_example.py` as a reference for anyone adding a new build.
