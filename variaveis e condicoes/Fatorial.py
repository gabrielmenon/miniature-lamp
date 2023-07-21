InputValue = (int);
Aux = (int);
result = (int);

print(f'O código irá retornar o Fatorial de um número.');

InputValue = int(input("Digite um número inteiro: "));
Aux = InputValue;
result = InputValue;

while(InputValue>1):    
    result *= (InputValue-1);
    InputValue -= 1;
    
print(f' O fatorial de {Aux} é {result}');