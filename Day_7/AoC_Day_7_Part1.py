#Advent of Code
#Day 7: Camel Cards
from collections import Counter

    ranking = {
        '2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,
        '9':8,'T':9,'J':10,'Q':11,'K':12,'A':13
    }

def main():
    total_winnings = 0
    with open("Day_7/sample.txt") as file:
        sorted_array = rankHands(file)
        for index, play in enumerate(sorted_array, start = 1):
            total_winnings += play[1] * index
            
    print(total_winnings)

if __name__ == '__main__':
    main()