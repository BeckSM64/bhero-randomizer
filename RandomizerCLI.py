import sys
import random
import argparse
from RomData import *
from BheroRandomizer import *

class RandomizerCLI:
    def __init__(self):

        parser = argparse.ArgumentParser()
        parser.add_argument("input_rom", help="The clean Bomberman Hero ROM", type=str)
        parser.add_argument("output_dir", help="The directory to place the generated ROM. Output ROM will be named <input_rom>.rando.z64", type=str)
        parser.add_argument("--seed", help="A specified seed used to generate the ROM", type=int)
        args = parser.parse_args()
        
        # generate seed
        seed = random.randint(0, 1000000)

        # overwrite seed if provided via command line arg
        if args.seed is not None:
            seed = args.seed

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
