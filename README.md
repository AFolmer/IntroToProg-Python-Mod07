# IntroToProg-Python-Mod07
Mod 7 project: Exceptions and pickles

## Files
This repository includes two files: the code for mod 7 and a starter file with monsters and characters already loaded, game_parameter_pickle.dat.

## Purpose
The purpose of this program is to use functions, exceptions, and pickles to allow the user to manage two dictionaries supporting a game:
 - Monsters:  each monster has a name (str) and a stat list (int) of hit points, attack, and dexterity
 - Characters: each character has a name (str), character type (str), and a stat list (int) of willpower, intellect, combat, agility, and money

## Code Overview
The program begins by opening a pickle with the two dictionaries.  If the program encounters an exception, it assumes that the pickle needs to be created and defines the two dictionaries used in the program.  The user then has a choice of editing the character dictionary, monster dictionary, or saving and exiting the program.
Within each dictionary menu the user has a choice of printing, adding, editing, or removing dictionary pairs.  Each dictionary is structured with the name as the key, then the definition is a list of stats.  Once the dictionaries have been created and saved, they can be used by other programs to run text based games.

## Pickles
In python, the pickle function is used to store multiple objects from your code into one file.  There are two major advantages to doing this:
 - You no longer have to convert lists, tuples, dictionaries, etc. into comma/tab/etc. separated values in a text file and back out again
 - All objects are saved to the pickle together, reducing the risk of forgetting to save/move a file
The first action in this program is to import pickle functionality.

![Screenshot of code to enable pickle functions](https://github.com/CaseNightmareGreen/IntroToProg-Python-Mod07/assets/132308533/b84e7f53-7763-4a9f-8a70-ab545063bcd4)
### Figure 1: Code to enable pickle functions

Next, the program attempts to open the file. On line 180 the program tries to open the pickle using open("filename.dat", "rb") and load the two dictionaries using the pickle.load() function.  If the program enounters an error, "except: " on line 185, it creates the two dictionaries character and monster to edit and then save as a new pickle at the end of the program.

![Screenshot of code to open pickle, or create dictionaries if pickle cannot be opened](https://github.com/CaseNightmareGreen/IntroToProg-Python-Mod07/assets/132308533/7a0336c3-3a02-44b6-8ffd-a896bc2d3a07)
### Figure 2: Code to open pickle, or create dictionaries if pickle cannot be opened

Finally, the program ends with the pickle file being opened or created using open("filename.dat", "wb") (line 302), the two dictionaries being pickled using pickle.dump() (lines 304 and 305) and the pickle closed, f.close (line 307).

![Screenshot of code to pickle and save dictionaries](https://github.com/CaseNightmareGreen/IntroToProg-Python-Mod07/assets/132308533/884947e8-ad29-4805-bf4e-8fdc79b43d8e)
### Figure 3: Code to pickle and save dictionaries

## Classes, Functions, and Exceptions
The next programming topic introduced in this module is exception handling.  In python the programmer has the ability to provide custom responses to predicted user errors and  a general response to unexpected user errors using try > except > else as seen in Figure 4.  The most important difference between try/except and if/else is that an error within an if/else tree will cause the program to terminate, but a try/except will provide an alternative path to start over or continute so that progress is not lost.  There are several examples within the program, but the best is function IO.enter_stat_int()

![Code for function enter_stat_int()](https://github.com/CaseNightmareGreen/IntroToProg-Python-Mod07/assets/132308533/d2beb9ac-0ad7-4f8d-b1ef-d8a832d04fdb)
### Figure 4: Code for IO.enter_stat_int() to enter stats as an integer using try except and if else to catch errors

The function enter_stat_int() is assigned to the class IO and tagged as @staticmethod (lines 23 - 26) as it does not rely on it's class, IO is a decorator to identify what the function does when it is used in the program. The function is structured as:
 - while loop that does not break until the user has entered a value that meets all conditions (line 30)
 - try to check that user has entered an integer (lines 32 - 33)
 - except Value Error to notify user if they enter an invalid type e.g. string or float (lines 35 - 36)
 - except any other kind of error an inventive user can come up with (lines 38 - 39)
 - else if the try does not result in any errors a final if/else (lines 41 - 45) checks that the user entered integer is between the min and max values defined for the program (lines 17 - 18) and returns a final variable stat (line 47)

## Conclusion
In this module I continued to build on classes and functions developed in module 6 by adding exception handling and pickling to create a stronger program that is less likely to break and allows me to handle multiple lists/dictionaries/tuples/etc.  These features will be used in future programs to code games with multiple input files played by chaos muppets who don't like following directions.
