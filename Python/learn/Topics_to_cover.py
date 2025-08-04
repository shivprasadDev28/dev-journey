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
"""
Create a Book class with: 

Attributes: title, author, pages

Method: describe() that prints:
"{title} by {author}, {pages} pages"
"""

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def describe(self):
        print(f"{self.title} by {self.author}, {self.pages} pages.")


book1 = Book("Atomic Habits","James Clear",320)
book1.describe()