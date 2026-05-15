# SC2 Bot — Sharpy Starter

A StarCraft II bot built on [sharpy-sc2](https://github.com/DrInfy/sharpy-sc2/wiki) and [python-sc2](https://github.com/BurnySc2/python-sc2).

---

## Getting started

The steps below will get you set up locally with your own bot name.

### 1. Prerequisites

- [Python 3.11.9](https://www.python.org/downloads/release/python-3119/)
- StarCraft II installed locally (for testing)
- Git

### 2. Clone the repo

```
git clone --recursive https://github.com/sunsetorpheus/sc2-bot-montka.git <BotName>
cd <BotName>
```


### 3. Rename the bot (do this before anything else)

See the [Rename the bot](#rename-the-bot) section below. Do this now before you start coding so all your commits use your own bot name.

### 4. Create and activate a virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 5. Install dependencies

```
pip install -r requirements.txt
```

---

## Run the bot locally (vs built-in AI)

```
python run_custom.py -m EverDreamLE -p1 BotName -p2 ai
```

Replace `BotName` with whatever name you registered in `run_custom.py`, and the map name with any SC2 ladder map.

Replays and logs will be saved to the `games/` folder.

---

## Rename the bot

To rename the bot to your own name, make the following changes:

### 1. Rename the bot folder

Rename the `montka/` folder to your bot name (lowercase, no spaces), e.g. `BotName/`.

### 2. Update the bot class (`montka/montka.py` → `BotName/BotName.py`)

Change the class name and the display name passed to `KnowledgeBot`:

```python
class BotName(KnowledgeBot):
    def __init__(self):
        super().__init__("BotName")  # This is the in-game display name
```

### 3. Update `run_custom.py`

Find the import and registration lines for montka and update them:

```python
# Change this import
from montka.montka import Montka

# To
from BotName.BotName import BotName
```

And update the bot registration:

```python
# Change
definitions.add("montka", "Mon'tka", Race.Random, lambda params: Bot(CHOSEN_RACE, Montka()))

# To
definitions.add("BotName", "BotName", Race.Random, lambda params: Bot(CHOSEN_RACE, BotName()))
```

### 4. Update `montka/run.py` → `BotName/run.py`

```python
# Change
from montka.montka import Montka

# To
from BotName.BotName import BotName
```

And update the bot instantiation:

```python
bot = Bot(Race.Random, BotName())
```

### 5. Update `ladder_zip.py`

Find the `montka_zip` entry and update the name, folder, and run.py path:

```python
montka_zip = LadderZip(
    "BotName", "Random", [("BotName", None), (os.path.join("BotName", "run.py"), "run.py")], common
)
```

Also update the `zip_types` dict key:

```python
zip_types = {
    ...
    "BotName": montka_zip,
    ...
}
```

---

## Publish for ladder

Package the bot into a ladder-ready zip:

```
python ladder_zip.py -n BotName
```

The zip will be placed in the `publish/` folder. Upload it to [AI Arena](https://aiarena.net) or your ladder of choice.

---

## Project structure

```
montka/              # Bot code (rename this to your bot name)
  montka.py          # Main bot class
  run.py             # Ladder entry point
  protoss/           # Protoss builds and tactics
  terran/            # Terran builds and tactics
  zerg/              # Zerg builds and tactics
sharpy-sc2/          # Framework (git submodule, do not edit)
run_custom.py        # Local testing entry point
ladder_zip.py        # Packaging script for ladder submission
config.ini           # Bot settings (ladder)
config-local.ini     # Bot settings (local testing, debug enabled)
requirements.txt     # Python dependencies
```

---

## Documentation

- [Sharpy-sc2 wiki](https://github.com/DrInfy/sharpy-sc2/wiki)
