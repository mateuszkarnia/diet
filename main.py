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
            print(color.BOLD + color.YELLOW + menu[option].upper().center(columns) + color.END)
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
            if current < 4:
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


def get_int_data(text):
    while True:
        data_to_check = input(text)
        try:
            data_to_check = int(data_to_check)
            return data_to_check
        except ValueError:
            print("That's now even a digit")


def caloric_formula():
    weight = get_int_data('How much is your weight? ')
    height = get_int_data('How much is your height? ')
    old = get_int_data('How old are you? ')
    food_calorie_formula = int(1.6 *(10*weight + 6.25*height -5*old))
    burning_calorie_formula_male = int(655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * old))
    burning_calorie_formula_woman = int(66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * old))
    return food_calorie_formula, burning_calorie_formula_male , burning_calorie_formula_woman





def get_needed_calories():
    print('Hello Sir/Madam')
    print("Now we need to get yours daily caloric demand.\nDo you already know it[1] or would you like to count it[2]?")
    pressedkey = getch()
    if pressedkey == '1':
        x = get_int_data('Enter your daily caloric demand: ')
        dates = caloric_formula()
        sex = input('\nAre you male[m] or female[f]?')
        return x, dates[1], dates[2], sex
    elif pressedkey == '2':
        print('Please answer on the following questions.')
        sex = sex_choice()
        if sex == 'm':
            dates = caloric_formula()
            return dates[0] - 161, dates[1], dates[2], 'm'
        elif sex == 'f':
            dates = caloric_formula()
            return dates[0] + 5, dates[1], dates[2], 'f'


def sex_choice():
    while True:
        print('\nAre you male[m] or female[f]?')
        sex = getch()
        if sex == 'm':
            return 'm'
        elif sex == 'f':
            return 'f'
        else:
            print("Yes, it's foolproof")


def export_to_file(data, mode = 'w'):
    with open('demand_calories.txt', mode) as file:
        for element in data:
            if element == data[-1]:
                file.write(str(element))
            else:
                file.write(str(element) + ',')


def export_to_file_int(data, mode = 'w'):
    with open('demand_calories.txt', mode) as file:
        file.write(str(data))


def introduction_screen():
    print_ascii()
    x = get_needed_calories()

    if type(x) is tuple:
        x = list(x)
        export_to_file(x)
    else:
        export_to_file_int(x)

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
        data_manager.show_informations(value)
        pause()
    elif choice == 3:
        dict_of_excersises = {}
        data_manager.show_list_of_excersises()
        pause()

    elif choice == 4:
        sys.exit()


def main():
    while True:
        run_function(get_input())


if __name__ == '__main__':
    introduction_screen()
    main()
