class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def classificar(self) -> str:
        a, b, c = self.a, self.b, self.c

        if a <= 0 or b <= 0 or c <= 0:
            return "invalido"

        if a + b <= c or a + c <= b or b + c <= a:
            return "invalido"

        if a == b == c:
            return "equilatero"

        if a == b or a == c or b == c:
            return "isosceles"

        return "escaleno"
