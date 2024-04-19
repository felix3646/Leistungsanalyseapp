from my_classes import Person, Experiment 
from my_functions import build_person
import json

first_name = input("Gib deinen Vorname an:")
last_name = input("Gib deinen Nachnamen an:")
age = int(input("Gib ein Alter an:"))
sex = input("Gib dein Geschlecht an (male or female):")

person1 = Person(first_name, last_name, sex, age) 
person1.save()

experiment_name = input("Gib den Experimentennamen an:")
date = input("Gib das Datum an:")
supervisor = input("Gib den Versuchsleiter an:")
subject = input("Gib die Versuchsperson an:")

experiment1 = Experiment(experiment_name, date, supervisor, subject)
experiment1.save()
