from art import logo

def add(n1, n2):
    return n1 + n2


def substract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "/":divide,
    "+":add,
    "*": multiply,
    "-":substract
}

print(logo)
first_number = int(input("Type in the first number "))
while True:
    second_number = int(input("Type in the next number "))
    operation = input(f"Type in the operations. Available operations: {"".join(operations.keys())} ")
    result = operations[operation](first_number, second_number)
    print(f"Result is {result}")
    want_continue = input("Type y if you want to continue, n otherwise ")
    if want_continue == "y":
        first_number = result
    else:
        break