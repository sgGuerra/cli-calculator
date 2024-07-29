class Calculadora:

    def add(self, num_1: float, num_2: float) -> float:  # pistas de tipo
        return num_1 + num_2

    def subtract(self, num_1: float, num_2: float) -> float:  # pistas de tipo
        return num_1 - num_2

    def multiply(self, num_1: float, num_2: float) -> float:  # pistas de tipo
        return num_1 * num_2

    def divida(self, num_1: float, num_2: float) -> float:  # pistas de tipo
        if num_2 == 0:
            return "Cannor divide by zaro!"
        return num_1 / num_2
