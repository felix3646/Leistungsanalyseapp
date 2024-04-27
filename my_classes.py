from my_functions import estimate_max_hr
import json

class Person():
#angepasst an Aufgabe 6.2
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__dict__ = {"first_name": self.first_name,
                        "last_name": self.last_name,
                        }
      
    def save(self):
        with open("person.json", "w") as f:
            json.dump(self.__dict__, f)

class Evaluator(Person):
    def __init__(self,first_name, last_name, id):
        super().__init__(first_name, last_name)
        self.id = id
        self.__dict__ = {"first_name": self.first_name,
                     "last_name": self.last_name,
                     "id":self.id
                     }
    def save(self):
        with open("evaluator.json", "w") as f:
            json.dump(self.__dict__, f)

#Aufgabe 6.2 
class Subject (Person): #Kindklasse Subject übernimmt die Elternklasse (Person)
    def __init__(self,first_name,last_name,age,sex, birthday): # geburtstag kommt dazu für die genaure berechnung
        super().__init__(first_name, last_name) # Zeile übernommen vom Skriptum

        self.age = age
        self.sex = sex
        self.__birthday = birthday #wird mit .__ "versteckt"
        self.max_heart_rate = self.estimate_max_hr()
        self.__dict__ = {"first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age,
                    "sex": self.sex,
                    "max_heart_rate": self.max_heart_rate
                    }
    
    def estimate_max_hr(self):
        return estimate_max_hr(self.age, self.sex)
    
    def save(self):
        with open("subject.json", "w") as f:
            json.dump(self.__dict__, f)

# bleibt gleich
class Experiment():

    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
        self.__dict__= {"experiment_name" : self.experiment_name,
                    "date" : self.date,
                    "supervisor" : self.supervisor,
                    "subject" : self.subject
                    }
    
    def save(self):
        with open("experiment.json", "w") as f:
            json.dump(self.__dict__, f)


if __name__ == "__main__":
    person = Subject("Amelie","Koutny", "33", "female","11/07/1990")
    person.save()
    
    experiment = Experiment("Test6.2", "26/04/2024", "Thomas", "Moritz")
    experiment.save()

    # es klappt nicht so richtig, keine Ahnung wieso... 