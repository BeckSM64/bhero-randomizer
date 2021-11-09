# Bomberman Hero Level Randomizer
This is a script which will generate a ROM image of Bomberman Hero with randomized stages. This is currently a work in progress and is actively being updated.

## Known Issues
1. This only works with the Japanese version of the ROM currently. I may work on US in the future if there is any interest.
2. Stages that come after two exit stages have been left untouched for now while I work out the logic to swap them with other stages.
3. Stages that come two stages after a stage with two exits have two rom address. For now, they are only being swapped with other stages that are two stages after two exit stages while I work out how to deal with this.
4. The last world (Gossick) was left untouched for now.
5. I removed the assembly instruction which is responsible for marking stages as complete. I did this as a temporary fix to get around some other issues I was running into. As a result, stages that were completed won't be marked with a 1-5 on the stage select screen, and you won't be able to navigate between planets or areas, even if you completed all stages.

## Usage
In order to run this application, you will need to do the following:
1. You will need to have Python3 installed
2. Clone this repository or download the zip  
   `git clone https://github.com/BeckSM64/bhero-randomizer.git`
3. Ensure you have n64cksum.py in the same directory that you cloned the project to. Can be found here:  
   https://gist.github.com/dkosmari/ee7bb471ea12c21b008d0ecffebd6384
4. You will also need a Bomberman Hero ROM (JP Version) which I cannot, and will not, supply. But I have faith in your abilities to find one :)
5. From the directory where you cloned the project, run this command:  
   `python3 bherorandomizer.py <input_file>`
6. This will generate a .z64 ROM file in the same directory which you can run on emulator or console using an Everdrive :D

## Credits
Thanks to the following people for developing tools that made my life 1000x easier:  
**masl123** for n64RomConverter: https://github.com/masl123/n64RomConverter  
**dkosmari** for n64chksum.py: https://gist.github.com/dkosmari/ee7bb471ea12c21b008d0ecffebd6384

## Questions
If you have questions, you can contact me directly  
Email: BeckSM64@gmail.com  
Discord: Beck#9214