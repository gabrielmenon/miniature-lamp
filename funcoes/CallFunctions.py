from impor_def_tabuada import multiplicar;
from import_def_calc1aX import CalcularSomatorio;
from import_defPositivoNegativoZero import NumeroPositivoNegativoOuZero;

print(f'Algoritmo de seleção.');
print(f'A seguir está a lista de programas a serem utilizados.');
print(f'Digite o número correspondente: ');
print(f'/ 0 (zero) para sair do programa.')
print(f'/ 1 (um) para o programa de Tabuada.');
print(f'/ 2 (dois) para o programa de verificação de números positivos, negativos e zero.');
print(f'/ 3 (três) para o programa de somatório de números compreendidos na faixa informada pelo usuário.');
print(f'Caso o usuário digite o número inválido mais de três vezes, o programa será encerrado.')
print("\n");

inputChoice = int(0);
check = True;
contador = int(0);

while(check == True):

    inputChoice = int(input("Digite o número correspondente ao programa para utilização ou 0 (zero) para sair: "))
    print("\n");

    if(inputChoice >= 0 and inputChoice <= 3):

        if(inputChoice == 0):
            print(f'O programa será encerrado.');
            Check = False;
            exit();     

        if(inputChoice == 1):
            multiplicar();
            print(f'\n');
                
        if(inputChoice == 2):
            NumeroPositivoNegativoOuZero();
            print(f'\n');
        
        if(inputChoice == 3):
            CalcularSomatorio();
            print(f'\n');
        
    else:
        while(contador < 4):
            print(f'O usuário informou um númro que não corresponde a nenhum programa.');
            print(f'Por favor, informe um número válido entre 0 (zero) e 3 (três).');
            print(f'\n')
            contador = contador + 1;
            break;
    if(contador == 4):
        print(f'O usuário é retardado e digitou o número inválido mais de três vezes.');
        print(f'Dessa maneira, o programa será encerrado.');
        exit();