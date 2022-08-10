'''Calculator with functions'''
def add():

    X = float(input("Enter first number: "))
    Y = float(input("Enter second number: "))
    return X + Y

def subtract():
    X = float(input("Enter first number: "))
    Y = float(input("Enter second number: "))
    return X - Y

def multiply():
    X = float(input("Enter first number: "))
    Y = float(input("Enter second number: "))
    return X * Y

def divide():
    X = float(input("Enter first number: "))
    Y = float(input("Enter second number: "))
    if Y == 0:
        print('The second number mut be !=0')
    else:
     return X / Y

if __name__ == "__main__":
    while True:    
        choice = input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n")

        if choice == '1':
            print("The sum is:",add())

        elif choice == '2':
            print("The difference is:",subtract())

        elif choice == '3':
            print("The product is:",multiply())
        
        elif choice == '4':
            print("The quotient is:",divide())
        
        elif choice == '5':
            break
        
        else:
            print("Enter correct choice!!")