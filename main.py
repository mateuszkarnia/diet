import os
import time
import math
import shutil
import data_manager
import sys

class color:
   PURPLE = '\033[95m0'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def print_menu(menu, upper):
    columns = shutil.get_terminal_size().columns
    for option in range(len(menu)):
        if option == upper:
            print(color.BOLD + color.RED + menu[option].upper().center(columns) + color.END)
        else:
            print(menu[option].center(columns))


def get_input():
    options_to_chose = ['Add food and callories what you eat.', 'Add excersise and callories burning', 'Show list of food.',
                        'Show list of excersises.', 'Exit\n', "Press 'ENTER' to choose"]
    current = 0
    pressedkey = ''
    os.system('clear')
    while pressedkey.lower() != 'e':
        os.system('clear')
        print_menu(options_to_chose, current)
        pressedkey = getch()

        if pressedkey.lower() == 'w':
            if current > 0:
                current -= 1
        elif pressedkey.lower() == 's':
            if current < 8:
                current += 1
    return current


def pause():
    columns = shutil.get_terminal_size().columns
    print('\n')
    print('Press any key to display a menu.'.center(columns))
    next_step = getch()


def introduction_screen():
    os.system('clear')
    columns = shutil.get_terminal_size().columns

    print(" <}\\".center(columns))
    print("      .--\--.".center(columns))
    print("     /   `   \\".center(columns))
    print("     |       |".center(columns))
    print("      \     /".center(columns))
    print("      '-'-'".center(columns))
    pause()


def run_function(current_choice):
    choice = current_choice


    if choice == 0:
        dict_of_food = {}
        data_manager.add_food(dict_of_food)
    elif choice == 1:
        dict_of_excersises = {}
        data_manager.add_excersise(dict_of_excersises)
    elif choice == 2:
        dict_of_food = {}
        data_manager.show_list_of_food()
        x = data_manager.import_file(filename='food.txt')
        value = data_manager.calculate(x)
        data_manager.check(value)
        pause()
    elif choice == 3:
        dict_of_excersises = {}
        data_manager.show_list_of_excersises()
        x = data_manager.import_file(filename='excersises.txt')
        value = data_manager.calculate(x)
        data_manager.check(value)
        pause()

    elif choice == 4:
        sys.exit()

def main():
    while 1:
        run_function(get_input())


if __name__ == '__main__':
    introduction_screen()
    main()
