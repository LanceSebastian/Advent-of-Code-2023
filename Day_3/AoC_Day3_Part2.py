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




def numbersFound(surrounding):
    output = 0
    if surrounding[1].isdigit():
        output += 1
    if surrounding[7].isdigit():
        output += 1
    if surrounding[4].isdigit():
        output += 1
    if surrounding[6].isdigit():
        output += 1
    
    if output == 2:
        return output
        
    digits_found = 0
    for char in surrounding[0:3]:
        if char.isdigit():
            digits_found += 1
    if digits_found == 2 and not surrounding[1].isdigit():
        return 2

    digits_found = 0
    for char in surrounding[6:9]:
        if char.isdigit():
            digits_found += 1
    if digits_found == 2 and not surrounding[7].isdigit():
        return 2
    
    return output


def findRatios(lines, index):
    start_index = index-1
    end_index = index+2

    first_part=""
    second_part=""

    surrounding_numbers = []
    for line in lines:
        surrounding_numbers += line[start_index:end_index]
    
    if numbersFound(surrounding_numbers) < 2:
        return
    
    #look at first layer
        #slice the numbers out
    #look at second
        #slice the numbers out
    #look at third
        #slice the numbers out
    #Get numbers



def findGears(line, prev_line, next_line):
    lines = [prev_line, line, next_line]
    output=0

    for index, char in enumerate(line):
        if char == '*':
            output = findRatios(lines, index)
    return output

def readFile():
    sum = 0
    previous_line = []
    next_line = []
    with open("F:/Lance's Stuff/GitHub/Advent-of-Code-2023/Day_3/sample.txt") as file:
        for index, line in enumerate(file, start = 1):
            next_line = linecache.getline(file.name, index+1)
            sum += findGears(line,previous_line, next_line)
            previous_line = line
    return sum

def main():
    print(readFile())

if __name__ == '__main__':
    main()