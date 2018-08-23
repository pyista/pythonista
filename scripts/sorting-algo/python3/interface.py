from os import system
from utility import create_custom_list, generate_random_list, parse_non_int

# -- Text Prompt and Interfaces


def first_greet() -> None:
    system('clear')
    print("Welcome to Sorting Algorithm Visualizer ! Created By : wowotek\nTested on Linux ")


def tutorial(clear=False) -> None:
    if clear:
        system('clear')
    print("Tutorial :")
    print("   Before you can view how sorting works, you")
    print("   Need to generate or configure your own list")
    print("   You can do this by choosing Menu 1 first")
    print("   ")
    print("   After you done configuring or generating")
    print("   your own List, now you can Sort it using")
    print("   Menu 2")


def main_menu(first_opened: bool, list_showcase: list) -> int:
    system('clear')
    if first_opened:
        first_greet()
        print()
        tutorial()
        print()
    print(" [ WARNING : THIS APP CONTAIN FLASHING, AND BLINKING SCREEN ! ]")
    print("                  USE WITH YOUR OWN CAUTION !\n")
    print("--- > Main Menu < ---")
    print("1. Create List")
    print("2. Sort : Selection Sort")
    print("X. Sort : Quick Sort [Not Implemented]")
    print("X. Sort : Heap Sort [Not Implemented]")
    print("3. Tutorial")
    print("0. Exit")

    if list_showcase is not None:
        print("   Your List : {}".format(list_showcase))

    return int(input("\nSelect Your Choice : "))


def create_list_submenu() -> int:
    system('clear')
    print("--- > Create List < ---")
    print("1. Custom List")
    print("2. Random List")
    print("0. Back")

    return int(input("\nSelect Your Choice : "))


def ask_custom_list() -> list:
    system('clear')
    print("--- > Custom List Creator < ---")
    print("Please input your own desired list")
    print("every integer should be separated by " " (whitespace)")
    print("ex:")
    print("1 2 3 4 5 6 7 9 0")
    print("367 1928 8 28 90 894")

    return create_custom_list(str(input("\nYour List : ")))


def ask_random_list() -> list:
    system('clear')
    print("---> Random List Configurator < ---")
    print("Please specify your list requirements")
    list_length = parse_non_int(
        str(input("   Length of List (default=40)  : ")))[0]
    min_num = parse_non_int(
        str(input("   Minimal Number (default=1)   : ")))[0]
    max_num = parse_non_int(
        str(input("   Maximal Number (default=20)  : ")))[0]
    random_iteration = parse_non_int(
        str(input("Random Multiplier (default=100) : ")))[0]
    print("Generating List...")
    generated_list = generate_random_list(
        list_length, min_num, max_num, random_iteration)
    print("Generated List :\n{}".format(generated_list))
    input("Press Enter to Continue ")

    return generated_list
