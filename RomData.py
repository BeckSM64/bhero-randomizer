
# w1 a1
hyper_room = {0x3: 0x000FA4F0}
heavy_room = {0x4: 0x000FA4F4}
sky_room = {0x5: [0x000FA4FC, 0x000FA504]}
secret_room = {0x6: 0x000FA4F6}

# w1 a2
blue_cave = {0x9: 0x000FA744}
hole_lake = {0xA: 0x000FA510}
red_cave = {0xB: 0x000FA514}
dark_wood = {0xC: 0x000FA51A}
big_cannon = {0xD: 0x000FA518}
dragon_road = {0xE: [0x000FA51C, 0x000FA520]}
nitros_1 = {0xF: 0x000FA524}

# w1 a3
clown_valley = {0x10: 0x000FA74C}
great_rock = {0x11: 0x000FA52C}
fog_route = {0x12: 0x000FA530}
endol_1 = {0x13: 0x000FA534}

# w2 a1
groog_hills = {0x15: 0x000FA76C}
bubble_hole = {0x16: 0x000FA540}
erars_lake = {0x17: 0x000FA548}
waterway = {0x18: 0x000FA6A0}
water_slider = {0x19: 0x000FA6A4}

# w2 a2
rockin_road = {0x1C: [0x000FA55C, 0x000FA564]}
water_pool = {0x1B: 0x000FA572}
warp_room = {0x1E: 0x000FA56E}
millian_road = {0x1F: 0x000FA56C}
dark_prison = {0x1D: [0x000FA578, 0x000FA58C]}
nitros_2 = {0x57: 0x000FA574}

# w2 a3
killer_gate = {0x21: 0x000FA77C}
spiral_tower = {0x22: 0x000FA594}
snake_route = {0x23: 0x000FA598}
baruda_1 = {0x25: 0x000FA59C}

# w3 a1
hades_crater = {0x27: 0x000FA778}
magma_lake = {0x28: 0x000FA5AC}
magma_dam = {0x29: 0x000FA5B0}
crysta_hole = {0x2A: 0x000FA5B4}
emerald_tube = {0x8: 0x000FA5B6}

# w3 a2
death_temple = {0x2D: [0x000FA5B8, 0x000FA50C]}
death_road = {0x30: 0x000FA5C4}
death_garden = {0x2F: 0x000FA5C6}
float_zone = {0x31: [0x000FA5D4, 0x000FA5D0]}
aqua_tank = {0x32: 0x000FA5D8}
aquaway = {0x33: 0x000FA7A0}
nitros_3 = {0x58: 0x000FA5E0}

# w3 a3
hard_coaster = {0x35: 0x000FA768}
dark_maze = {0x36: 0x000FA5E8}
mad_coaster = {0x37: 0x000FA600}
move_stone = {0x38: 0x000FA604}
bolban_1 = {0x39: 0x000FA608}

# w4 a1
hopper_land = {0x3D: 0x000FA770}
jun_falls = {0x3C: 0x000FA61C}
cool_cave = {0x3E: 0x000FA61A}
freeze_lake = {0x3B: 0x000FA618}

# w4 a2
snow_land = {0x40: [0x000FA620, 0x000FA614]}
storm_valley = {0x41: 0x000FA628}
snow_circuit = {0x4A: 0x000FA62C}
heaven_sky = {0x43: 0x000FA654}
eye_snake = {0x42: 0x000FA634}
nitros_4 = {0x59: 0x000FA630}

# w4 a3
air_room = {0x44: 0x000FA7A4}
zero_g_room = {0x46: 0x000FA640}
mirror_room = {0x47: 0x000FA644}
natia_1 = {0x5A: 0x000FA6EA}

# w5
endol_2 = {0x4C: 0x000FA788}
baruda_2 = {0x4D: 0x000FA65C}
cronus = {0x4E: 0x000FA660}
nitros_5 = {0x4F: 0x000FA664}
bolban_2 = {0x50: 0x000FA7B4}
natia_2 = {0x51: 0x000FA66C}
bagular = {0x52: 0x000FA670}

# Holds maps that have two exits
two_exits = [hyper_room, red_cave, erars_lake, water_pool, magma_dam, jun_falls]

# Holds maps that come immediately after two exit stages
after_two_exits = [
    heavy_room,
    secret_room,
    dark_wood,
    big_cannon,
    waterway,
    water_slider,
    warp_room,
    millian_road,
    crysta_hole,
    emerald_tube,
    death_road,
    death_garden,
    cool_cave,
    freeze_lake,
]

# Holds maps that come two stages after two exit stages (These have two possible entrances and therefore two rom addresses)
has_two_rom_addresses = [
    sky_room,
    dragon_road,
    rockin_road,
    dark_prison,
    float_zone,
    snow_land,
]

# Maps to not swap temporarily
# TODO: Figure out how to shuffle
do_not_swap = [death_temple]

# Collection of all stages in the game (except for World 6, Unused, Bonus, and Secret Stages)
maps = [
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
    groog_hills,
    bubble_hole,
    erars_lake,
    waterway,
    water_slider,
    rockin_road,
    water_pool,
    warp_room,
    millian_road,
    dark_prison,
    nitros_2,
    killer_gate,
    spiral_tower,
    snake_route,
    baruda_1,
    hades_crater,
    magma_lake,
    magma_dam,
    crysta_hole,
    emerald_tube,
    death_temple,
    death_road,
    death_garden,
    float_zone,
    aqua_tank,
    aquaway,
    nitros_3,
    hard_coaster,
    dark_maze,
    mad_coaster,
    move_stone,
    bolban_1,
    hopper_land,
    jun_falls,
    cool_cave,
    freeze_lake,
    snow_land,
    storm_valley,
    snow_circuit,
    heaven_sky,
    eye_snake,
    nitros_4,
    air_room,
    zero_g_room,
    mirror_room,
    natia_1,
    endol_2,
    baruda_2,
    cronus,
    nitros_5,
    bolban_2,
    natia_2,
    bagular,
]

# Temporary list of all maps that keeps track of which levels haven't been randomized yet
maps_temp = maps.copy()
