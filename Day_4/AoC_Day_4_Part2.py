#Advent of Code
#Day 4: Scratchcards

def calculateCardsGenerated(win_array):
    card_generation_array = []

    for card in win_array[::-1]:
        total_cards = 0
        new_cards = []
        
        for index, cards_generated in enumerate(card_generation_array[::-1]):
            if index >= card : break
            new_cards.append(cards_generated)
        
        total_cards = 1 + sum(new_cards)
        card_generation_array.append(total_cards)

    return card_generation_array


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
    total_cards = 0
    win_array = []
    with open("Day_4/Puzzle_input.txt") as file:
        for index, card in enumerate(file, start = 1):
            win_array.append(calculateWinnings(card))

        total_cards = sum(calculateCardsGenerated(win_array))

    print(total_cards)


if __name__ == '__main__':
    main()