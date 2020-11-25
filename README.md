# Bomberman Hero Level Randomizer
This is a script which will generate a ROM image of Bomberman Hero with randomized levels. This is currently a work in progress and is by no means complete.

## Known Issues
Currently there are several issues. As previously stated, this project is a work in progress. The hope is that some cool people from the Bhero community will help me test this as I haven't really tested it all too much as of now. But yeah, current issues are as follows:
1. I don't think it's actually possible to beat the game currently (unless you happen to get lucky and Bagular is one of the levels that loads before the game breaks)
2. There seem to be problems with circular dependencies (ie. You load a level, then another level, then it kicks you back to the first level you laoded). I haven't looked into this much yet, it's the next thing I'll tackle, but if you can think of a fix for this, please feel free to let me know.
3. If you move the joystick up or down while on the level select screen in planets you weren't supposed to have yet unlocked you may crash the game. You have been warned.

## Usage
In order to run this application, you will need to do the following:
1. You will need to have Python 3 and Java installed
2. Clone this repository or download the zip        git clone https://github.com/BeckSM64/bhero-randomizer.git
3. Ensure you have N64Converter.jar in the same directory that you cloned the project to. Can be found here: https://github.com/masl123/n64RomConverter/tree/master/release
4. Ensure you have n64cksum.py in the same directory that you cloned the project to. Can be found here: https://gist.github.com/dkosmari/ee7bb471ea12c21b008d0ecffebd6384
5. You will also need a Bomberman Hero ROM (JP Version) which I cannot, and will not, supply. But I have faith in your abilities to find one :)
6. From the directory where you cloned the project, run this command:       python3 bherorandomizer.py <input file>
7. This will generate a .z64 ROM file in the same directory which you can run on emulator or console using an Everdrive :D

# Credits
Special thanks to the following people for developing tools that made my life 1000x easier:
masl123 for n64RomConverter: https://github.com/masl123/n64RomConverter
dkosmari for n64chksum.py: https://gist.github.com/dkosmari/ee7bb471ea12c21b008d0ecffebd6384

## Questions
If you have questions, you can contact me directly
Email: BeckSM64@gmail.com
Discord: Beck#9214