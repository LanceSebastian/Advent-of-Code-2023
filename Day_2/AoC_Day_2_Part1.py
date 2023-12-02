#Advent of Code
#Day 2: Cube Conundrum
import re

def isLegal(number, colour):
    if colour == "red" and int(number) <= 12:
        return True
    if colour == "green" and int(number) <= 13:
        return True
    if colour == "blue" and int(number) <= 14:
        return True
    return False


def getGameID(line):
    game_id = ""
    for char in line[5::]:
        if char == ':':
            break
        game_id += char
        
    return game_id


def getRecords(line):
    startIndex = 0

    for char in line:
        startIndex += 1
        if char == ':':
            break    
    
    line_of_games = line[startIndex:]
    line_of_games = line_of_games.strip('\n')
    game_list = re.split(',|;', line_of_games)
    final_game_list = []

    for cube in game_list:
        data = cube[1::]
        data = data.split(' ')
        final_game_list.append(data)
        

    return final_game_list
        


def processLine(line):
    legal = True
    game_id = getGameID(line)
    game_record = getRecords(line)
    for cube in game_record:
        if not isLegal(cube[0],cube[1]):
            game_id = 0

    return int(game_id)



def readFile():
    sum = 0
    with open("F:/Lance's Stuff/GitHub/Advent-of-Code-2023/Day_2/sample.txt") as file:
        for line in file:
            sum += processLine(line)
    return sum


def main():
    print(readFile())

if __name__ == '__main__':
    main()