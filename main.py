"""
Simple Calculator Application
A basic calculator that performs arithmetic operations
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    """Main function to run the calculator"""
    print("Simple Calculator")
    print("=" * 40)

    while True:
        print("\nOperations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("\nSelect operation (1-5): ")

        if choice == '5':
            print("Thank you for using the calculator!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                    print(f"Result: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"Result: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"Result: {num1} * {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
