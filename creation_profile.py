import main


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
    food_calorie_formula = int(1.6 * (10 * weight + 6.25 * height - 5 * old))
    burning_calorie_formula_male = int(655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * old))
    burning_calorie_formula_woman = int(66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * old))

    return food_calorie_formula, burning_calorie_formula_male, burning_calorie_formula_woman


def get_needed_calories():
    print('Hello Sir/Madam')
    print("Now we need to get yours daily caloric demand.\nDo you already know it[1] or would you like to count it[2]?")
    pressedkey = main.getch()
    if pressedkey == '1':
        return known_information()
    elif pressedkey == '2':
        return count_information()


def known_information():
    x = get_int_data('Enter your daily caloric demand: ')
    dates = caloric_formula()
    sex = input('\nAre you male[m] or female[f]?')
    return x, dates[1], dates[2], sex


def count_information():
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
        sex = main.getch()
        if sex == 'm':
            return 'm'
        elif sex == 'f':
            return 'f'
        else:
            print("Yes, it's foolproof")


def export_to_file(data, mode='w'):
    with open('demand_calories.txt', mode) as file:
        for element in data:
            if element == data[-1]:
                file.write(str(element))
            else:
                file.write(str(element) + ',')


def export_to_file_int(data, mode='w'):
    with open('demand_calories.txt', mode) as file:
        file.write(str(data))
