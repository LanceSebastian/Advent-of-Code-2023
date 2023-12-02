#Advent of Code
#Day 1: Trebuchet?! (part 2)

def isNumber(string):
    d = { '0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five',
          '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine'}
    for key, value in d.items():
        if value in string:
            return key
    return False

def getFirstDigit(line):
    if line[0].isdigit():
        return line[0]
    
    string = ""
    for char in line:
        if char.isdigit():
            return char
        
        string += char
        if len(string)>2 and isNumber(string):
            return isNumber(string)

def getLastDigit(line):
    if line[-1].isdigit():
        return line[-1]
    
    string = ""
    for char in line[::-1]:
        if char.isdigit():
            return char
        
        string = char + string
        if len(string)>2 and isNumber(string):
            return isNumber(string)


def processLine(line):
    final_number =  getFirstDigit(line) + getLastDigit(line)
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