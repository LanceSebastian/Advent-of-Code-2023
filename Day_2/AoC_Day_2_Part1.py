#Advent of Code
#Day 2: Cube Conundrum
def isLegal(number, colour):
    if colour == "red" and number <= 12:
        return True
    if colour == "green" and number <= 13:
        return True
    if colour == "blue" and number <= 14:
        return True
    return False


def getGameID(line):
    game_id = ""
    for char in line[5::]:
        if char == ':':
            break
        game_id += char
        
    return game_id


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
    with open("F:/Lance's Stuff/GitHub/Advent-of-Code-2023/Day_2/sample.txt") as file:
        for line in file:
            sum += processLine(line)
    return sum


def main():
    print("Hello World")

if __name__ == '__main__':
    main()