InputValue = (int);
CountStop = (int);
Count = int(1);
result = (int);


print(f'O algoritmo a seguir irá imprimir a tabuada de um número inteiro informado pelo usuário.');

InputValue = int(input("Digite um número inteiro para ser multiplicado: "));
CountStop = int(input("Digite um número do multiplicações: "));

while(Count<=CountStop):
    result = InputValue*Count;
    print(f'{InputValue} x {Count} = {result}');
    Count += 1;

print(f'O programa será encerrado.');
exit();