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
    red_number = 0
    blue_number = 0
    green_number = 0
    
    game_record = getRecords(line)
    for cube in game_record:
        name = cube[1]
        number = int(cube[0])

        if name == "blue" and number > blue_number:
            blue_number = number
        if name == "red" and number > red_number:
            red_number = number
        if name == "green" and number > green_number:
            green_number = number

    output = blue_number * red_number * green_number
    return output


def readFile():
    sum = 0
    with open("F:/Lance's Stuff/GitHub/Advent-of-Code-2023/Day_2/Puzzle_input.txt") as file:
        for line in file:
            sum += processLine(line)
    return sum


def main():
    print(readFile())

if __name__ == '__main__':
    main()