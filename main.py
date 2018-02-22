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


def get_input():
    options_to_chose = ['Add food and callories what you eat.', 'Add excersise and callories burning', 'Show list of food.',
                        'Show list of excersises.', 'Mark/unmark as done', 'Delete thing to do', 'Archive', 'Exit\n', "Press key 'e' to run current option"]
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
            if current < 7:
                current += 1
    return current


def pause():
    columns = shutil.get_terminal_size().columns
    print('\n')
    print('Press any key to display a menu.'.center(columns))
    next_step = getch()


def print_ascii():
    os.system('clear')
    columns = shutil.get_terminal_size().columns
    
    print(" <}\\".center(columns))
    print("      .--\--.".center(columns))
    print("     /   `   \\".center(columns))
    print("     |       |".center(columns))
    print("      \     /".center(columns))
    print("      '-'-'".center(columns))
    pause()


def caloric_formula():
    weight = int(input('How much is your weight?'))
    height = int(input('How much is your height?'))
    old = int(input('How old are you?'))
    return 10*weight + 6.25*height -5*old


def get_needed_calories():
    print('Hello Sir/Madam')
    print("Now we need to get yours daily caloric demand.\nDo you already know it[1] or would you like to count it[2]?")
    pressedkey = getch()
    if pressedkey == '1':
        return input('Enter your daily caloric demand: ')
    elif pressedkey == '2':
        print('Please answer on the following questions.')
        sex = sex_choice()
        if sex == 'm':
            return int(caloric_formula() - 161.0)
        elif sex == 'f':
            return int(caloric_formula() + 5.0)


def sex_choice():
    while 1:
        print('\nAre you male[m] or female[f]?')
        sex = getch()
        if sex == 'm':
            return 'm'
        elif sex == 'f':
            return 'f'
        else:
            print("Yes, it's foolproof")


def introduction_screen():
    print_ascii()
    get_needed_calories()


def run_function(current_choice):
    choice = current_choice
    choice_1 = ""
    marked = "X"
    unmarked = " "

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
        data_manager.mark_as_done()
    elif choice == 5:
        data_manager.delete_thing()
    elif choice == 6:
        data_manager.archive()
    elif choice == 7:
        data_manager.save()


def main():
    while 1:
        run_function(get_input())


if __name__ == '__main__':
    introduction_screen()
