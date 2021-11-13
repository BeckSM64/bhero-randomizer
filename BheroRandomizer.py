import random
import os
from RomData import *
from N64RomConverter import *


# Dictionary to hold the new level order that is generated
new_level_order = {}

# Temporary list of all maps that keeps track of which levels haven't been randomized yet
maps_temp = maps.copy()

def isLastMapTooEarly(map_to_replace, currentIteration):
    last_map = maps[-1]
    if (map_to_replace == last_map) and (currentIteration != (len(maps) - 1)):
        return True
    else:
        return False

def isMapSelf(map_to_replace, current_map):
    if map_to_replace == current_map:
        return True

def randomize_stages(seed):

    # Set the seed
    random.seed(seed)

    # Loop through list of maps
    for i in range(len(maps)):

        # Set the current map (Manually set the first map that gets swapped)
        if i == 0:
            current_map = hyper_room

        map_to_replace = {}

        # Randomly generated value to get a random map from the temp map list
        randValue = random.randint(0, len(maps_temp) - 1)

        # if level is two level exit, ignore
        if current_map in two_exits:

            map_to_replace = maps_temp[randValue]

            while (
                map_to_replace in after_two_exits
                or map_to_replace in has_two_rom_addresses
                or isLastMapTooEarly(map_to_replace, i)
            ):
                randValue = random.randint(0, len(maps_temp) - 1)
                map_to_replace = maps_temp[randValue]

        # if the level is one of two levels that comes after a two exit
        elif current_map in after_two_exits:

            map_to_replace = current_map

        elif current_map in has_two_rom_addresses:

            map_to_replace = maps_temp[randValue]

            while (
                map_to_replace in two_exits
                or map_to_replace in after_two_exits
                or isLastMapTooEarly(map_to_replace, i)
            ):
                randValue = random.randint(0, len(maps_temp) - 1)
                map_to_replace = maps_temp[randValue]

        # else, this is a normal single exit level
        else:

            # Can switch with any other normal single exit level
            map_to_replace = maps_temp[randValue]

            # Ensure that the map to replace is a single exit normal level
            while (
                map_to_replace in after_two_exits
                or isLastMapTooEarly(map_to_replace, i)
            ):
                randValue = random.randint(0, len(maps_temp) - 1)
                map_to_replace = maps_temp[randValue]

        # Remove it from the temp map list
        maps_temp.remove(map_to_replace)

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
        if i < (len(maps) - 1):
            current_map = maps[maps.index(map_to_replace) + 1]

# reads in the rom file and return a byte array
def read_file(fname, outputRomDir):

    file = os.path.join(outputRomDir, fname)
    with open(file, "rb") as f:

        file_array = bytearray(f.read())

        # NOP the instructions that prevent the game from loading with a bad CRC
        # so I don't have to write my own checksum utility cause I'm lazy
        file_array[0x0000066C] = 0x0
        file_array[0x0000066D] = 0x0
        file_array[0x0000066E] = 0x0
        file_array[0x0000066F] = 0x0
        file_array[0x00000678] = 0x0
        file_array[0x00000679] = 0x0
        file_array[0x0000067A] = 0x0
        file_array[0x0000067B] = 0x0

        # NOP the instruction that marks levels as completed
        file_array[0x0005CC38] = 0x0
        file_array[0x0005CC39] = 0x0
        file_array[0x0005CC3A] = 0x0
        file_array[0x0005CC3B] = 0x0

        # create log to track which rom addresses
        # were assigned to which maps
        with open("mapLog.txt", "w") as g:
            # assign new values to map id rom addresses
            for rom_address, map_id in new_level_order.items():
                file_array[rom_address] = map_id
                g.write(str(hex(rom_address)) + ": " + str(hex(map_id)) + "\n")

        return file_array

# writes the modified data back to the rom
def write_file(fname, outputRomDir, data):

    file = os.path.join(outputRomDir, fname)
    with open(file, "wb") as f:
        f.write(data)

def generate_rom(inputRomFile, outputRomDir, seed):

    global new_level_order
    global maps_temp

    # Check that paths exist
    if not os.path.exists(inputRomFile) or not os.path.exists(outputRomDir):
        return -1

    # Make sure temp maps is full and new level order is empty
    new_level_order = {}
    maps_temp = maps.copy()

    # get file as input
    input_name = inputRomFile
    output_name = input_name.split("/")[-1][:-4] + ".rando.z64"

    # N64CONVERTER -i [INPUT] -o [OUTPUT]
    convertRom(input_name, output_name, outputRomDir)

    # generate the new level order dictionary
    randomize_stages(seed)

    # hold the bytes read in from the rom file
    rom_data = read_file(output_name, outputRomDir)

    # write modified data back to rom
    write_file(output_name, outputRomDir, rom_data)

    # print success
    print("Success. Generated output file " + output_name + " in current directory")
