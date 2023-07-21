#O programa irá verificar se o vetor informado está em ordem crescente ou não.
from insert import insertVectorValues;

vector1 = [];
vector2 = [];

print(f'O programa irá verificar se o vetor informado pelo usuário se encontra em ordem crescente.');
print(f'Digite apenas números inteiros. Digite 0 (zero) para encerrar o programa.\n');

vector1 = insertVectorValues();
vector2 = vector1.copy();
vector2.sort();

if(vector1 == vector2):
    print("\nO vetor está ordenado em ordem crescente.");
    
else:
    print("\nO vetor não está ordenado em ordem crescente.");