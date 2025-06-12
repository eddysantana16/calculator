class Calculation:
    def __init__(self, a, b, operation, result):
        self.a = a
        self.b = b
        self.operation = operation
        self.result = result

    def __str__(self):
        return f"{self.a} {self.operation} {self.b} = {self.result}"
