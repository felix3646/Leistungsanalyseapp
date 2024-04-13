from my_functions import build_person
import json

first_name = input("Geben Sie den Vornamen an:")
last_name = input("Geben Sie den Nachnamen an:")
age = int(input("Geben Sie das Alter an:"))
sex = input("Geben Sie das Geschlecht an(male or female):")

person1 = build_person(first_name, last_name, sex, age) 

with open("person.json", "w") as f: 
    json.dump(person1, f)