from ascii_art import logo

print(logo)

def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

operations = {
    "+" : add ,
    "-" : subtract ,
    "*" : multiply ,
    "/" : divide
}

first_number = float(input("What\'s the first number? "))

continue_calculation = True

while continue_calculation == True:

    operation = input("""\n
    +
    -
    *
    /
    Pick an operation: 
    """)
    next_number = float(input("\nWhat\'s the next number? "))

    result = operations[operation](first_number , next_number)

    calculation = (f"{first_number} {operation} {next_number} = {result}")

    print(calculation)

    should_continue_calculation = input(f"Type \'y' to continue with {result}, or type \'n' to start a new calculation.\n").lower()

    if should_continue_calculation == "y":
        first_number = result
    elif should_continue_calculation == "n":
        print("\n" * 100)
        first_number = float(input("What\'s the first number? "))