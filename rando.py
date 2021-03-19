#!/bin/env python3

import sys
import random
import subprocess
import os.path

# w1 a1
#battle_room  = 0x001574D0 #0x000FA75C
hyper_room   = 0x000FA4F0
heavy_room   = 0x000FA4F4
#secret_room  = 0x000FA4F6
sky_room     = 0x000FA4FC

# w1 a2
#blue_cave    = 0x000FA524 #0x000FA744
hole_lake    = 0x000FA510
red_cave     = 0x000FA514
#big_cannon   = 0x000FA518
dark_wood    = 0x000FA51A
dragon_road  = 0x000FA51C
nitros_1     = 0x000FA524 #0x000FA748

# w1 a3
clown_valley = 0x000FA74C
great_rock   = 0x000FA52C
fog_route    = 0x000FA530
endol_1      = 0x000FA534 #0x000FA763

# w2 a1
#groog_hills  = 0x000FA7D3
#bubble_hole  = 0x000FA540
erars_lake   = 0x000FA548
#waterway     = 0x000FA6A0
#water_slider = 0x000FA6A4

# w2 a2
#rockin_road  = 0x000FA55C #0x000FA750
water_pool   = 0x000FA570
#warp_room    = 0x000FA56E
millian_room = 0x000FA56C
dark_prison  = 0x000FA578
nitros_2     = 0x000FA574 #0x000FA754

# w2 a3
killer_gate  = 0x000FA688 #0x000FA77C
spiral_tower = 0x000FA594
snake_route  = 0x000FA598
baruda_1     = 0x000FA59C #0x000FA780

# w3 a1
#hades_crater = 0x000FA79C
magma_lake   = 0x0007A5AC
magma_dam    = 0x000FA5B0
crysta_hole  = 0x000FA5B4
#emerald_tube = 0x000FA5B6

# w3 a2
#death_temple = 0x000FA5B8 #0x000FA774
death_road   = 0x000FA5c4
death_garden = 0x000FA5c6
float_zone   = 0x000FA5D4
aqua_tank    = 0x000FA5D8
aquaway      = 0x000FA7A0 #0x000FA7E0
#nitros_3     = 0x000FA5E0 #0x000FA760

# w3 a3
#hard_coaster = 0x000FA68C #0x000FA768
dark_maze    = 0x000FA5E8
mad_coaster  = 0x000FA600
move_stone   = 0x000FA604
bolban_1     = 0x000FA608 #0x000FA790

# w4 a1
#hopper_land  = 0x000FA7A8
jun_falls    = 0x000FA61C
cool_cave    = 0x000FA61A
freeze_lake  = 0x000FA618

# w4 a2
snow_land    = 0x000FA620 #0x000FA794
storm_valley = 0x000FA628
snow_circuit = 0x000FA62C
heaven_sky   = 0x000FA650
eye_snake    = 0x000FA634
nitros_4     = 0x000FA630 #0x000FA784

# w4 a3
air_room     = 0x000FA7A4
zero_g_room  = 0x000FA640
mirror_room  = 0x000FA644
#natia_1      = 0x000FA798

# w5
#endol_2      = 0x000FA7D0
baruda_2     = 0x000FA65C
cronus       = 0x000FA660
nitros_5     = 0x000FA664 #0x000FA7B0
bolban_2     = 0x000FA7B4
natia_2      = 0x000FA66C #0x000FA66C
bagular      = 0x000FA670 #0x000FA7B8

# list of addresses in rom that hold each map id
rom_addresses = [
    hyper_room,   heavy_room,   sky_room,     hole_lake,  
    red_cave,     dark_wood,    dragon_road,  nitros_1, 
    great_rock,   clown_valley, fog_route,    endol_1,
    erars_lake,   water_pool,   dark_prison,  nitros_2,
    killer_gate,  spiral_tower, snake_route,  baruda_1,
    magma_lake,   magma_dam,    crysta_hole,  death_road,
    float_zone,   aqua_tank,    aquaway,      dark_maze,
    mad_coaster,  move_stone,   bolban_1,     jun_falls,
    cool_cave,    snow_land,    storm_valley, snow_circuit,
    heaven_sky,   eye_snake,    nitros_4,     air_room,
    zero_g_room,  mirror_room,  baruda_2,     cronus,
    nitros_5,     bolban_2,     natia_2
]

# id of each map
map_ids = [
    0x3,  0x4,  0x5,  0xA,  0xB,  0xC,  0xE,  0xF,
    0x10, 0x11, 0x12, 0x13, 0x17, 0x1B, 0x1D, 0x21,
    0x22, 0x23, 0x25, 0x28, 0x29, 0x2A, 0x30, 0x31,
    0x32, 0x33, 0x36, 0x37, 0x38, 0x39, 0x3C, 0x3E,
    0x40, 0x41, 0x42, 0x43, 0x44, 0x69, 0x6A, 0x4A,
    0x57, 0x59, 0x4D, 0x4E, 0x4F, 0x50, 0x51
]

def moveMapRoutine(file_array):

    #baseAddress = 0x003CEA90
    baseAddress = 0x0004D76C

    # ROUTINE THAT SETS UP NEXT MAP TO BE LOADED
    file_array[baseAddress] = 0xA3 # SB T1, $001E (SP)
    file_array[baseAddress + 0x1] = 0xA9
    file_array[baseAddress + 0x2] = 0x00
    file_array[baseAddress + 0x3] = 0x1E

    file_array[baseAddress + 0x4] = 0x3C # LUI T2, $8017
    file_array[baseAddress + 0x5] = 0x0A
    file_array[baseAddress + 0x6] = 0x80
    file_array[baseAddress + 0x7] = 0x17

    file_array[baseAddress + 0x8] = 0x8D # LW T2, $E420 (T2)
    file_array[baseAddress + 0x9] = 0x4A
    file_array[baseAddress + 0xA] = 0xE4
    file_array[baseAddress + 0xB] = 0x20

    file_array[baseAddress + 0xC] = 0x3C # LUI AT, $8017
    file_array[baseAddress + 0xD] = 0x01
    file_array[baseAddress + 0xE] = 0x80
    file_array[baseAddress + 0xF] = 0x17

    file_array[baseAddress + 0x10] = 0xA4 # SH T2, $E42C (AT)
    file_array[baseAddress + 0x11] = 0x2A
    file_array[baseAddress + 0x12] = 0xE4
    file_array[baseAddress + 0x13] = 0x2C

    file_array[baseAddress + 0x14] = 0x3C # LUI AT, $8017
    file_array[baseAddress + 0x15] = 0x01
    file_array[baseAddress + 0x16] = 0x80
    file_array[baseAddress + 0x17] = 0x17

    file_array[baseAddress + 0x18] = 0xA4 # SH R0, $E428 (AT)
    file_array[baseAddress + 0x19] = 0x20
    file_array[baseAddress + 0x1A] = 0xE4
    file_array[baseAddress + 0x1B] = 0x28

    file_array[baseAddress + 0x1C] = 0x93 # LBU T3, $001F (SP)
    file_array[baseAddress + 0x1D] = 0xAB
    file_array[baseAddress + 0x1E] = 0x00
    file_array[baseAddress + 0x1F] = 0x1F

    file_array[baseAddress + 0x20] = 0x3C # LUI AT, $8017
    file_array[baseAddress + 0x21] = 0x01
    file_array[baseAddress + 0x22] = 0x80
    file_array[baseAddress + 0x23] = 0x17

    file_array[baseAddress + 0x24] = 0xA4 # SH T3, $E42A (AT)
    file_array[baseAddress + 0x25] = 0x2B
    file_array[baseAddress + 0x26] = 0xE4
    file_array[baseAddress + 0x27] = 0x2A

    file_array[baseAddress + 0x28] = 0x00 # NOP
    file_array[baseAddress + 0x29] = 0x00 # NOP
    file_array[baseAddress + 0x2A] = 0x00 # NOP
    file_array[baseAddress + 0x2B] = 0x00 # NOP

    # NOP the original routine and put a jump to the new one
    file_array[0x0005C14C] = 0x00 # NOP
    file_array[0x0005C14D] = 0x00 # NOP
    file_array[0x0005C14E] = 0x00 # NOP
    file_array[0x0005C14F] = 0x00 # NOP
    file_array[0x0005C150] = 0x00 # NOP
    file_array[0x0005C151] = 0x00 # NOP
    file_array[0x0005C152] = 0x00 # NOP
    file_array[0x0005C153] = 0x00 # NOP
    file_array[0x0005C154] = 0x00 # NOP
    file_array[0x0005C155] = 0x00 # NOP
    file_array[0x0005C156] = 0x00 # NOP
    file_array[0x0005C157] = 0x00 # NOP
    file_array[0x0005C158] = 0x00 # NOP
    file_array[0x0005C159] = 0x00 # NOP
    file_array[0x0005C15A] = 0x00 # NOP
    file_array[0x0005C15B] = 0x00 # NOP
    file_array[0x0005C15C] = 0x00 # NOP
    file_array[0x0005C15D] = 0x00 # NOP
    file_array[0x0005C15E] = 0x00 # NOP
    file_array[0x0005C15F] = 0x00 # NOP
    file_array[0x0005C160] = 0x00 # NOP
    file_array[0x0005C161] = 0x00 # NOP
    file_array[0x0005C162] = 0x00 # NOP
    file_array[0x0005C163] = 0x00 # NOP
    file_array[0x0005C164] = 0x00 # NOP
    file_array[0x0005C165] = 0x00 # NOP
    file_array[0x0005C166] = 0x00 # NOP
    file_array[0x0005C167] = 0x00 # NOP
    file_array[0x0005C168] = 0x00 # NOP
    file_array[0x0005C169] = 0x00 # NOP
    file_array[0x0005C16A] = 0x00 # NOP
    file_array[0x0005C16B] = 0x00 # NOP
    # file_array[0x0005C16C] = 0x08 # 08 #08 # J $0004CB6C J $003CDE90
    # file_array[0x0005C16D] = 0x0F # 01 #0F
    # file_array[0x0005C16E] = 0x37 # 32 #37
    # file_array[0x0005C16F] = 0xA4 # DB #A4
    file_array[0x0005C16C] = 0x08 #08 # J $0004CB6C J $003CDE90
    file_array[0x0005C16D] = 0x01 #0F
    file_array[0x0005C16E] = 0x32 #37
    file_array[0x0005C16F] = 0xDB #A4
    file_array[0x0005C170] = 0x00 # NOP
    file_array[0x0005C171] = 0x00 # NOP
    file_array[0x0005C172] = 0x00 # NOP
    file_array[0x0005C173] = 0x00 # NOP

    return file_array

# reads in the rom file and return a byte array
def read_file(fname):
    with open(fname, "rb") as f:

        file_array = bytearray(f.read())
        duplicate_rom_addresses = rom_addresses.copy()
        random.shuffle(duplicate_rom_addresses)

        # Move the normal routine for determining the next map
        file_array = moveMapRoutine(file_array)

        # Holds the base address for the custom map routine
        baseAddress = 0x0004D798
        #baseAddress = 0x003CEABC
        offset = 0x8004CB68 + 0x56

        maps = [0x3, 0xC, 0x3E]
        romMaps = [
                    0x7FD0, # Hyper Room
                    0x7FFA, # Dark Wood
                    0x80FA, # Cool Cave
                    0x822C  # Hades Crater
                ]

        # 0004DBC8
        for i in range(len(romMaps) - 1):

            # Convert map ram address to a string
            romMap = str(hex(romMaps[i]))

            # Slice the string to get the first two and last two bytes
            romMap = romMap[2:]
            beginMap = romMap[:2]
            endMap = romMap[2:]

            # Convert the two sets of bytes back to hex values from string
            beginMapInt = int(beginMap, base=16)
            endMapInt   = int(endMap, base=16)

            beginMapHex = hex(beginMapInt)
            endMapHex   = hex(endMapInt)

            # Convert map ram address to a string
            romMap1 = str(hex(romMaps[i + 1]))

            # Slice the string to get the first two and last two bytes
            romMap1 = romMap1[2:]
            beginMap1 = romMap1[:2]
            endMap1 = romMap1[2:]

            # Convert the two sets of bytes back to hex values from string
            beginMapInt1 = int(beginMap1, base=16)
            endMapInt1   = int(endMap1, base=16)

            beginMapHex1 = hex(beginMapInt1)
            endMapHex1   = hex(endMapInt1)

            # Custom routine to check previous map played and load a different map
            file_array[baseAddress] = 0x3C # LUI AT, $8017
            file_array[baseAddress + 0x1] = 0x01
            file_array[baseAddress + 0x2] = 0x80
            file_array[baseAddress + 0x3] = 0x17

            file_array[baseAddress + 0x4] = 0x90 # LBU T1, $E42D (AT)
            file_array[baseAddress + 0x5] = 0x29
            file_array[baseAddress + 0x6] = 0xE4
            file_array[baseAddress + 0x7] = 0x2D

            file_array[baseAddress + 0x8] = 0x3C # LUI AT, $8010
            file_array[baseAddress + 0x9] = 0x01
            file_array[baseAddress + 0xA] = 0x80
            file_array[baseAddress + 0xB] = 0x10

            file_array[baseAddress + 0xC] = 0x90 # LBU T2, $7FD0
            file_array[baseAddress + 0xD] = 0x2A
            file_array[baseAddress + 0xE] = beginMapInt
            file_array[baseAddress + 0xF] = endMapInt

            file_array[baseAddress + 0x10] = 0x11 # BEQ T1, T2, $0004D7B8
            file_array[baseAddress + 0x11] = 0x2A
            file_array[baseAddress + 0x12] = 0x00
            file_array[baseAddress + 0x13] = 0x03

            file_array[baseAddress + 0x14] = 0x00 # NOP
            file_array[baseAddress + 0x15] = 0x00
            file_array[baseAddress + 0x16] = 0x00
            file_array[baseAddress + 0x17] = 0x00

            file_array[baseAddress + 0x18] = 0x15#0x08 # J $00069C50
            file_array[baseAddress + 0x19] = 0x49#0x01
            file_array[baseAddress + 0x1A] = 0x00#0xA7
            file_array[baseAddress + 0x1B] = 0x07#0x15

            file_array[baseAddress + 0x1C] = 0x00 # NOP
            file_array[baseAddress + 0x1D] = 0x00
            file_array[baseAddress + 0x1E] = 0x00
            file_array[baseAddress + 0x1F] = 0x00

            file_array[baseAddress + 0x20] = 0x3C # LUI AT, $8010
            file_array[baseAddress + 0x21] = 0x01
            file_array[baseAddress + 0x22] = 0x80
            file_array[baseAddress + 0x23] = 0x10

            file_array[baseAddress + 0x24] = 0x90 # LBU T3, $7FF0 (AT)
            file_array[baseAddress + 0x25] = 0x2B
            file_array[baseAddress + 0x26] = beginMapInt1
            file_array[baseAddress + 0x27] = endMapInt1

            file_array[baseAddress + 0x28] = 0x3C # LUI AT, $8017
            file_array[baseAddress + 0x29] = 0x01
            file_array[baseAddress + 0x2A] = 0x80
            file_array[baseAddress + 0x2B] = 0x17

            file_array[baseAddress + 0x2C] = 0xA4 # SH T3, $E42A (AT)
            file_array[baseAddress + 0x2D] = 0x2B
            file_array[baseAddress + 0x2E] = 0xE4
            file_array[baseAddress + 0x2F] = 0x2A

            file_array[baseAddress + 0x30] = 0x08 # J $00069C50
            file_array[baseAddress + 0x31] = 0x01
            file_array[baseAddress + 0x32] = 0xA7
            file_array[baseAddress + 0x33] = 0x15

            baseAddress += 0x38
        
        # file_array[baseAddress + 0x30] = 0x08 # J $00069C50
        # file_array[baseAddress + 0x31] = 0x01
        # file_array[baseAddress + 0x32] = 0xA7
        # file_array[baseAddress + 0x33] = 0x15

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

if __name__ == "__main__":
    main()