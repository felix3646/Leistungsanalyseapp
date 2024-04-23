from my_functions import build_person
import json
from my_classes import Person, Experiment, Subject, Examiner

first_name = input("Geben Sie den Vornamen an:")
last_name = input("Geben Sie den Nachnamen an:")
age = int(input("Geben Sie das Alter an:"))
sex = input("Geben Sie das Geschlecht an(male or female):")
birthday = input("Geben Sie das Geburstdatum an:")

person1 = Subject(first_name, last_name, age, sex, birthday) 
person1.save()

