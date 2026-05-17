# ---------------------------------------------------------------------------
# Default macro parameters — override these in individual build configs.
# ---------------------------------------------------------------------------

# Worker cap
PROBE_MAX: int = 75

# Maximum number of bases (hard ceiling — overridden per-build as needed).
# In practice the saturation logic drives expansion; this is a safety cap.
EXPAND_MAX: int = 99

# Supply threshold for the first all-in attack wave.
ATTACK_SUPPLY: int = 100

# Gateway scaling: bases_committed * GATEWAY_PER_BASE, capped at GATEWAY_MAX.
GATEWAY_PER_BASE: int = 4
GATEWAY_MAX: int = 16

# Chrono boost energy threshold — only use chrono when Nexus has this much energy.
CHRONO_ENERGY_THRESHOLD: float = 50.0
