

def addition(first_number, second_number):
    total = first_number+second_number
    return total


def subtraction(first_number, second_number):
    total = first_number-second_number
    return total


def multiplication(first_number, second_number):
    total = first_number*second_number
    return total


def division(first_number, second_number):
    if second_number == 0:
        return "Error cannot be divided"
    total = first_number//second_number
    return total


def menu():
    print("Select operation: ")
    print("[1]:Addition ")
    print("[2]:Subtration ")
    print("[3]:Multiplication")
    print("[4]:Division")


def calculator():
    while True:
        menu()
        try:
            choice = int(input("Enter Number: \n"))
            if choice == 0:
                print("Closing")
                break
            first_number = int(input("First Number: "))
            second_number = int(input("Second number: "))

            if choice == 1:
                result = addition(first_number, second_number)
                print(f"Total: {result}")

            elif choice == 2:
                result = subtraction(first_number, second_number)
                print(f"Difference: {result}")

            elif choice == 3:
                result = multiplication(first_number, second_number)
                print(f"product: {result}")

            elif choice == 4:
                result = division(first_number, second_number)
                print(f"quotient: {result}")

            else:
                print("Error no values")

        except ValueError:
            print("Error something is wrong")


calculator()
