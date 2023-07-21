InputValue = (int);
CountStop = (int);
result = (int);
Multiplicador = (int);



print(f'O algoritmo a seguir irá imprimir a tabuada de um número inteiro informado pelo usuário.');

InputValue = int(input("Digite um número inteiro para ser multiplicado: "));
CountStop = int(input("Digite um número do multiplicações: "));

for i in range(CountStop):
    Multiplicador = i + 1;
    result = InputValue*(Multiplicador);
    print(f'{InputValue} x {Multiplicador} = {result}');
   
    

print(f'O programa será encerrado.');
exit();