#Advent of Code
#Day 2: Cube Conundrum
def processGame(game):
    for cube in game:
        if not isLegal(cube[0],cube[1]):
            return False


def processLine(line):
    legal = True
    game_id = getGameID(line)
    game_record = getRecords(line)
    for game in game_record:
        legal = processGame(game)
        if not legal:
            return 0

    return game_id



def readFile():
    sum = 0
    with open("sample.txt") as file:
        for line in file:
            sum += processLine(line)
    return sum


def main():
    print("Hello World")

if __name__ == '__main__':
    main()