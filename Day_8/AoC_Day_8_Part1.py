#Advent of code 
#Haunted Wasteland
def followPath(instructions, map):
    step = 0
    start = "AAA"
    end = "ZZZ"
    paths = map[start]
    current_location = start
    has_ended = False
    
    while not has_ended:
        char = instructions[step%(len(instructions)-1)]
        step += 1
        print(current_location)
        if char == 'L':
            current_location = paths[0]
            paths = map[paths[0]]
        else:
            current_location = paths[1]
            paths = map[paths[1]]

        if current_location == end:
            return step

        


def main():
    steps_required = 0
    with open("Day_8/Puzzle_input.txt") as file:
        instructions = file.readline()
        map = {}
        
        for line in file:
            line = line.strip('\n|')
            if not line:
                continue
            location = line.split('=')[0].strip(' ')
            paths = line.split('=')[1].strip(' ()').split(', ')
            map[location] = [paths[0],paths[1]]
        
        steps_required = followPath(instructions,map)
    print(steps_required)


if __name__ == '__main__':
    main()
