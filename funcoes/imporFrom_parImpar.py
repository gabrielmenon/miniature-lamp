from def_ParImpar import verificarParImpar;

resultado1 = int(0);
resultado2 = int(0);
input1 = int(0);
input2 = int(0);

input1 = input("Digite o primeiro número inteiro: ");
input2 = input("Digite o segundo número inteiro: ");

resultado1 = verificarParImpar(input1);
print(resultado1);

resultado2 = verificarParImpar(input2);
print(resultado2);