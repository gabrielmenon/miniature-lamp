import math

class circulo:
    def __init__(self, _raio) -> None:
        self.raio = _raio;

    def area(self):
        result = float(0);
        result = math.pi *(self.raio**2);
        print(f'O cálculo da área resultou em: {round(result, 3)}');
        return result;

    def crcuferencia(self):
        result = float(0);
        result = 2*math.pi*self.raio;
        print(f'O cálculo da circunferência resultou em: {round(result, 3)}');
        return result;