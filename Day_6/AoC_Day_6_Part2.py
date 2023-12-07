#Advent of Code
#Day 6: Wait For It
import re
from functools import reduce
import operator

def calculateRecordBeat(time, distance):
    number_of_wins = 0
    time = int(time)
    distance = int(distance)
    for wind_up in range(time):
        distance_travelled = (time - wind_up) * wind_up
        number_of_wins += 1 if distance_travelled > distance else 0
    return number_of_wins

def main():
    output = []
    with open("Day_6/Puzzle_input.txt") as file:
        lines = file.read().splitlines()
        time, distance = "".join(re.findall(r"\d+", lines[0])), "".join(re.findall(r"\d+", lines[1]))
        output.append(calculateRecordBeat(time, distance))
    
        
    print(reduce(operator.mul, output, 1))

if __name__ == '__main__':
    main()