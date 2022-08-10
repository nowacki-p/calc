'''Calculator with functions'''
from ast import Return


def read_parameters() -> float:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    return x , y

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        print('The second number mut be !=0')
    else:
     return x / y

if __name__ == "__main__":
    while True: 

        choice = input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n")
        options = {"1": add, "2": subtract, "3": multiply, "4": divide, "5": Return}
        read_parameters() 
        print('x',read_parameters)

        options.get(choice,  print("Enter correct choice!!"))(x,y)
else:
        print("Enter correct choice!!")