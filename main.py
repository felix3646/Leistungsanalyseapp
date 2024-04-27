from my_classes import Person, Subject, Evaluator, Experiment 
from my_functions import build_person
import json

first_name = input("Gib deinen Vorname an:")
last_name = input("Gib deinen Nachnamen an:")
age = int(input("Gib ein Alter an:"))
sex = input("Gib dein Geschlecht an (male or female):")
birthday = input("Gib dein Geburtsdatum ein (dd/mm/yyyy):")

person62 = Subject(first_name, last_name, sex, age, birthday) 
person62.save()

experiment_name = input("Wie heisst das Experiment:")
date = input("Gib das Datum an(dd/mm/yyyy):")
supervisor = input("Gib den Versuchsleiter an:")
subject = input("Gib die Versuchsperson an:")

experiment1 = Experiment(experiment_name, date, supervisor, subject)
experiment1.save()
