#Advent of Code
#Day 4: Scratchcards

def simulateScratchcards(filename, number_of_wins, current_index):
    


def calculateWinnings(card):
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

    return number_of_wins

def main():
    sum = 0
    with open("Day_4/Puzzle_input.txt") as file:
        for card in file:
            sum += calculateWinnings(card)
    print(sum)

if __name__ == '__main__':
    main()    main()
