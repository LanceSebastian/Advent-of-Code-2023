#Advent of Code
#Day 6: Wait For It
import re
from functools import reduce
import operator

def calculateRecordBeat(time, distance):
    output = None
    #loop through possible time:distance ratios
    return output

def main():
    output = []
    with open("Day_6/sample.txt") as file:
        lines = file.read().splitlines()
        time_array, distance_array = re.findall(r"\d+", lines[0]), re.findall(r"\d+", lines[1])
        for index, time in enumerate(time_array):
            distance = distance_array[index]
            output += calculateRecordBeat(time, distance)
    
        
    print(reduce(operator.mul, output, 1))

if __name__ == '__main__':
    main()