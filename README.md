# Keystroke Counter

## What does it do?
This program takes in text files put in the `txts` directory and generates a keyboard-shaped heatmap out of which keystrokes it took to type the file.

## How do I run it?
1. Run `git clone https://EthanTock/keystroke_counter <directory>`, with `<directory>` being the directory you want to clone this code into.
2. Put the text file you wish to generate a heatmap out of into the `txts` directory.
3. From your defined `<directory>`, run main.py.

Then you just have to follow the instructions in the command-line!  

## How do I read the heatmap?
For each key, the bolder the its color on the heatmap, the more often it was pressed.  
The list below the keyboard heatmap displays the keys pressed descending by order of frequency, then how many times it was pressed, its frequency relative to the most pressed key, and its frequency relative to the total.  
If you enabled shift press tracking, each time the shift key was used in the creation of a character (ex. Shift + q = Q), a shift press will be counted.
