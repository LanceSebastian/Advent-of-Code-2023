#Advent of Code
#Day 1: Trebuchet?!

def getNumbers(line):
    numbers = ""
    for character in line:
        if character.isdigit():
            numbers += character
    return numbers

def processLine(line):
    string_numbers = getNumbers(line)
    final_number = string_numbers[0] + string_numbers[-1]
    return int(final_number)

def readFile():
    total = 0
    with open("Puzzle_Input.txt") as file:
        for line in file:
            total += processLine(line)
    return total

def main():
    print(readFile())

if __name__ == '__main__':
    main()