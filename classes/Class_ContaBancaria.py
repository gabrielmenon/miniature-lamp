from classPessoa import Pessoa;
import random

class Conta_Bancaria:
    def __init__(self, _titular: Pessoa, _saldo: float) -> None:
        self.titular = _titular;
        self.saldo = _saldo;
        self.numero = random.randint(1, 10000);    
        

    def Exibir_Saldo(self):
        print(f'O saldo da conta corrente é: R${self.saldo}');
        return self.saldo

    def Depositar_Dinheiro(self, inputCash):
        if(inputCash > 0):
            self.saldo += inputCash;
            print("\nValor depositado com sucesso.");
            print(f'O salto atual é: R${self.saldo}');
            return True;
        else:
            print("\nNão é possível efetuar o depósito.");
            return False
    def Retirar_Dinheiro(self, outputCash):
        if(self.saldo < outputCash):
            print("\nEsse valor não está disponível pra saque.");
            return False
        else:
            self.saldo -= outputCash;
            print("\nValor retirado com sucesso.");
            print(f'O saldo atual é: R${self.saldo}');
            return True;
                   
    def exibir_informaçõesConta(self):
        print(f'\nNome do titular: {self.titular.nome} {self.titular.sobrenome};');
        print(f'Número da c/c: {self.numero}');
        print(f'Saldo atual: R${self.saldo}');


    def getTitular(self):
        return self.titular;
    def getTitular(self, _newTitular):
        self.titular = _newTitular;
    def getNumero(self):
        return self.numero;
    def setNumero(self, _newNumero):
        self.numero = _newNumero;
    def getSaldo(self):
        return self.saldo;
    def setSaldo(self, _newSaldo):
        self.saldo = _newSaldo;