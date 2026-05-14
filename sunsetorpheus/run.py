from ladder import run_ladder_game
from sunsetorpheus.sunsetorpheus import run

bot = run()

def main():
    print("Starting ladder game...")
    result, opponentid = run_ladder_game(bot)
    print(result, " against opponent ", opponentid)

if __name__ == '__main__':
    main()
