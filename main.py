import os
import time
import math
import data_menager

choice = ""
choice_1 = ""
marked = "X"
unmarked = " "

things_to_do = []
things_marked = []

while choice != "6":
    print("[1] - Add food and callories what you eat.")
    print("[2] - Show list")
    print("[3] - Mark/unmark as done")
    print("[4] - Delete thing to do.")
    print("[5] - Archive")
    print("[6] - Exit")
    choice = input("Type your choose: ")
    if choice == "1":
        data_menager.add()
    if choice == "2":
        data_menager.show_list()
    if choice == "3":
        data_menager.mark_as_done()
    if choice == "4":
        data_menager.delete_thing()
    if choice == "5":
        data_menager.archive()
    if choice == "6":
        data_menager.save()