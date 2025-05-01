
import art

print(art.logo)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

dictionary = {"+": add, "-": subtract, "*":multiply, "/": divide}

def calculator():
    accumulate = True

    n1 = float(input("Enter the first number:\n"))

    while accumulate == True:
        operation = input("Select an operator +, -, * or /:\n")
        n2 = float(input("Enter the second number:\n"))

        calc = dictionary[operation]
        result = calc(n1, n2)
        print(f"{n1} {operation} {n2} = {result}")

        reuse_result = input("Do you want to continue working with the same result? Y or N?")

        if reuse_result == "Y":
            n1 = result
        else:
            accumulate=False
            print ("\n" * 20)
            calculator()


calculator()


