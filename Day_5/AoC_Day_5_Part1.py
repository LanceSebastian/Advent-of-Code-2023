#Advent of Code
#Day 5: If You Give A Seed A Fertilizer

def getLocation(map, seed):
    location_number = 0
    # for loop through map, match the seed to the map till location
    return location_number

def getMapValues(file):
    array_output = []
    #for loop through file, read first char, if digit then add line.. (work on algor)
    return array_output

def main():
    lowest_location = None
    seed_packet = []
    map_translation = []
    with open("Day_5/sample.txt") as file:
        seed_packet = list(filter(None,file.readline().split(':')[1].strip('\n').split(' ')))
        map_translation = getMapValues(file)
        for seed in seed_packet:
            location = getLocation(map_translation, seed)
            if lowest_location is None or location < lowest_location:
                lowest_location = location
            

    print(lowest_location)

if __name__ == '__main__':
    main()