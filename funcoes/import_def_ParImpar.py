import def_ParImpar;
import checkint;


input1 = str("0");

input1 = input("Digite o primeiro número inteiro: ");

if(checkint.checkintnum(input1)):
    
    input1 = int(input1);
    print(def_ParImpar.verificarParImpar(input1));

else:
    print("Digite apenas números inteiros.");