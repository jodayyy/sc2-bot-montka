# SC2 Bots

Two Protoss StarCraft II ladder bots built on [ares-sc2](https://github.com/AresSC2/ares-sc2) and [python-sc2 (burnysc2)](https://github.com/BurnySc2/python-sc2). Same framework, same race, very different play styles.

## The bots

### Montka — fast and aggressive
Tight tech path, low base count, hits the opponent before they finish setting up. Built around an early attack wave and tempo. If the first push doesn't break, things get spicy.

### Kauyon — slow and macro-heavy
Plays the long game. Expands hard, builds a deeper economy, takes the full upgrade ladder, and only commits to a fight once the army is well past critical mass. Patient and grindy.

Both are Protoss-only — leaning on Stalker / Gateway play. The Terran and Zerg scaffolding is still in the repo (commented out) in case they get reactivated later.

---

## Run locally

```
python -m venv venv
venv\Scripts\activate
pip install -e "git+https://github.com/AresSC2/ares-sc2.git#egg=ares-sc2"
python run_custom.py
```

Edit `run_custom.py` to pick map, difficulty, and which bot to run.

---

## Ladder

Each bot ships as its own zip to [AI Arena](https://aiarena.net). `package_bot.py` builds either one — flip the `BOT` constant at the top. GitHub Actions builds the Linux zip on every push to `master`; download from the Actions artifact and upload manually on aiarena.net.
