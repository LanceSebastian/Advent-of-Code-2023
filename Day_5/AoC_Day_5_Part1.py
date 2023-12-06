#Advent of Code
#Day 5: If You Give A Seed A Fertilizer

def mapProcess(map, seed):
    output = None
    match = False
    for line in map:
        range = int(line[2])
        source = int(line[1])
        destination = int(line[0])

        #print(str(seed - source) + ':' + str(range))
        if seed - source < range and seed-source >= 0:
            output = seed + destination - source

    if output == None:
        return seed
    return output

def getLocation(map_array, seed):
    location_number = 0
    # for loop through map, match the seed to the map till location
    value = seed
    for map in map_array:
        value = mapProcess(map,value)
    location_number = value
    return location_number

def getMapValues(file):
    array_output = []

    temp_array = []
    for line in file:
        line = line.strip('\n')

        if not line:
            continue
        
        if not line[0].isdigit():
            array_output.append(temp_array)
            temp_array = []
        
        else:
            line = line.split(' ')
            temp_array.append(line)
    
    array_output.append(temp_array)
    array_output = list(filter(None, array_output))
    
    return array_output

def main():
    lowest_location = None
    seed_packet = []
    map_translation = []
    with open("Day_5/Puzzle_input.txt") as file:
        seed_packet = list(filter(None,file.readline().split(':')[1].strip('\n').split(' ')))
        map_translation = getMapValues(file)
        for seed in seed_packet:
            location = getLocation(map_translation, seed)
            if lowest_location is None or location < lowest_location:
                lowest_location = location

    print(lowest_location)



if __name__ == '__main__':
    main()