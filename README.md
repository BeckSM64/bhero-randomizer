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

## Run Via the Command Line
1. You will need to have Python3 installed
2. Clone this repository or download the zip  
   ```python
   git clone https://github.com/BeckSM64/bhero-randomizer.git
   ```
3. You will also need a Bomberman Hero ROM (JP Version) which I cannot, and will not, supply. But I have faith in your abilities to find one :)
4. From the directory where you cloned the project, run this command:  
   ```python
   python3 Main.py <input_file>
   ```
5. Alternatively, you can run without arguments to launch the GUI version of the application:
   ```python
   python3 Main.py
   ```
6. Whichever method you choose will generate a .z64 ROM file in the same directory which you can run on emulator or console using an Everdrive :D

# Credits
Thanks to the following people for developing tools that made my life 1000x easier:  
**masl123** for n64RomConverter: https://github.com/masl123/n64RomConverter  
**dkosmari** for n64chksum.py: https://gist.github.com/dkosmari/ee7bb471ea12c21b008d0ecffebd6384

# Questions
If you have questions, you can contact me directly  
Email: BeckSM64@gmail.com  
Discord: Beck#9214