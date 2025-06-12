from app.calculation import Calculation
from app.operation import add, subtract, multiply, divide

class Calculator:
    def __init__(self):
        self.history = []

    def perform_operation(self, operation, a, b):
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            raise ValueError("Unsupported operation.")
        
        # Store the calculation in history
        calculation = Calculation(a, b, operation, result)
        self.history.append(calculation)
        return result

    def get_history(self):
        return [str(c) for c in self.history] # pragma: no cover
    
