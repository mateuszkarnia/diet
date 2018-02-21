import os
import time
import math
import shutil
import data_menager

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


def menu():
    options_to_chose = ['Add food and callories what you eat.', 'Add excersise and callories burning', 'Show list of food.',
                        'Show list of excersises.', 'Mark/unmark as done', 'Delete thing to do', 'Archive', 'Exit', 'Calculate calories\n', "Press 'ENTER' to choose"]
    current = 0
    pressedkey = ''
    os.system('clear')
    while pressedkey != 'e':
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


def run_functions(current_choice):
    choice = current_choice
    choice_1 = ""
    marked = "X"
    unmarked = " "

    dict_of_food = {}
    dict_of_excersises = {}

    # print("\n[1] - Add food and callories what you eat.")
    # print("[2] - Add excersise and callories burning.")
    # print("[3] - Show list of food.")
    # print("[4] - Show list of excersises.")
    # print("[5] - Mark/unmark as done")
    # print("[6] - Delete thing to do.")
    # print("[7] - Archive")
    # print("[8] - Exit")
    # print("[9] - calculate calories")
    if choice == 0:
        data_menager.add_food(dict_of_food)
    elif choice == 1:
        data_menager.add_excersise(dict_of_excersises)
    elif choice == 2:
        data_menager.show_list_of_food()
        print('\nPress any key to display a menu')
        next_step = getch()
    elif choice == 3:
        data_menager.show_list_of_excersises()
        print('\nPress any key to display a menu')
        next_step = getch()
    elif choice == 4:
        data_menager.mark_as_done()
    elif choice == 5:
        data_menager.delete_thing()
    elif choice == 6:
        data_menager.archive()
    elif choice == 7:
        data_menager.save()
    elif choice == 8:
        x = data_menager.import_file(filename='food.txt')
        value = data_menager.calculate(x)
        data_menager.check(value)

def main():
    while 1:
        run_functions(menu())

if __name__ == '__main__':
    main()