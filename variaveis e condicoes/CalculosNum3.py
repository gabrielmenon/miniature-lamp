InputValue = (int);
Num = int(0);
Count = int(1);

print(f'Esse algoritmo irá calcular a soma dos números de 1 ao número informado.');

InputValue = int(input("Digite o número limite para a soma: "));

while(Count <= InputValue):
    Num += Count;
    Count += 1;

print(f'O resultado da soma de 1 a {InputValue} é {Num}');