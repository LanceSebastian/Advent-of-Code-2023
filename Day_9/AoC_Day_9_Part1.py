#Advent of Code
#Mirage Maintenance

def difference(sequence):
    finished = False
    i = 0
    new_sequence = []
    while not finished:
        if i+1 >= len(sequence):
            return new_sequence
        new_sequence.append(sequence[i+1] - sequence[i])
        i += 1


def extrapolate(sequence):
    difference_sequence = difference(sequence)
    if all(isinstance(x, int) and x == 0 for x in sequence):
        return 0
    next_integer = sequence[len(sequence)-1] + extrapolate(difference_sequence)
    return next_integer

def main():
    sum = 0
    with open("Day_9/Puzzle_input.txt") as file:
        for line in file:
            sequence = [int(i) for i in line.split()]
            sum += extrapolate(sequence)
    print(sum)
            

if __name__ == '__main__':
    main()