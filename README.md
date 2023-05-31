# IntroToProg-Python-Mod07
Mod 7 project: exceptions and pickles

## Files
This repository includes two files: the code for mod 7 and a starter file with monsters and characters already loaded, game_parameter_pickle.dat

## Purpose
The purpose of this program is to use functions, exceptions, and pickles to allow the user to manage two dictionaries supporting a game:
 - Monsters:  each monster has a name (str) and a stat list (int) of hit points, attack, and dexterity
 - Characters: each character has a name (str), character type (str), and a stat list (int) of willpower, intellect, combat, agility, and money
## Code Overview
The program begins by opening a pickle with the two dictionaries.  If the program encounters an exception, it assumes that the pickle needs to be created and defining the two dictionaries.  The user then has a choice of editing the character dictionary, monster dictionary, or saving and exiting the program.
Within each dictionary menu the user has a choice of printing current entries, adding entries, editing current entries, or removing entries.  Each dictionary is structured with the name as the key, then the definition is a list of stats.  Once the dictionaries have been created, they can be used by other programs to run text based games.
