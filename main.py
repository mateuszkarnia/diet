import os
import time
import math
import data_menager

def main():

    choice = ""
    choice_1 = ""
    marked = "X"
    unmarked = " "

    dict_of_food = {}
    dict_of_excersises = {}

    while choice != "8":
        print("\n[1] - Add food and callories what you eat.")
        print("[2] - Add excersise and callories burning.")
        print("[3] - Show list of food.")
        print("[4] - Show list of excersises.")
        print("[5] - Mark/unmark as done")
        print("[6] - Delete thing to do.")
        print("[7] - Archive")
        print("[8] - Exit")
        print("[9] - calculate calories")
        choice = input("Type your choose: ")
        if choice == "1":
            os.system('clear')
            data_menager.add_food(dict_of_food)
        if choice == "2":
            os.system('clear')
            data_menager.add_excersise(dict_of_excersises)
        if choice == "3":
            os.system('clear')
            data_menager.show_list_of_food(filename='food.txt')
        if choice == "4":
            os.system('clear')
            data_menager.show_list_of_excersises(filename = 'excersises.txt')
        if choice == "5":
            data_menager.mark_as_done()
        if choice == "6":
            data_menager.delete_thing()
        if choice == "7":
            data_menager.archive()
        if choice == "8":
            data_menager.save()
        if choice == "9":
            x = data_menager.import_file(filename='food.txt')
            value = data_menager.calculate(x)
            data_menager.check(value)
main()
