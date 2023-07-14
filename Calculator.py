import cmath

def display_menu():
    print("Complex Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_complex_number():
    real = float(input("Enter the real part: "))
    imaginary = float(input("Enter the imaginary part: "))
    return complex(real, imaginary)

def add_complex_numbers():
    num1 = get_complex_number()
    num2 = get_complex_number()
    result = num1 + num2
    print("Result: ", result)

def subtract_complex_numbers():
    num1 = get_complex_number()
    num2 = get_complex_number()
    result = num1 - num2
    print("Result: ", result)

def multiply_complex_numbers():
    num1 = get_complex_number()
    num2 = get_complex_number()
    result = num1 * num2
    print("Result: ", result)

def divide_complex_numbers():
    num1 = get_complex_number()
    num2 = get_complex_number()
    result = num1 / num2
    print("Result: ", result)

def complex_calculator():
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            add_complex_numbers()
        elif choice == 2:
            subtract_complex_numbers()
        elif choice == 3:
            multiply_complex_numbers()
        elif choice == 4:
            divide_complex_numbers()
        elif choice == 5:
            print("Exiting the calculator...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

complex_calculator()