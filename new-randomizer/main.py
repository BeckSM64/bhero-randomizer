import random

def replace_map_pointer_element(base_address, original_id, replacement_id, file_array):

    # This index is the base rom address of what's being replaced
    index = base_address + (replacement_id * 4)
    bytes_grabbed = file_array[index:index + 4]
    index_to_replace = base_address + (original_id * 4)

    # Insert the value into the byte array at the specific index
    file_array = file_array[:index_to_replace] + bytes_grabbed + file_array[index_to_replace + 4:]

    # return the file array
    return file_array

def main():
    
    # List of map ids in the game, only the ones that will be swapped
    map_ids = [
        # 0x00, # Battle Room entrance
        # 0x01, # Battle Room elevator
        0x02, # Battle Room
        0x03, # Hyper Room
        0x04, # Heavy Room
        0x05, # Sky Room
        0x06, # Secret Room
        # 0x07, # Cutscene
        0x08, # Emerald Tube
        0x09, # Blue Cave
        0x0A, # Hole Lake
        0x0B, # Red Cave
        0x0C, # Dark Wood
        0x0D, # Big Cannon
        0x0E, # Dragon Road
        0x0F, # Nitros 1
        0x10, # Clown Valley
        0x11, # Great Rock
        0x12, # Fog Route
        0x13, # Endol 1
        # 0x14, # Cutscene
        0x15, # Groog Hills
        0x16, # Bubble Hole
        0x17, # Erars Lake 1
        0x18, # Waterway
        0x19, # Waterslider
        # 0x1A, # Cutscene
        0x1B, # Waterpool
        0x1C, # Rockin Road
        0x1D, # Dark Prison
        0x1E, # Warp Room
        0x1F, # Millian Road
        # 0x20, # Cutscene
        0x21, # Killer Gate
        0x22, # Spiral Tower
        0x23, # Snake Route
        # 0x24, # Baruda Cutscene
        0x25, # Baruda
        # 0x26, # Hades Crater Cutscene
        0x27, # Hades Crater
        0x28, # Magma Lake
        0x29, # Magma Dam
        0x2A, # Crysta Hole
        # 0x2B, # Secret Level 1
        # 0x2C, # Cutscene
        0x2D, # Death Temple
        # 0x2E, # Death Road 2
        0x2F, # Death Garden
        0x30, # Death Road 1
        0x31, # Float Zone
        0x32, # Aqua tank
        0x33, # Aquaway
        # 0x34, # Cutscene
        0x35, # Hard Coaster
        0x36, # Dark Maze
        0x37, # Mad Coaster
        0x38, # Move Stone
        0x39, # Bolban 1
        # 0x3A, # Cutscene
        0x3B, # Freeze Lake
        0x3C, # Jun Falls
        0x3D, # Hopper Land
        0x3E, # Cool Cave
        # 0x3F, # Snowland Cutscene
        0x40, # Snowland
        0x41, # Storm Valley
        0x42, # Eye Snake
        0x43, # Heaven Sky
        0x44, # Air Room Select
        0x45, # Air Room
        0x46, # Zero G Room
        0x47, # Mirror Room
        # 0x48, # Nitros 4 After Cutscene
        # 0x49, # Secret Level 2
        0x4A, # Snow Circuit
        # 0x4B, # Cutscene
        0x4C, # Endol 2
        0x4D, # Baruda
        0x4E, # Cronus
        0x4F, # Nitros 5
        0x50, # Bolban 2
        0x51, # Natia 2
        0x52, # Bagular
        0x53, # Bagular Phase 3
        # 0x54, # Secret Level 3
        0x55, # Evil Bomber
        # 0x56, # Cutscene
        0x57, # Nitros 2
        0x58, # Nitros 3
        0x59, # Nitros 4
        0x5A, # Natia 1
        # 0x5B, # Cutscene
        # 0x5C, # Aquaway In Fish
        # 0x5D, # Erars 2
        # 0x5E, # Erars 3
        # 0x5F, # Heaven Sky 2
        # 0x60, # Fly Test Stage
        # 0x61, # Bonus Stage
        # 0x62, # Bonus Stage
        # 0x63, # Bonus Stage
        # 0x64, # Bonus Stage
        # 0x65, # Bonus Stage/Unused Stage
        0x66, # Outer Road
        0x67, # Inner Road
        # 0x68, # Groog Hills 2
        0x69, # Zero G Entrance
        0x6A, # Mirror Room Entrance
        0x6B, # Natia 1 Entrance
        0x6C  # Bagular Phase 2
    ]

    # Create the dictionary of what the levels will change to
    map_ids_2 = map_ids.copy()
    random.shuffle(map_ids_2)

    map_to_map_dict = {}
    for i, map_id in enumerate(map_ids):
        map_to_map_dict[map_id] = map_ids_2[i]

    # TODO: Remove print for debug
    for key, value in map_to_map_dict.items():
        print(f"Map ID {hex(key)} becomes {hex(value)}")

    # ROM Address of map pointer array
    map_pointer_array_rom_address = 0x00FA758 # RAM: 0x80108238

    # ROM Address of object pointer array
    object_pointer_array_rom_address = 0x000FE150 # RAM: 0x8010BC30

    # ROM Address of level details pointer array
    level_details_pointer_array_rom_address = 0x000FD91C # RAM: 0x8010BC30

    # The path to the ROM
    # TODO: DO error handling for this file open
    file_path = "Bomberman Hero (USA).z64"
    with open(file_path, "rb") as f:

        # Read in the file as a byte array
        file_array = bytearray(f.read())

        # Make a copy so we have an unmodified version to grab values from
        file_array_unmodified = file_array.copy()

        # Iterate over every key value pair in the dict
        # in order to replace levels
        for key, value in map_to_map_dict.items():

            # 1. Change map pointer
            file_array = replace_map_pointer_element(map_pointer_array_rom_address, key, value, file_array)

            # 2. Change objects pointer
            file_array = replace_map_pointer_element(object_pointer_array_rom_address, key, value, file_array)

            # 0x38 is the struct size, multiplied by map id we want for the offset
            original_level_detail_index = 0x000FAF1C + (key * 0x38)
            # print("ORIGINAL VALUE: " + hex(original_level_detail_index))

            # Get original level select value
            original_level_select_value = file_array_unmodified[original_level_detail_index:original_level_detail_index + 4]
            # print("Original Level Select: ", original_level_select_value)

            replace_this_level_detail_index = 0x000FAF1C + (value * 0x38)
            # print("OVERWRITE HERE", hex(replace_this_level_detail_index))

            # 5. change unk00 -> Level select of original level
            file_array = file_array[:replace_this_level_detail_index] + original_level_select_value + file_array[replace_this_level_detail_index + 4:]

            # 6. change unk08 -> Address of level after original level
            original_next_level_pointer = file_array_unmodified[(original_level_detail_index + 8):(original_level_detail_index + 8) + 4]
            file_array = file_array[:(replace_this_level_detail_index + 8)] + original_next_level_pointer + file_array[(replace_this_level_detail_index + 8) + 4:]

            # 3. Change level details pointer
            file_array = replace_map_pointer_element(level_details_pointer_array_rom_address, key, value, file_array)

    # New randomized file
    new_file = "rando.z64"
    with open(new_file, "wb") as f:
        f.write(file_array)

if __name__=="__main__":
    main()
