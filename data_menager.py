import os


choice = ""
choice_1 = ""
marked = "X"
unmarked = " "

things_to_do = []
things_marked = []


def add_food(list_of_food, list_of_food_calories):
    cls()
    name_of_food = input("[1] - Back\nEnter the name of the food: ")
    food_calorie = input("Enter the amount of calories: ")
    if name_of_food != "1":
        list_of_food.append(name_of_food)
        list_of_food_calories.append(food_calorie)

        return(list_of_food, list_of_food_calories)

def show_list_of_food(list_of_food, list_of_food_calories):
    cls()
    print("Your list of food:")
    for k in range(0, len(list_of_food), 1):
        print(str(k+1) + ".) " + list_of_food[k] + " [" + list_of_food_calories[k] + "]")

def show_list_of_excersises(list_of_excersises, list_of_calories_burning):
    cls()
    print("Your list of excersises:")
    for k in range(0, len(list_of_excersises), 1):
        print(str(k+1), ".) ", list_of_excersises[k], list_of_calories_burning[k], "kcl")

def add_excersise(list_of_excersises, list_of_calories_burning):
    cls()
    name_of_excersise = input("[1] - Back\nEnter the name of the excersise: ")
    calories_burning = input("Enter the amount of calories burning: ")

    if name_of_excersise != "1":
        list_of_excersises.append(name_of_excersise)
        list_of_calories_burning.append(calories_burning)
        return(list_of_excersises, list_of_calories_burning)


def mark_as_done():
    cls()
    show_list()
    mark_choise = input("Choose number 0f thing which you want to mark/unmark as done: ")
    if things_marked[int(mark_choise) - 1] != "X":
        things_marked[int(mark_choise) - 1] = marked
    else:
        things_marked[int(mark_choise) - 1] = unmarked
    show_list()


def delete_thing():
    cls()
    show_list()
    delete_choice = input("[x] - Back\nWhich task do you want to delete?")
    if delete_choice != "x":
        things_to_do.remove(things_to_do[int(delete_choice) - 1])
        things_marked.pop(int(delete_choice) - 1)
    if delete_choice == "x":
        return
    show_list()

def archive():
    k = 0

    while k != len(things_to_do):
        if things_marked[k] == "X":
            things_to_do.pop(k)
            things_marked.pop(k)
            k -= 1
        k += 1



def save():
    file_to_delete="things.txt"
    if os.path.isfile(file_to_delete) :
        os.unlink(file_to_delete)
    file_to_delete="marking.txt"
    if os.path.isfile(file_to_delete) :
        os.unlink(file_to_delete)
    file1 = open("things.txt", "w")
    file2 = open("marking.txt", "w")
    for k in range(0, len(things_to_do), 1):
        file1.write(things_to_do[k] + "\n")
        file2.write(things_marked[k] +"\n")
    file1.close()
    file2.close()


def opened():
    file1 = open("things.txt", "r")
    for line in file1:
        lstr = line
        lstr = lstr.replace("\n","")
        things_to_do.append(lstr)
    file2 = open("marking.txt", "r")
    for line in file2:
        lstr = line
        lstr = lstr.replace("\n","")
        things_marked.append(lstr)



def cls():
    print("\n" * 5)

file_exist="things.txt"
if os.path.isfile(file_exist) :
    file_exist="marking.txt"
    if os.path.isfile(file_exist) :
        opened()
