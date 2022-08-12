"""Calculator with functions"""


def read_parameters():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    return x , y


def add(x, y):
    print("Result is :", x + y)
    return x + y


def subtract(x, y):
    print("Result is :", x - y)
    return x - y


def multiply(x, y):
    print("Result is :", x * y)
    return x * y


def divide(x, y):
    if y != 0:
        print("Result is ", x / y)
        return x / y
    else:
        print("Can't do that. Second number is null")


options = {
    "1": add,
    "2": subtract,
    "3": multiply,
    "4": divide,
    "5": ""
}

if __name__ == "__main__":
    while True:
        choice = input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit\n")
        print("You choose", choice)
        if choice in options.keys():
            if choice == "5":
                print("Exit")
                break
            else:
                x, y = read_parameters()
                options.get(choice)(x, y)
        else:
            print("Incorrect value - there is no option for this value. Try again")