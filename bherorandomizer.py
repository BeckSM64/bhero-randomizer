#!/bin/env python3

import sys
import random
import subprocess
import os.path

# w1 a1
#battle_room  = 0x001574D0 #0x000FA75C
hyper_room   = 0x000FA4F0
heavy_room   = 0x000FA4F0
secret_room  = 0x000FA4F6
sky_room     = 0x000FA4FC

# w1 a2
blue_cave    = 0x000FA744
hole_lake    = 0x000FA510
red_cave     = 0x000FA514
big_cannon   = 0x000FA518
dark_wood    = 0x000FA51A
dragon_road  = 0x000FA51C
nitros_1     = 0x000FA524

# w1 a3
clown_valley = 0x000FA74C
great_rock   = 0x000FA52C
fog_route    = 0x000FA530
endol_1      = 0x000FA534

# w2 a1
groog_hills  = 0x000FA6B0
bubble_hole  = 0x000FA540
erars_lake   = 0x000FA548
waterway     = 0x000FA6A0
water_slider = 0x000FA6A4

# w2 a2
rockin_road  = 0x000FA55C
water_pool   = 0x000FA572
warp_room    = 0x000FA56E
millian_room = 0x000FA56C
dark_prison  = 0x000FA578
nitros_2     = 0x000FA574

# w2 a3
killer_gate  = 0x000FA77C
spiral_tower = 0x000FA594
snake_route  = 0x000FA598
baruda_1     = 0x000FA59C

# w3 a1
hades_crater = 0x000FA778
magma_lake   = 0x000FA5AC
magma_dam    = 0x000FA5B0
crysta_hole  = 0x000FA5B4
emerald_tube = 0x000FA5B6

# w3 a2
death_temple = 0x000FA5B8
death_road   = 0x000FA5C4
death_garden = 0x000FA5C6
float_zone   = 0x000FA5D4
aqua_tank    = 0x000FA5D8
aquaway      = 0x000FA7A0
nitros_3     = 0x000FA5E0

# w3 a3
hard_coaster = 0x000FA768
dark_maze    = 0x000FA5E8
mad_coaster  = 0x000FA600
move_stone   = 0x000FA604
bolban_1     = 0x000FA608

# w4 a1
hopper_land  = 0x000FA770
jun_falls    = 0x000FA61C
cool_cave    = 0x000FA61A
freeze_lake  = 0x000FA618

# w4 a2
snow_land    = 0x000FA620
storm_valley = 0x000FA628
snow_circuit = 0x000FA62C
heaven_sky   = 0x000FA654
eye_snake    = 0x000FA634
nitros_4     = 0x000FA630

# w4 a3
air_room     = 0x000FA7A4
zero_g_room  = 0x000FA640
mirror_room  = 0x000FA644
natia_1      = 0x000FA6EA

# w5
endol_2      = 0x000FA788
baruda_2     = 0x000FA65C
cronus       = 0x000FA660
nitros_5     = 0x000FA664
bolban_2     = 0x000FA7B4
natia_2      = 0x000FA66C
bagular      = 0x000FA670

# World 1 addresses
world_1_rom_addresses = [
    hyper_room, heavy_room, secret_room, sky_room,
    blue_cave, hole_lake, red_cave, big_cannon,
    dark_wood, dragon_road, nitros_1, clown_valley,
    great_rock, fog_route, endol_1
]

# World 2 addresses
world_2_rom_addresses = [
    groog_hills, bubble_hole, erars_lake, waterway,
    water_slider, rockin_road, water_pool, warp_room,
    millian_room, dark_prison, nitros_2, killer_gate,
    spiral_tower, snake_route, baruda_1
]

# World 3 addresses
world_3_rom_addresses = [
    hades_crater, magma_lake, magma_dam, crysta_hole,
    emerald_tube, death_temple, death_road, death_garden,
    float_zone, aqua_tank, aquaway, nitros_3,
    hard_coaster, dark_maze, mad_coaster, move_stone,
    bolban_1
]

# World 4 addresses
world_4_rom_addresses = [
    hopper_land, jun_falls, cool_cave, freeze_lake,
    snow_land, storm_valley, snow_circuit, heaven_sky,
    eye_snake, nitros_4, air_room, zero_g_room,
    mirror_room, natia_1
]

# World 5 addresses
world_5_rom_addresses = [
    endol_2, baruda_2, cronus, nitros_5,
    bolban_2, natia_2, bagular
]

# list of addresses in rom that hold each map id
rom_addresses = world_1_rom_addresses + world_2_rom_addresses + world_3_rom_addresses + world_4_rom_addresses + world_5_rom_addresses

world_1_map_ids = [
    0x3,  0x4,  0x5,  0x6,  0x9,
    0xA,  0xB,  0xC,  0xD,  0xE,
    0xF,  0x10, 0x11, 0x12, 0x13
]

world_2_map_ids = [
    0x15, 0x16, 0x17, 0x18, 0x19,
    0x1B, 0x1C, 0x1D, 0x1E, 0x1F,
    0x21, 0x22, 0x23, 0x25, 0x57
]

world_3_map_ids = [
    0x8,  0x27, 0x28, 0x29,
    0x2A, 0x2D, 0x2F, 0x30,
    0x31, 0x32, 0x33, 0x35,
    0x36, 0x37, 0x38, 0x39,
    0x58
]

world_4_map_ids = [
    0x3C, 0x3B, 0x3D, 0x3E, 0x40, 0x41, 0x42,
    0x43, 0x44, 0x46, 0x47, 0x4A, 0x59, 0x5A
]

world_5_map_ids = [
    0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51, 0x52
]

# id of each map
map_ids = world_1_map_ids + world_2_map_ids + world_3_map_ids + world_4_map_ids + world_5_map_ids

# reads in the rom file and return a byte array
def read_file(fname):
    with open(fname, "rb") as f:

        file_array = bytearray(f.read())
        random.shuffle(rom_addresses)

        # create log to track which rom addresses
        # were assigned to which maps
        with open("mapLog.txt", "w") as g:
            # assign new values to map id rom addresses
            for rom_address, map_id in zip(rom_addresses, map_ids):
                file_array[rom_address] = map_id
                g.write(str(hex(rom_address)) + ": " + str(hex(map_id)) + '\n')

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
        sys.exit("Incorrect number of arguments. Usage: python3 bherorandomizer.py <input_file>")

    # get file as input
    input_name = sys.argv[1]
    output_name = input_name

    # help
    if ((sys.argv[1] == "-h") or (sys.argv[1] == "-help")):
        sys.exit("Input must be a Bomberman Hero ROM file with .n64 extension. \n Usage: python3 bherorandomizer.py <input_file>")

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
    subprocess.call(["python3", n64converter, "-i", input_name, "-o", output_name])

    # hold the bytes read in from the rom file
    rom_data = read_file(output_name)

    # write modified data back to rom
    write_file(output_name, rom_data)

    # recalculate checksum
    subprocess.call(["python3", n64checksum, output_name])

    # print success
    print("Success. Generated output file " + output_name + " in current directory")

    print(len(rom_addresses))
    print(len(map_ids))

if __name__ == "__main__":
    main()