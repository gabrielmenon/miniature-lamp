InputNum = (int);
result = (str);

InputNum = input("Digite um número inteiro: ");

result = "Não solucionado";

if(InputNum.isdigit()):
    InputNum = int(InputNum);

if(type(InputNum) != int):
    result = "O usuário não digitou um número inteiro.";
    print(result);
    exit();

else:
    if(InputNum % 2 == 0):
        result = "O número " + str(InputNum) + " é par.";
        print(result);
        exit();

    else:
        result = "O número " + str(InputNum) + " é ímpar.";
        print(result);
        exit();