InputNum = (int);
result =(str);

InputNum = int(input("Digite um número inteiro: "));

result = "Não solucionado.";

if(InputNum > 0):
    result = "O número informado é positivo.";
    print(result);
    exit();

if(InputNum < 0):
    result = "O número informado é negativo.";
    print(result);
    exit();

if(InputNum == 0):
    result = "O número informado é zero."
    print(result);
    exit();