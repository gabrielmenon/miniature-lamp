def verificarParImpar(InputNum: str):

#    InputNum = input("Digite um número inteiro: "); Não é necessário o input na função.

    result = (str);

    if(InputNum.isdigit()):
        InputNum = int(InputNum);

    if(type(InputNum) != int):
        result = "O usuário não digitou um número inteiro.";
        return;
        

    else:
        if(InputNum % 2 == 0):
            result = "O número " + str(InputNum) + " é par.";
            
        
        else:
            result = "O número " + str(InputNum) + " é ímpar.";
            
    
    return(result);