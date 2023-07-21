InputValue = (int);
result = int(1);

print(f'Esse algoritmo irá retornar o Fatorial de um número.');
InputValue = int(input("Digite um número inteiro:"));

for i in range(InputValue, 0 , -1):
    result *= i;
    print(result)
    
print(f'O fatorial de {InputValue} é {result}');