import os


def add_food(dict_of_food):
    name_of_food = input("[1] - Back\nEnter the name of the food: ")
    food_calorie = input("Enter the amount of calories: ")

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


def check(calories):
    if calories <1500:
        print("\n"+str(calories) + " kcl That's too low!")
    elif calories <1800 or calories < 2500:
        print("\n"+str(calories) + " kcl Good")
    elif calories < 2000:
        print("\n"+str(calories) + " kcl Perfect!")
    elif calories > 2500:
        print("\n"+str(calories) + " kcl That's too much!")
    else:
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
    name_of_excersise = input("[1] - Back\nEnter the name of the excersise: ")
    calories_burning = input("Enter the amount of calories burning: ")
    dict_of_excersises[name_of_excersise] = calories_burning

    fout = "excersises.txt"
    fo = open(fout, "a")

    for k, v in dict_of_excersises.items():
        fo.write(str(k) + " " + v  + " " + 'kcl\n')


def mark_as_done():
    show_list()
    mark_choise = input("Choose number 0f thing which you want to mark/unmark as done: ")
    if things_marked[int(mark_choise) - 1] != "X":
        things_marked[int(mark_choise) - 1] = marked
    else:
        things_marked[int(mark_choise) - 1] = unmarked
    show_list()


def delete_thing():
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


def calculate(list_a):
    count = 0
    for i in range(len(list_a)):
        count += int(list_a[i][1])

    return count
