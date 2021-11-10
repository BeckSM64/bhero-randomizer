import random
import subprocess
import os
from RomData import *


class BheroRandomizer:
    def __init__(self, seed, inputRomFile, outputRomDir):

        # Dictionary to hold the new level order that is generated
        self.new_level_order = {}

        # Temporary list of all maps that keeps track of which levels haven't been randomized yet
        self.maps_temp = maps.copy()

        # Seed for the random function
        self.seed = seed

        # Clean ROM file to randomize
        self.inputRomFile = inputRomFile

        # Directory to output randomized ROM to
        self.outputRomDir = outputRomDir

        # Output file (Force z64 output for now)
        self.outputRomFile = (
            self.outputRomDir
            + "/"
            + self.inputRomFile.split("/")[-1][:-4]
            + ".rando"
            + ".z64"
        )

    def isLastMapTooEarly(self, map_to_replace, currentIteration):
        last_map = maps[-1]
        if (map_to_replace == last_map) and (currentIteration != (len(maps) - 1)):
            return True
        else:
            return False

    def isMapSelf(self, map_to_replace, current_map):
        if map_to_replace == current_map:
            return True

    def randomize_stages(self):

        # Check that seed isn't blank
        if self.seed == "":
            return -1

        # Set the seed
        random.seed(self.seed)

        # Loop through list of maps
        for i in range(len(maps)):

            # Set the current map (Manually set the first map that gets swapped)
            if i == 0:
                current_map = hyper_room

            map_to_replace = {}

            # Randomly generated value to get a random map from the temp map list
            randValue = random.randint(0, len(self.maps_temp) - 1)

            # if level is two level exit, ignore
            if current_map in two_exits:

                map_to_replace = self.maps_temp[randValue]

                while (
                    map_to_replace in do_not_swap
                    or map_to_replace in after_two_exits
                    or map_to_replace in has_two_rom_addresses
                    or self.isLastMapTooEarly(map_to_replace, i)
                ):
                    randValue = random.randint(0, len(self.maps_temp) - 1)
                    map_to_replace = self.maps_temp[randValue]

            # if the level is one of two levels that comes after a two exit
            elif current_map in after_two_exits or current_map in do_not_swap:

                map_to_replace = current_map

            elif current_map in has_two_rom_addresses:

                map_to_replace = self.maps_temp[randValue]

                while (
                    map_to_replace not in has_two_rom_addresses
                    or map_to_replace in do_not_swap
                    or self.isLastMapTooEarly(map_to_replace, i)
                ):
                    randValue = random.randint(0, len(self.maps_temp) - 1)
                    map_to_replace = self.maps_temp[randValue]

            # else, this is a normal single exit level
            else:

                # Can switch with any other normal single exit level
                map_to_replace = self.maps_temp[randValue]

                # Ensure that the map to replace is a single exit normal level
                while (
                    map_to_replace in do_not_swap
                    or map_to_replace in after_two_exits
                    or map_to_replace in has_two_rom_addresses
                    or self.isLastMapTooEarly(map_to_replace, i)
                ):
                    randValue = random.randint(0, len(self.maps_temp) - 1)
                    map_to_replace = self.maps_temp[randValue]

            # Remove it from the temp map list
            self.maps_temp.remove(map_to_replace)

            # Insert new level order
            for current_id, current_rom in current_map.items():
                for map_to_replace_id, map_to_replace_rom in map_to_replace.items():
                    if type(current_rom) == list:
                        self.new_level_order[current_rom[0]] = map_to_replace_id
                        self.new_level_order[current_rom[1]] = map_to_replace_id
                    else:
                        self.new_level_order[current_rom] = map_to_replace_id

            # Debug output
            # for current_id, current_rom in current_map.items():
            #     for replace_id, replace_rom in map_to_replace.items():
            #         print(f"{hex(current_id)} -> {hex(replace_id)}")

            # Get the next map after the map to replace
            if i < (len(maps) - 1):
                current_map = maps[maps.index(map_to_replace) + 1]

    # reads in the rom file and return a byte array
    def read_file(self):

        # Check if input file exists
        if not os.path.exists(self.inputRomFile):
            return -1

        with open(self.inputRomFile, "rb") as f:

            file_array = bytearray(f.read())

            # NOP the instruction that marks levels as completed
            file_array[0x0005CC38] = 0x0
            file_array[0x0005CC39] = 0x0
            file_array[0x0005CC3A] = 0x0
            file_array[0x0005CC3B] = 0x0

            # create log to track which rom addresses
            # were assigned to which maps
            with open("mapLog.txt", "w") as g:
                # assign new values to map id rom addresses
                for rom_address, map_id in self.new_level_order.items():
                    file_array[rom_address] = map_id
                    g.write(str(hex(rom_address)) + ": " + str(hex(map_id)) + "\n")

            return file_array

    # writes the modified data back to the rom
    def write_file(self, data):

        # Check if output path is valid
        if not os.path.exists(self.outputRomDir):
            return -1

        with open(self.outputRomFile, "wb") as f:
            f.write(data)

    def generate_rom(self):

        # Tools
        n64converter = "N64RomConverter.py"
        n64checksum = "n64cksum.py"

        # N64CONVERTER -i [INPUT] -o [OUTPUT]
        subprocess.call(
            ["python", n64converter, "-i", self.inputRomFile, "-o", self.outputRomFile]
        )

        # Shuffle stages
        success = self.randomize_stages()

        # Check if randomize stages returned an error
        if success == -1:
            return -1

        # Read in the ROM file
        rom_data = self.read_file()

        # Check if read file succeeded
        if rom_data == -1:
            return -1

        # Write the new ROM file
        success = self.write_file(rom_data)

        # Check if write file succeeded
        if success == -1:
            return -1

        # Recalculate checksum
        subprocess.call(["python", n64checksum, self.outputRomFile])

        # Print success
        print(
            "Success. Generated output file "
            + self.outputRomFile.split("/")[-1]
            + " in "
            + self.outputRomDir
        )
