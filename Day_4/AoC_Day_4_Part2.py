#Advent of Code
#Day 4: Scratchcards

def calculateWinnings(card):
    output = 1
    number_of_wins = 0
    win_numbers = []
    own_numbers = []
    numbers = []

    numbers = card.split(':')[1]
    win_numbers = list(filter(None,numbers.split('|')[0].split(' ')))
    own_numbers = list(filter(None,numbers.split('|')[1].strip('\n').split(' ')))

    for number in win_numbers:
        if number in own_numbers:
            number_of_wins += 1

    if number_of_wins == 0:
        return 0
    
    for index in range(number_of_wins-1):
        output *= 2

    return output

def main():
    sum = 0
    with open("Day_4/Puzzle_input.txt") as file:
        for card in file:
            sum += calculateWinnings(card)
    print(sum)

if __name__ == '__main__':
    main()