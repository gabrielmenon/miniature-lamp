from insert import insertVectorValues;

vector = [];
inputValue = int(0);
aux = int(0);

print(f'O programa a seguir irá inserir dados em um vetor e verificar se há um elemento específico nesse vetor.\n')
print(f'Digite 0 (zero) para sair do programa.\n')

vector = insertVectorValues();

inputValue = int(input("\nDigite o número que deseja verificar se consta no vetor: "));

for i in range(len(vector)):
    
    if(vector[i] == inputValue):
        aux +=1;

if(aux==1):
    print(f'\nO número {inputValue} está presente {aux} vez no vetor.');
if(aux>1):
    print(f'\nO número {inputValue} está presente {aux} vezes no vetor.');
else:
    print(f'\nO número {inputValue} não está presente no vetor.');