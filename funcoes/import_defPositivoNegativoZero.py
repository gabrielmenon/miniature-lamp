from def_positivoNegativoZero import verificar_numeroPositivoNegativoZero;

def NumeroPositivoNegativoOuZero():

    inputNum = int(0);
    result = str("");
    
    print(f'O programa a seguir irá retornar se o número informado pelo usuário é positivo, negativo ou zero.');

    inputNum = int(input("Digite um número inteiro: "));

    result = verificar_numeroPositivoNegativoZero(inputNum);
    print(f' O número informado é {result}');