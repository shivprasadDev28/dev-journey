#PYTHON

#* topic completed

"""
output
variabls
input
If/else
loops (for, while)
nested conditions
List
Tuple
Set
Dictionary
Functions
CLASS
"""

#* current TOPIC OOP

# TODO 

from abc import ABC, abstractclassmethod

class Veh(ABC):
    @abstractclassmethod
    def start(self):
        pass

class Car(Veh):
    def start(self):
        print("Engine started")

c = Car()
c.start()