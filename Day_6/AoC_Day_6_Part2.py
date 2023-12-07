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
        time_array, distance_array = re.findall(r"\d+", lines[0]), re.findall(r"\d+", lines[1])
        for index, time in enumerate(time_array):
            distance = distance_array[index]
            output.append(calculateRecordBeat(time, distance))
    
        
    print(reduce(operator.mul, output, 1))

if __name__ == '__main__':
    main()