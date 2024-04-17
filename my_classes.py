from my_functions import estimate_max_hr
import json

class Person():

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.__dict__ = { "first_name" : self.first_name,
                        "last_name" : self.last_name,
                        "age" : self.age,
                        "estimate_max_hr" : estimate_max_hr(self.age, self.sex)}
    def estimate_max_hr(self):
        return estimate_max_hr(self.age, self.sex)
    
    def save(self):
        with open("person.json", "w") as f: 
            json.dump(self.__dict__, f)

class Experiment():

    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
        self.__dict__ = {"experiment_name" : self.experiment_name,
                        "date" : self.date,
                        "supervisor" : self.supervisor,
                        "subject" : self.subject}
        
    def save(self):
        with open("experiment.json", "w") as f: 
            json.dump(self.__dict__, f)

if __name__ == "__main__":
    person = Person("felix", "sturm", 24, "male")
    person.save()