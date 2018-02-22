import os


def add_food(dict_of_food):
        name_of_food = input("Enter the name of the food: ")
        food_calorie = input("Enter the amount of calories: ")
        print("That's not a correct input")
        dict_of_food[name_of_food] = food_calorie
        fout = "food.txt"
        fo = open(fout, "a")

        for k, v in dict_of_food.items():
            fo.write(str(k) + " " + v + " " + 'kcl\n')


def import_file(filename='food.txt'):
    file_to_open = open(filename)
    list_from_file = file_to_open.readlines()
    for i in range(len(list_from_file)):
        list_from_file[i] = list_from_file[i].replace("/n","").split(" ")

    return list_from_file


def show_informations(calories, filename = "demand_calories.txt"):
    demand_calories = []
    with open(filename , "r") as f:
        for line in f:
            line = line.split(',')
            demand_calories.append(line)
    print('________________________')
    print("\nYou need "+str(demand_calories[0][0])+ " to eat.\n")
    if demand_calories[0][3] == 'm':
        print("You need to burn " + str(int(int(demand_calories[0][2])/10)) + " kcl per day to lead a healthy lifestyle.\n")
    else:
        print("You need to burn" + str(int(int(demand_calories[0][1])/10)) + " kcl per day to lead a healthy lifestyle.\n")
    print('________________________')
    if calories > int(demand_calories[0][0]) - 50 and calories < int(demand_calories[0][0]) + 50:
        print("\nYou ate "+str(calories) + " kcl That's perfect!")
    elif calories < int(demand_calories[0][0]):
        print("\nYou ate "+str(calories) + " kcl That's too low!")
    elif calories > int(demand_calories[0][0]):
        print("\nYou ate "+str(calories) + " kcl That's too much!")


def check_excersises(calories, filename = "demand_calories.txt"):
    with open(filename , "r") as f:
        for line in f:
            demand_calories = int(line)
        print("\nYou need ",demand_calories," kcl\n")
    if calories > demand_calories - 50 and calories < demand_calories + 50:
        print("\n"+str(calories) + " kcl That's perfect")
    elif calories <demand_calories:
        print("\n"+str(calories) + " kcl That's too low!")
    elif calories >demand_calories:
        print("\n"+str(calories) + " kcl That's too much!")


def calculate(list_a):
    count = 0
    for i in range(len(list_a)):
        count += int(list_a[i][1])

    return count


def show_list_of_food():
    print("Your list of food: \n")
    with open("food.txt", "r") as f:
        for line in f:
            print(line, end='')


def show_list_of_excersises():
    print("Your list of excersises: \n")
    with open("excersises.txt", "r") as f:
        for line in f:
            print(line, end='')


def add_excersise(dict_of_excersises):
    name_of_excersise = input("Enter the name of the excersise: ")
    calories_burning = input("Enter the amount of calories burning: ")
    dict_of_excersises[name_of_excersise] = calories_burning

    fout = "excersises.txt"
    fo = open(fout, "a")

    for k, v in dict_of_excersises.items():
        fo.write(str(k) + " " + v  + " " + 'kcl\n')

#def clear_data():
    #with open()
