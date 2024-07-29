class Calculadora:

    def add(self, num_1: float, num_2: float) -> float:  # pistas de tipo
        return num_1 + num_2

    def subtract(self, num_1: float, num_2: float) -> float:  # pistas de tipo
        return num_1 - num_2

    def multiply(self, num_1: float, num_2: float) -> float:  # pistas de tipo
        return num_1 * num_2

    def divide(self, num_1: float, num_2: float) -> float | str:  # pistas de tipo
        if num_2 == 0:
            return "Cannot divide by zero!"
        return num_1 / num_2
