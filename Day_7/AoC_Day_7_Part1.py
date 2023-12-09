#Advent of Code
#Day 7: Camel Cards
from collections import Counter

def calculateWinnings(hand, bid):
    rank=0
    winnings = 0
    card_count = Counter(hand)
    ranking = {
        '2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,
        '9':8,'T':9,'J':10,'Q':11,'K':12,'A':13
    }
    order_hand = ''.join(sorted(hand, key=lambda char:ranking[char]))
    temp_array = []
    for card, count in card_count.items():
        temp_array.append(count)
    if len(temp_array) == 2 and temp_array[0] >=2:
        rank = 3
    for count in temp_array:
        if count < 3:
            count -= 1
        rank = max(count, rank)
    print(rank)

    winnings = rank * bid
    return winnings

def main():
    total_winnings = 0
    with open("Day_7/sample.txt") as file:
        sorted_array = rankHands(file)
        for index, play in enumerate(sorted_array, start = 1):
            total_winnings += play[1] * index
            
    print(total_winnings)

if __name__ == '__main__':
    main()