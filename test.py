#!/bin/env python3

import sys
import random
import subprocess
import os.path

# w1 a1
hyper_room = {0x3 : 0x000FA4F0}
heavy_room = {0x4 : 0x000FA4F4}
sky_room = {0x5 : [0x000FA4FC, 0x000FA504]}
secret_room = {0x6 : 0x000FA4F6}

# w1 a2
blue_cave = {0x9 : 0x000FA744}
hole_lake = {0xA : 0x000FA510}
red_cave = {0xB : 0x000FA514}
dark_wood = {0xC : 0x000FA51A}
big_cannon = {0xD : 0x000FA518}
dragon_road = {0xE : [0x000FA51C, 0x000FA520]}
nitros_1 = {0xF : 0x000FA524}

# w1 a3
clown_valley = {0x10 : 0x000FA74C}
great_rock = {0x11 : 0x000FA52C}
fog_route = {0x12 : 0x000FA530}
endol_1 = {0x13 : 0x000FA534}

world_1_two_exits = [hyper_room, red_cave]
world_1_after_two_exits = [heavy_room, secret_room, dark_wood, big_cannon]
world_1_has_two_rom_addresses = [sky_room, dragon_road]

world_1_maps = [
    hyper_room,
    heavy_room,
    secret_room,
    sky_room,
    blue_cave,
    hole_lake,
    red_cave,
    dark_wood,
    big_cannon,
    dragon_road,
    nitros_1,
    clown_valley,
    great_rock,
    fog_route,
    endol_1,
]

world_1_maps_temp = world_1_maps.copy()

# loop through maps
# if it's in two exits, ignore
# next two levels must go to levels that come after two exits
new_level_order = {}

def isLastMapTooEarly(map_to_replace, currentIteration):
    last_map = world_1_maps[-1]
    if ((map_to_replace == last_map) and (currentIteration != (len(world_1_maps) -1))):
        return True
    else:
        return False

def isMapSelf(map_to_replace, current_map):
    if map_to_replace == current_map:
        return True

# Loop through list of maps
for i in range(len(world_1_maps)):

    # Set the current map (Manually set the first map that gets swapped)
    if i == 0:
        current_map = hyper_room

    map_to_replace = {}

    # Randomly generated value to get a random map from the temp map list
    randValue = random.randint(0, len(world_1_maps_temp) - 1)
        
    # if level is two level exit, ignore
    if current_map in world_1_two_exits:

        map_to_replace = current_map

    # if the level is one of two levels that comes after a two exit
    elif current_map in world_1_after_two_exits:

        map_to_replace = current_map

    elif current_map in world_1_has_two_rom_addresses:

        map_to_replace = current_map

    # else, this is a normal single exit level
    else:

        # Can switch with any other normal single exit level
        map_to_replace = world_1_maps_temp[randValue]

        # Ensure that the map to replace is a single exit normal level
        while map_to_replace in world_1_two_exits or map_to_replace in world_1_after_two_exits or map_to_replace in world_1_has_two_rom_addresses or isLastMapTooEarly(map_to_replace, i):
            randValue = random.randint(0, len(world_1_maps_temp) - 1)
            map_to_replace = world_1_maps_temp[randValue]

    # Remove it from the temp map list
    world_1_maps_temp.remove(map_to_replace)
    
    # Insert new level order
    for current_id, current_rom in current_map.items():
        for map_to_replace_id, map_to_replace_rom in map_to_replace.items():
            if type(current_rom) == list:
                new_level_order[current_rom[0]] = map_to_replace_id
                new_level_order[current_rom[1]] = map_to_replace_id
            else:
                new_level_order[current_rom] = map_to_replace_id

    # Debug output
    for current_id, current_rom in current_map.items():
        for replace_id, replace_rom in map_to_replace.items():
            print(f"{hex(current_id)} -> {hex(replace_id)}")

    # Get the next map after the map to replace
    if i < (len(world_1_maps) - 1):
        current_map = world_1_maps[world_1_maps.index(map_to_replace) + 1]


for id, rom in new_level_order.items():
    print(hex(id), hex(rom))




# reads in the rom file and return a byte array
def read_file(fname):
    with open(fname, "rb") as f:

        file_array = bytearray(f.read())

        # create log to track which rom addresses
        # were assigned to which maps
        with open("mapLog.txt", "w") as g:
            # assign new values to map id rom addresses
            for rom_address, map_id in new_level_order.items():
                file_array[rom_address] = map_id
                g.write(str(hex(rom_address)) + ": " + str(hex(map_id)) + "\n")

        return file_array


# writes the modified data back to the rom
def write_file(fname, data):
    with open(fname, "wb") as f:
        f.write(data)


# main
def main():

    # tools
    n64converter = "N64RomConverter.py"
    n64checksum = "n64cksum.py"

    # check number of args
    if len(sys.argv) != 2:
        sys.exit(
            "Incorrect number of arguments. Usage: python3 bherorandomizer.py <input_file>"
        )

    # get file as input
    input_name = sys.argv[1]
    output_name = input_name

    # help
    if (sys.argv[1] == "-h") or (sys.argv[1] == "-help"):
        sys.exit(
            "Input must be a Bomberman Hero ROM file with .n64 extension. \n Usage: python3 bherorandomizer.py <input_file>"
        )

    # check file extension
    if ".n64" not in input_name:
        sys.exit("Invalid input file. Make sure the file extension is .n64")

    # ensure dependencies are in directory
    if not os.path.exists(n64converter):
        sys.exit("Cannot locate " + n64converter + ". Exiting...")
    if not os.path.exists(n64checksum):
        sys.exit("Cannot locate " + n64checksum + ". Exiting...")

    # change file extension for ouput file
    output_name = output_name.replace(".n64", ".z64")

    # N64CONVERTER -i [INPUT] -o [OUTPUT]
    subprocess.call(["python", n64converter, "-i", input_name, "-o", output_name])

    # hold the bytes read in from the rom file
    rom_data = read_file(output_name)

    # write modified data back to rom
    write_file(output_name, rom_data)

    # recalculate checksum
    subprocess.call(["python", n64checksum, output_name])

    # print success
    print("Success. Generated output file " + output_name + " in current directory")


if __name__ == "__main__":
    main()
