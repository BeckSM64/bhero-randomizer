import sys
import random
import subprocess
import os.path
from RomData import *
from BheroRandomizer import *
from RandomizerGUI import RandomizerGUI


def main():

    # tools
    n64converter = "N64RomConverter.py"
    n64checksum = "n64cksum.py"

    if len(sys.argv) <= 1:
        RandomizerGUI()

    else:
        
        # generate seed
        seed = random.randint(0, 1000000)

        # get file as input
        input_name = sys.argv[1]

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

        # generate the new level order dictionary
        generate_rom(input_name, ".", seed)

        # print success
        print("Seed: " + str(seed))


if __name__ == "__main__":
    main()
