def contadorNumero(numero1:int, numero2:int) -> int:
    if(numero1<=numero2):
        print(numero1);
        return contadorNumero(numero1 + 1, numero2);

contadorNumero(1,10);

