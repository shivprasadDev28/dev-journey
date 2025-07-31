def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

ch = int(input("Enter choice: "))

match ch:
    case 1:
        print("Result:",add(num1,num2))
    case 2:
        print("Result:",sub(num1,num2))
    case 3:
        print("Result:",mul(num1,num2))
    case 4:
        print("Result:",div(num1,num2))