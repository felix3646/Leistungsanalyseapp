from my_functions import estimate_max_hr
import json

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
        self.__dict__ = { "first_name" : self.first_name,
                        "last_name" : self.last_name}
    
    def save(self):
        with open("person.json", "w") as f: 
            json.dump(self.__dict__, f)

class Subject(Person):

    def __init__(self, first_name, last_name, age, sex, birthday):
        super().__init__(first_name, last_name)

        self.age = age
        self.sex = sex
        self.__birthday = birthday
        self.max_heart_rate = self.estimate_max_hr()
        self.__dict__ = { "first_name" : self.first_name,
                        "last_name" : self.last_name,
                        "age" : self.age,
                        "sex" : self.sex,
                        "max_heart_rate" : self.max_heart_rate}
        
    def estimate_max_hr(self):
         return estimate_max_hr(self.age, self.sex)
         
    
    
    def save(self):
        with open("subject.json", "w") as f: 
            json.dump(self.__dict__, f)
        
class Examiner(Person):

    def __init__(self, first_name, last_name, id_number):
        super().__init__(first_name, last_name)


        self.id_number = id_number
        self.__dict__ = { "first_name" : self.first_name,
                        "last_name" : self.last_name,
                        "id_number" : self.id_number}
        
        
    def save(self):
        with open("examiner.json", "w") as f: 
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
    person = Subject("felix", "sturm", 34, "male", "21.3.2003")
    print(person.max_heart_rate)
    person.save()