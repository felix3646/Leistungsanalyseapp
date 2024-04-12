from my_functions import build_person

first_name = input("Geben Sie den Vornamen an:")
last_name = input("Geben Sie den Nachnamen an:")
age = int(input("Geben Sie das Alter an:"))
sex = input("Geben Sie das Geschlecht an(male or female):")


print(build_person(first_name, last_name, sex, age)) 