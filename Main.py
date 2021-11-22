import sys
from Rando.RandomizerGUI import RandomizerGUI
from Rando.RandomizerCLI import RandomizerCLI


def main():

    # Run GUI by default
    if len(sys.argv) <= 1:
        RandomizerGUI()

    # If args provided, running CLI
    else:
        RandomizerCLI()


if __name__ == "__main__":
    main()
