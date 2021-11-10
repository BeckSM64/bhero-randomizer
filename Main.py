import sys
import random
import subprocess
import os.path
from RomData import *
from BheroRandomizer import *
from RandomizerGUI import RandomizerGUI


def main():

    gui = RandomizerGUI()

    # # tools
    # n64converter = "N64RomConverter.py"
    # n64checksum = "n64cksum.py"

    # # check number of args
    # if len(sys.argv) != 2:
    #     sys.exit(
    #         "Incorrect number of arguments. Usage: python3 bherorandomizer.py <input_file>"
    #     )

    # # get file as input
    # input_name = sys.argv[1]
    # output_name = input_name

    # # help
    # if (sys.argv[1] == "-h") or (sys.argv[1] == "-help"):
    #     sys.exit(
    #         "Input must be a Bomberman Hero ROM file with .n64 extension. \n Usage: python3 bherorandomizer.py <input_file>"
    #     )

    # # check file extension
    # if ".n64" not in input_name:
    #     sys.exit("Invalid input file. Make sure the file extension is .n64")

    # # ensure dependencies are in directory
    # if not os.path.exists(n64converter):
    #     sys.exit("Cannot locate " + n64converter + ". Exiting...")
    # if not os.path.exists(n64checksum):
    #     sys.exit("Cannot locate " + n64checksum + ". Exiting...")

    # # change file extension for ouput file
    # output_name = output_name.replace(".n64", ".z64")

    # # N64CONVERTER -i [INPUT] -o [OUTPUT]
    # subprocess.call(["python", n64converter, "-i", input_name, "-o", output_name])

    # # generate the new level order dictionary
    # randomize_stages()

    # # hold the bytes read in from the rom file
    # rom_data = read_file(output_name)

    # # write modified data back to rom
    # write_file(output_name, rom_data)

    # # recalculate checksum
    # subprocess.call(["python", n64checksum, output_name])

    # # print success
    # print("Success. Generated output file " + output_name + " in current directory")


if __name__ == "__main__":
    main()
