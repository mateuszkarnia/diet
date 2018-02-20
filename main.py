import os
import time
import math
import data_menager
import common

def main():

    choice = ""
    choice_1 = ""
    marked = "X"
    unmarked = " "

    list_of_food = []
    list_of_food_calories = []
    list_of_excersises = []
    list_of_calories_burning = []

    while choice != "8":
        print("[1] - Add food and callories what you eat.")
        print("[2] - Add excersise and callories burning.")
        print("[3] - Show list of food.")
        print("[4] - Show list of excersises.")
        print("[5] - Mark/unmark as done")
        print("[6] - Delete thing to do.")
        print("[7] - Archive")
        print("[8] - Exit")
        choice = input("Type your choose: ")
        if choice == "1":
            os.system('clear')
            data_menager.add_food(list_of_food, list_of_food_calories)
        if choice == "2":
            os.system('clear')
            data_menager.add_excersise(list_of_excersises, list_of_calories_burning)
        if choice == "3":
            os.system('clear')
            data_menager.show_list_of_food(list_of_food, list_of_food_calories)
        if choice == "4":
            os.system('clear')
            data_menager.show_list_of_excersises(list_of_excersises, list_of_calories_burning)
        if choice == "5":
            data_menager.mark_as_done()
        if choice == "6":
            data_menager.delete_thing()
        if choice == "7":
            data_menager.archive()
        if choice == "8":
            data_menager.save()
main()
