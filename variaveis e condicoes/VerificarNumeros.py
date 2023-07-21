InputNum = (int);
result =(str);

InputNum = input("Digite um número inteiro: ");

result = "Não solucionado.";

if(InputNum.isdigit()):
    InputNum = int(InputNum);

if(type(InputNum) != int):
    print(f'O usuário não digitou um número inteiro, portanto o programa será fechado.')
    exit();

if(InputNum > 0):
    result = "O número informado é positivo.";
else:
    if(InputNum < 0):
        result = "O número informado é negativo.";
    else:
        if(InputNum == 0):
            result = "O número informado é zero."

print(result);