from my_functions import build_person
import json
from my_classes import Person, Experiment

first_name = input("Geben Sie den Vornamen an:")
last_name = input("Geben Sie den Nachnamen an:")
age = int(input("Geben Sie das Alter an:"))
sex = input("Geben Sie das Geschlecht an(male or female):")

person1 = Person(first_name, last_name, sex, age) 
person1.save()

experiment_name = input("Geben Sie den Experimentennamen an:")
date = input("Geben Sie das Datum an:")
supervisor = input("Geben Sie den Versuchsleiter an:")
subject = input("Geben Sie die Versuchsperson an:")

experiment1 = Experiment(experiment_name, date, supervisor, subject)
experiment1.save()