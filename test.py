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

# # loop through maps
# # if it's in two exits, ignore
# # next two levels must go to levels that come after two exits
# new_level_order = {}

# # Loop through list of maps
# for index, map in enumerate(world_1_maps):

#     # Get id and rom address in map dict
#     for id, rom_address in map.items():
        
#         # if level is two level exit, ignore
#         if map in world_1_two_exits:
#             # Don't switch with anything for now
#             pass

#         # if the level is one of two levels that comes after a two exit
#         elif map in world_1_after_two_exits:
#             # Can only switch with other levels that come after two exit levels
#             pass

#         # else, this is a normal single exit level
#         else:
#             # Can switch with any other normal single exit level
#             pass


# loop through maps
# if it's in two exits, ignore
# next two levels must go to levels that come after two exits
new_level_order = {}

# Loop through list of maps
for i in range(len(world_1_maps)):

    # Set the current map
    if i == 0:
        current_map = hyper_room

    # # Get id and rom address in map dict
    # for id, rom_address in world_1_maps.items():
        
    # if level is two level exit, ignore
    if current_map in world_1_two_exits:

        # Don't switch with anything for now
        if i < (len(world_1_maps) - 1):
            current_map = world_1_maps[world_1_maps.index(current_map) + 1]
        pass

    # if the level is one of two levels that comes after a two exit
    elif current_map in world_1_after_two_exits:

        # Can only switch with other levels that come after two exit levels
        if i < (len(world_1_maps) - 1):
            current_map = world_1_maps[world_1_maps.index(current_map) + 1]
        pass

    elif current_map in world_1_has_two_rom_addresses:

        if i < (len(world_1_maps) - 1):
            current_map = world_1_maps[world_1_maps.index(current_map) + 1]
        pass

    # else, this is a normal single exit level
    else:
        
        # Randomly generated value to get a random map from the temp map list
        randValue = random.randint(0, len(world_1_maps_temp) - 1)

        # Can switch with any other normal single exit level
        map_to_replace = world_1_maps_temp[randValue]

        # Ensure that the map to replace is a single exit normal level
        while map_to_replace in world_1_two_exits or map_to_replace in world_1_after_two_exits or  map_to_replace in world_1_has_two_rom_addresses:
            randValue = random.randint(0, len(world_1_maps_temp) - 1)
            map_to_replace = world_1_maps_temp[randValue]

        # Remove it from the temp map list
        world_1_maps_temp.remove(map_to_replace)
        
        # Insert new level order
        for current_id, current_rom in current_map.items():
            for map_to_replace_id, map_to_replace_rom in map_to_replace.items():
                new_level_order[current_rom] = map_to_replace_id

        # Get the next map after the map to replace
        if i < (len(world_1_maps) - 1):
            current_map = world_1_maps[world_1_maps.index(map_to_replace) + 1]

    print(new_level_order)
    for id, rom in new_level_order.items():
        print(hex(id), hex(rom))
