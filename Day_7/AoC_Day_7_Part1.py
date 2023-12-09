#Advent of Code
#Day 7: Camel Cards
from collections import Counter

    ranking = {
        '2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,
        '9':8,'T':9,'J':10,'Q':11,'K':12,'A':13
    }
def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = card_comparison(array[len(array) // 2][0])

    left = [x for x in array if card_comparison(x[0]) < pivot]
    middle = [x for x in array if card_comparison(x[0]) == pivot]
    right = [x for x in array if card_comparison(x[0]) > pivot]

    left_sorted = quicksort(left)
    right_sorted = quicksort(right)

    sorted_array = left_sorted + middle + right_sorted
    return sorted_array

def getType(hand):
    card_count = Counter(hand)
    temp_array = [count for _,count in card_count.items()]

    size = len(temp_array)
    if size == 1:
        return 6 
    if size == 2:
        if temp_array.count(4):
            return 5
        return 4
    if temp_array.count(3):
        return 3
    if temp_array.count(2) == 2:
        return 2
    if temp_array.count(2) == 1:
        return 1
    return 0

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