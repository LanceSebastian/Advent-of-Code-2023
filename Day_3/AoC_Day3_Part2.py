#Advent of Code
#Day 3: Gear Ratios
import re
import linecache

def isPartNumber(neighbouring_lines, number_index, number_length):
    surrounding_characters = []
    final_index = len(neighbouring_lines[1])-1
    end_index = min(number_index+number_length+1,final_index)
    search_index = max(number_index-1,0)
    if neighbouring_lines[0]:
        surrounding_characters += neighbouring_lines[0][search_index:end_index]
    if neighbouring_lines[1]:
        surrounding_characters += neighbouring_lines[1][search_index:end_index]
    if neighbouring_lines[2]:
        surrounding_characters += neighbouring_lines[2][search_index:end_index]
    
    surrounding = ' '.join(surrounding_characters)

    special = set("!@#$%^&*()_+[]:;<>,?~/-=")
    return any(char in special for char in surrounding)

def findPartNumbers(line,prev_line, next_line):
    output = 0
    number = ""
    start_index = 0
    lines = [prev_line,line,next_line]
    for index, char in enumerate(line):
        number_length = len(number)
        if char.isdigit():
            number += char
            start_index = index if number_length <= 0 else start_index

        if not char.isdigit() and number_length > 0:
            output += int(number) if isPartNumber(lines, start_index, number_length) else 0
            number = ""

    return output




def findRatios(lines, index):
    start_index = index-1
    end_index = index+2

    numbers_found = 0
    first_part=""
    second_part="0"

    surrounding_numbers = []
    for line in lines:
        surrounding_numbers.append(line[start_index:end_index])
    
    print(surrounding_numbers)


def findGears(line, prev_line, next_line):
    lines = [prev_line, line, next_line]

    for index, char in enumerate(line):
        if char == '*':
            findRatios(lines, index)
    
    


def readFile():
    sum = 0
    previous_line = []
    line_index = 0
    next_line = []
    with open("F:/Lance's Stuff/GitHub/Advent-of-Code-2023/Day_3/sample.txt") as file:
        for index, line in enumerate(file, start = 1):
            next_line = linecache.getline(file.name, index+1)
            findGears(line,previous_line, next_line)
            previous_line = line
    return sum

def main():
    print(readFile())

if __name__ == '__main__':
    main()