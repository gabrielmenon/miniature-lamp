from def_calc1aX import calcularNumeros;

def CalcularSomatorio():
    inputNum = int(0);
    Result = int(0);

    print (f'Esse programa irá calcular a soma entre os números inteiros comprendidos na faixa informada pelo usuário: ');

    inputNum = int(input("Digite um número inteiro: "));

    Result = calcularNumeros(inputNum);
    print(f'A soma entre os números inteiros na faixa entre 1 a {inputNum} é igual a {Result}');