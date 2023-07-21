#O programa irá verificar se o vetor informado está em ordem crescente ou não.
from insert import insertVectorValues;

vector = [];
check = bool(False);

print(f'O programa irá verificar se o vetor informado pelo usuário se encontra em ordem crescente.');
print(f'Digite apenas números inteiros. Digite 0 (zero) para encerrar o programa.\n');

vector = insertVectorValues();

if(len(vector) == 0):
    print("\nO usuário digitou 0 (zero), portanto o programa será encerrado.");

else:
    for i in range (0, len(vector)-1, 1):
        if(vector[i]<=vector[i+1]):
            check = True;
        else:
            check = False;
            break;

    if(check == True):
        print("\nO vetor está em ordem crescente.");
    else:
        print("\nO vetor não está em ordem crescente.");