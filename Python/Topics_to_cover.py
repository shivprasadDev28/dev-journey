#PYTHON

#* topic 

"""
output
variabls
input
If/else
loops (for, while)
nested conditions
"""

# todo Create a program that validates an email address (must contain '@' and '.').

email = input("enter email: ")

if "@" and "." in email:
    print("Valid email")
else:
    print("Not valid")