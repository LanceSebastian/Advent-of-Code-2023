#Advent of Code
#Day 2: Cube Conundrum
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