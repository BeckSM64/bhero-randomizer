import sys
import random
import argparse
from RomData import *
from BheroRandomizer import *
from RandomizerGUI import RandomizerGUI


def main():

    if len(sys.argv) <= 1:
        RandomizerGUI()

    else:

        parser = argparse.ArgumentParser()
        parser.add_argument("input_rom", help="The clean Bomberman Hero ROM", type=str)
        parser.add_argument("output_dir", help="The directory to place the generated ROM", type=str)
        args = parser.parse_args()
        
        # generate seed
        seed = random.randint(0, 1000000)

        # get file as input
        input_name = args.input_rom

        # get output dir
        output_dir = args.output_dir

        # check file extension
        if ".n64" not in input_name:
            sys.exit("Invalid input file. Make sure the file extension is .n64")

        # generate the new level order dictionary
        generate_rom(input_name, output_dir, seed)

        # print success
        print("Seed: " + str(seed))


if __name__ == "__main__":
    main()
