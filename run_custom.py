"""
Local test runner for Montka.
Launches a game vs the built-in AI using python-sc2's sc2.main.run_game.
"""
from sc2 import maps
from sc2.data import Difficulty, Race
from sc2.main import run_game
from sc2.player import Bot, Computer

from montka.montka import Montka

# --- Options ---
BOT_RACE = Race.Protoss          # Race.Protoss | Race.Terran | Race.Zerg | Race.Random
OPPONENT_RACE = Race.Random      # Race.Protoss | Race.Terran | Race.Zerg | Race.Random
DIFFICULTY = Difficulty.VeryHard   # Easy | Medium | MediumHard | Hard | Harder | VeryHard | CheatVision | CheatMoney | CheatInsane
MAP = "PylonAIE_v4"                 # Any installed map name
REALTIME = False                 # True = watch at normal speed in SC2 window
# ---------------


def main():
    run_game(
        maps.get(MAP),
        [
            Bot(BOT_RACE, Montka()),
            Computer(OPPONENT_RACE, DIFFICULTY),
        ],
        realtime=REALTIME,
    )


if __name__ == "__main__":
    main()
