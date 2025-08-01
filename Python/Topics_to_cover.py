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
"""

#* current TOPIC OOP

# TODO 

class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes sounds.")

class Cat(Animal):
    def speak(self):
        print("Meow...")
        #super().speak()

a1 = Cat("Shiv")
a1.speak()
Animal.speak(a1)