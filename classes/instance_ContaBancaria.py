from Class_ContaBancaria import Conta_Bancaria;
from classPessoa import Pessoa;
vetorCC = [];
SaldoInicial = int(0);
inputMenu = int(0);
saldo = float(0);

pessoa_1 = Pessoa("João", "100.100.100-10", "10/10/10", "da Silva");

Conta_1 = Conta_Bancaria(pessoa_1, SaldoInicial);

print("");
print(f'{pessoa_1.nome} {pessoa_1.sobrenome}, bem vindo ao Banco MENON');

while True:
    print("---------------------------------")
    print("\nMenu do Usuário.");
    print("Digite:\n1 - para consultar saldo.\n2 - para depositar dinheiro.\n3 - para sacar dinheiro.\n4 - para informações da conta.\n0 - para sair.");
    print("\n---------------------------------")
    print("");
    inputMenu = int(input("Digite o número do comando: "));
    print("");
    print("---------------------------------");

    if(inputMenu<0 or inputMenu>4):
        print("\nComando inválido.");
    
    else:
        if(inputMenu==1):
            saldo = Conta_1.Exibir_Saldo();
            
        if(inputMenu == 2):
            inputCash = float(input("Digite o valor para depósito: "));
            Conta_1.Depositar_Dinheiro(inputCash);
        if(inputMenu == 3):
            outputCash = float(input("Digite o valor para saque: "));
            Conta_1.Retirar_Dinheiro(outputCash);
        if(inputMenu == 4):
            Conta_1.exibir_informaçõesConta();
        if(inputMenu == 0):
            print("A sessão será encerrada com segurança.")
            print("");
            break;
