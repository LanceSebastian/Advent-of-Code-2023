#Advent of Code
#Day 7: Camel Cards

def main():
    total_winnings = 0
    with open("Day_7/sample.txt") as file:
        for line in file:
            hand = line.split()[0]
            bid = int(line.split()[1])
            print(hand, bid)
            
    print(total_winnings)

if __name__ == '__main__':
    main()