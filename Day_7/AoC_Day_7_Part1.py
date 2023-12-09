#Advent of Code
#Day 7: Camel Cards
from collections import Counter

    ranking = {
        '2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,
        '9':8,'T':9,'J':10,'Q':11,'K':12,'A':13
    }
def rankHands(file):
    high, pair, two_pairs, three_kinds, house, four_kinds, five_kinds = [],[],[],[],[],[],[]
    sorted_array = []
    hand_type_lists = {
        0:high,
        1:pair,
        2:two_pairs,
        3:three_kinds,
        4:house,
        5:four_kinds,
        6:five_kinds,  
    }

    for line in file:
        hand = line.split()[0]
        bid = int(line.split()[1])
        play = [hand, bid]
        hand_type = getType(hand)
        if hand_type in hand_type_lists:
            hand_type_lists[hand_type].append(play)

    for _,list in hand_type_lists.items():
        sorted_array += quicksort(list)

    return sorted_array

def main():
    total_winnings = 0
    with open("Day_7/sample.txt") as file:
        sorted_array = rankHands(file)
        for index, play in enumerate(sorted_array, start = 1):
            total_winnings += play[1] * index
            
    print(total_winnings)

if __name__ == '__main__':
    main()