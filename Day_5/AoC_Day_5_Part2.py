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

def get_seeds(seed_packet):
    arranged_packets = []
    temp_array = []
    for index, seed in enumerate(seed_packet):
        seed = int(seed)
        if index%2 == 0:
            arranged_packets.append(temp_array)
            temp_array = []
        temp_array.append(seed)
        
    arranged_packets.append(temp_array)
    arranged_packets = list(filter(None, arranged_packets))

    return arranged_packets

#Look into yield
#look into functools, reduce
#look into zip

"""
This algorithm NEEDS to be more efficient.
Currently sat here for 30 minutes waiting for an output still.
Think about working in ranges or working with estimations
"""
def main():
    lowest_location = None
    seed_packet = []
    map_translation = []
    with open("Day_5/Puzzle_input.txt") as file:
        seed_packet = list(filter(None,file.readline().split(':')[1].strip('\n').split(' ')))
        seed_packet = get_seeds(seed_packet)
        map_translation = getMapValues(file)
        for seed in seed_packet:
            seed_number = seed[0]
            seed_range = seed[1]
            while seed_range > 0:
                location = getLocation(map_translation, seed_number)
                #print(str(seed) + ':'+ str(location))
                if lowest_location is None or location < lowest_location:
                    lowest_location = location
                seed_number += 1
                seed_range -= 1

    print(lowest_location)



if __name__ == '__main__':
    main()