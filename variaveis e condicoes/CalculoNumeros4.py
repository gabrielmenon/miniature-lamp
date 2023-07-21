InputValue = (int);
Result = (0);

print(f'Esse algoritmo irá calcular a soma dos números de 1 ao número informado.');

InputValue = int(input("Digite um número limite para a soma: "))

for i in range (1, InputValue +1 , 1 ):
    Result += i;
    
print(f'A soma dos números entre 1 e {InputValue} é {Result}');