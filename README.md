# Bomberman Hero Level Randomizer
This is a script which will generate a ROM image of Bomberman Hero with randomized stages. This is currently a work in progress and is actively being updated.

# Notes
1. This only works with the Japanese version of the ROM currently. I may work on US in the future if there is any interest.
2. Battle Room will always be the first stage you play and Bagular will always be the last, for now.
3. Stages that come after two exit stages have been left untouched for now while I work out the logic to swap them with other stages.
4. Stages that come two stages after a stage with two exits have two rom address. For now, they are only being swapped with other stages that are two stages after two exit stages while I work out how to deal with this.
5. The last world (Gossick) was left untouched for now.
6. I removed the assembly instruction which is responsible for marking stages as complete. I did this as a temporary fix to get around some other issues I was running into. As a result, stages that were completed won't be marked with a 1-5 on the stage select screen, and you won't be able to navigate between planets or areas, even if you completed all stages.
7. When you load the game, you'll get a warning about a bad CRC, don't panic. On Everdrive, you can just press A and continue to the game as normal. On Project 64, you can hit OK, but you may have to resume the emulation as well, which should be bound to F2.

# Usage
In order to run this application, you will need to do one of the following:

## Run Via the Executable
You can go to the side of this page and click the latest release, and then download BombermanHeroRandomizer.exe. If you double click the executable that is downlaoded, you should see a GUI that looks like this:

   ![alt text](https://github.com/BeckSM64/bhero-randomizer/blob/main/Assets/bheroRandomizerGui.png?raw=true)

You will most likely get a warning about Windows not being able to verify the developer of the application. But don't worry, it was me. Then perform the following steps:
1. Simply click more info, run anyway, and you should be good to go
2. Now just click the new seed button, give the path to a fresh Bomberman Hero JP ROM, select an output directory, and click generate
3. If everything worked, this should generate a .z64 ROM file which you can run on emulator or console using an Everdrive :D

## Run Via the Command Line
An alternative method is to clone the project directly. To run this way, you will need to do the following:
1. You will need to have Python3 installed
2. Clone this repository or download the zip  
   ```python
   git clone https://github.com/BeckSM64/bhero-randomizer.git
   ```
3. You will also need a Bomberman Hero ROM (JP Version) which I cannot, and will not, supply. But I have faith in your abilities to find one :)
4. Usage:
   ```bash
   usage: Main.py [-h] [--seed SEED] input_rom output_dir

   positional arguments:
   input_rom    The clean Bomberman Hero ROM
   output_dir   The directory to place the generated ROM. Output ROM will be named <input_rom>.rando.z64

   optional arguments:
   -h, --help   show this help message and exit
   --seed SEED  A specified seed used to generate the ROM
   ```
5. Alternatively, you can run without arguments to launch the GUI version of the application:
   ```python
   python3 Main.py
   ```
6. If everything worked, you should have generated a .z64 file

# Credits
Thanks to

**masl123** for developing their n64RomConverter utility which helped me during testing: https://github.com/masl123/n64RomConverter

**dkosmari** for their n64chksum utility which helped me during testing: https://gist.github.com/dkosmari/ee7bb471ea12c21b008d0ecffebd6384

**Yashichi** for giving me permission to use his BomberMad FrankerFaceZ emote as the icon for the GUI: https://www.frankerfacez.com/emoticon/525967-BomberMad

# Questions
If you have questions, you can contact me directly  
Email: BeckSM64@gmail.com  
Discord: Beck#9214