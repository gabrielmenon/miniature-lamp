from def_tabuada import tabuadaNum;

def multiplicar():
    
    InputValue = (int);
    CountStop = (int);
    resultado = int(0);
    contador = int(0)

    print(f'O algoritmo a seguir irá imprimir a tabuada de um número inteiro informado pelo usuário.');

    InputValue = int(input("Digite um número inteiro para ser multiplicado: "));
    CountStop = int(input("Digite um número do multiplicações: "));

    while(contador<=CountStop):
        resultado = tabuadaNum(InputValue, contador);
        print(f'{InputValue} x {contador} = {resultado}');
        contador += 1;