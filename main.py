from app.calculator import Calculator

def print_help():
    print("\nAvailable operations: add, subtract, multiply, divide")
    print("Commands: help, history, exit\n")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def main():
    calc = Calculator()
    print("Welcome to the Command-Line Calculator! :)")
    print_help()

    while True:
        command = input("Enter command or operation: ").strip().lower()

        if command == "exit":
            print("Goodbye! -_-")
            break
        elif command == "help":
            print_help()
        elif command == "history":
            for item in calc.get_history():
                print(item)
        elif command in ("add", "subtract", "multiply", "divide"):
            a_str = input("Enter first number: ").strip()
            b_str = input("Enter second number: ").strip()

            # LBYL: Check inputs before conversion
            if not is_number(a_str) or not is_number(b_str):
                print("Invalid input: Please enter valid numeric values.")
                continue

            a = float(a_str)
            b = float(b_str)

            # EAFP: Try performing operation and handle exceptions
            try:
                result = calc.perform_operation(command, a, b)
                print(f"Result: {result}")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
            except Exception as e:
                print(f"Unexpected error: {e}")
        else:
            print("Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    main()
