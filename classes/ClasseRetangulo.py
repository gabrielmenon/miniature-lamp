class Retangulo:
    def __init__(self, _comprimento: float, _largura: float) -> None:
        self.comprimento = _comprimento;
        self.largura = _largura;
        if(_comprimento == _largura):
            print("Square exception.")
            exit(1);

    def area(self):
        result  = float(0);
        result = self.comprimento *self.largura;
        print(result);

    def perimetro(self):
        result = float(0);
        result = 2* (self.comprimento + self.largura);
        print(result);

retangulo_1 = Retangulo(2,5);

print("A área do retangulo é:");
retangulo_1.area();
print("O perimetro do retangulo é: ");
retangulo_1.perimetro();