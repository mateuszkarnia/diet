import data_menager

def add_excersise(list_of_excersises, list_of_calories_burning):
    data_menager.cls()
    name_of_excersise = input("[1] - Back\nEnter the name of the excersise: ")
    calories_burning = input("Enter the amount of calories burning")

    if name_of_excersise != "1":
        list_of_excersises.append(name_of_excersise)
        list_of_calories_burning.append(calories_burning)
        print(list_of_excersises, list_of_calories_burning)
add_excersise(list_of_excersises, list_of_calories_burning)
