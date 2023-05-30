# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Exception handling and pickling,
#              When the program starts open a pickle file with two dictionaries,
#              characters and monsters.  User navigates main menu and character
#               /monster sub menus to view, add, edit, and remove dictionary
#               entries and then save changes back to the pickle.
# ChangeLog (Who,When,What):
# AFolmer,5.29.2023,Created initial script
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Import the pickle functions
import pickle

# Declare variables and constants
int_stat_min = 1  # Minimum value for integer stats
int_stat_max = 10  # Maximum value for integer stats
menu_choice = int  # Integer variable used to capture user menu choice


# Inputs and Outputs ------------------------------------------------------------------#
class IO:
    """  Performs Input and Output tasks"""
    @staticmethod
    def enter_stat_int():
        """ Gets statistic value from user
        :return: integer
        """
        while True:
            # User inputs statistic value
            try:
                stat = int(input("Enter a value between " + str(int_stat_min) + " and " + str(int_stat_max) + ". "))
            # User notified of error if input is not an integer
            except ValueError:
                print("Value must be an integer.")
            # User notified if they generate any other type of error
            except:
                print("Unknown error.")
            # Check to ensure that input is within stat min and max values
            else:
                if int_stat_min <= stat <= int_stat_max:
                    break
                else:
                    print("Value outside of stat parameters.")
        # Stat value returned
        return stat

    @staticmethod
    def print_main_menu():
        """ Prints the list of menu items in the main menu
        :return: nothing"""
        print("Main Menu \n"
              "1. Edit characters \n"
              "2. Edit monsters \n"
              "3. Save and exit \n"
              "\n")

    @staticmethod
    def print_monster_menu():
        """Prints the list of menu items for monsters
        :return: nothing"""
        print("Monster Menu \n"
              "1. Print monster list \n"
              "2. Add monsters \n"
              "3. Edit monsters \n"
              "4. Remove monsters \n"
              "5. Exit monsters \n")

    @staticmethod
    def print_character_menu():
        """ Prints the list of menu items for characters
        :return: nothing"""
        print("Character Menu \n"
              "1. Print character list \n"
              "2. Add characters \n"
              "3. Edit characters \n"
              "4. Remove characters \n"
              "5. Exit characters \n")

    @staticmethod
    def input_menu_choice(upper):
        """ User inputs menu choice
        :param upper: Max value menu choice for the menu
        :return: integer choice"""
        while True:
            # User inputs menu choice
            try:
                choice = int(input("What would you like to do? "))
            # User notified if choice is not an integer
            except ValueError:
                print("Choice must be an integer.")
            # User notified if they make any other type of error
            except:
                print("Unknown error.")
            # Check to ensure user entered valid menu choice
            else:
                if 1 <= choice <= upper:
                    break
                else:
                    print("Invalid menu choice.")
        return choice


# Edit Character Dictionary -----------------------------------------------------------------#
class Character:
    """ Performs character dictionary editing tasks"""
    @staticmethod
    def change_character_stats():
        """Change character statistics
        :return: list of character statistics"""
        while True:
            character_type = input("Character type: ")
            if len(character_type) <= 50:
                break
            else:
                print("Length restricted to 50 characters.")
        print("Willpower: ")
        willpower = IO.enter_stat_int()
        print("Intellect: ")
        intellect = IO.enter_stat_int()
        print("Combat: ")
        combat = IO.enter_stat_int()
        print("Agility: ")
        agility = IO.enter_stat_int()
        print("Starting Money: $")
        money = IO.enter_stat_int()
        stat_list = character_type, willpower, intellect, combat, agility, money
        return stat_list

    @staticmethod
    def print_characters():
        """ Print list of characters
        :return: nothing"""
        if len(character_dictionary) == 0:
            print("You don't have any characters")
        else:
            print("Willpower, Intellect, Combat, Agility, Money")
            for i in character_dictionary:
                stat_list = character_dictionary[i]
                # Print character name and description
                print(i.capitalize() + ": " + stat_list[0])
                print(stat_list[1:6])


# Edit Monster Dictionary -------------------------------------------------------------------#
class Monster:
    """ Performs monster dictionary editing tasks"""
    @staticmethod
    def change_monster_stats():
        """ Change monster statistics
        :return: list of monster statistics"""
        print("Hit points: ")
        hit_points = IO.enter_stat_int()
        print("Attack: ")
        attack = IO.enter_stat_int()
        print("Dexterity: ")
        dexterity = IO.enter_stat_int()
        # Turns hit points, attack, and dexterity into a list
        stat_list = hit_points, attack, dexterity
        return stat_list

    @staticmethod
    def print_monsters():
        """ Print list of monsters
        :return: nothing """
        if len(monster_dictionary) == 0:
            print("You have no monsters.")
        else:
            print("Hit Points, Attack, Dexterity")
            for i in monster_dictionary:
                stat_list = monster_dictionary[i]
                print(i.capitalize())
                print(stat_list)


# Main body of script
# Open the pickle in read mode and extract monster and character dictionaries
try:
    f = open("game_parameter_pickle.dat", "rb")
    character_dictionary = pickle.load(f)
    monster_dictionary = pickle.load(f)
    f.close()
# If the file isn't found or there is an extraction error, notify user and create new dictionaries
except:
    print("Game file not found; creating new file.")
    character_dictionary = {}
    monster_dictionary = {}

# Main menu
while True:
    IO.print_main_menu()
    # menu_choice function used throughout the program to ensure that the user enters a valid integer
    # parameter "upper" is used to ensure that user choice matches valid menu option
    menu_choice = IO.input_menu_choice(upper=4)

    # User decides to edit characters
    if menu_choice == 1:
        while True:
            IO.print_character_menu()
            menu_choice = IO.input_menu_choice(upper=5)

            # View characters, message to user if character dictionary is empty
            if menu_choice == 1:
                Character.print_characters()

            # Add characters
            elif menu_choice == 2:
                character_name = input("What is your character's name? ")
                character_name = character_name.lower()
                # Message to let user know if character is already in dictionary
                if character_name in character_dictionary:
                    print("Character already in dictionary.")
                # Use function to input character stats and save to character in dictionary
                else:
                    character_stats = Character.change_character_stats()
                    character_dictionary[character_name] = character_stats
                    print(character_name + " added.")

            # Edit characters
            elif menu_choice == 3:
                character_name = input("Which character would you like to edit? ")
                character_name = character_name.lower()
                # Use function to input new character stats and save to character in dictionary
                if character_name in character_dictionary:
                    character_stats = Character.change_character_stats()
                    character_dictionary[character_name] = character_stats
                    print(character_name + " updated.")
                # Message to let user know if character not in dictionary
                else:
                    print("Character not found.")

            # Remove characters
            elif menu_choice == 4:
                character_name = input("Which character would you like to remove? ")
                character_name = character_name.lower()
                # Remove character from dictionary
                if character_name in character_dictionary:
                    del character_dictionary[character_name]
                    print(character_name + " removed.")
                # Message to let user know if character not in dictionary
                else:
                    print("Character not found.")

            # Exit character menu
            else:
                break

    # User decides to edit monsters
    elif menu_choice == 2:
        while True:
            IO.print_monster_menu()
            menu_choice = IO.input_menu_choice(upper=5)

            # View monsters, message to user if monster dictionary is empty
            if menu_choice == 1:
                Monster.print_monsters()

            # Add monsters
            elif menu_choice == 2:
                monster_name = input("What is your new monster's name? ")
                monster_name = monster_name.lower()
                # Notify user if monster is already in dictionary
                if monster_name in monster_dictionary:
                    print("Monster already in dictionary.")
                # Use function to capture monster stats and save to monster in dictionary
                else:
                    monster_stats = Monster.change_monster_stats()
                    monster_dictionary[monster_name] = monster_stats
                    print(monster_name + " added.")

            # Edit monsters
            elif menu_choice == 3:
                monster_name = input("Which monster would you like to edit? ")
                monster_name = monster_name.lower()
                # Function to enter new stats and save to monster in dictionary
                if monster_name in monster_dictionary:
                    monster_stats = Monster.change_monster_stats()
                    print(monster_name + " updated.")
                # Notify user that monster not found
                    print("Monster not found.")

            # Remove monsters
            elif menu_choice == 4:
                monster_name = input("Which monster would you like to remove?")
                monster_name = monster_name.lower()
                # Remove monster from dictionary
                if monster_name in monster_dictionary:
                    del monster_dictionary[monster_name]
                    print(monster_name + " removed.")
                # Notify user if monster not in dictionary
                else:
                    print("Monster not found.")

            # Exit monsters
            else:
                break

    # Save dictionaries to pickle and exit
    elif menu_choice == 3:
        # Open the game parameter pickle file in write mode
        f = open("game_parameter_pickle.dat", "wb")
        # Save character and monster dictionaries to pickle file
        pickle.dump(character_dictionary, f)
        pickle.dump(monster_dictionary, f)
        # Close pickle file
        f.close()
        print("Updated game parameters saved.")
        break
    else:
        print("Goodbye!")
        break
