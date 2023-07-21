from insert import insertVectorValues;

vector = [];
inputValue = int(0);

print(f'O programa a seguir irá inserir dados em um vetor e verificar se há um elemento específico nesse vetor.')
print(f'Digite 0 (zero) para sair do programa')

vector = insertVectorValues();

inputValue = int(input("Digite o número que deseja verificar se consta no vetor: "));

if(vector.count(inputValue) == 1):
    print(f'O número {inputValue} está presente {vector.count(inputValue)} vez no vetor.');
if(vector.count(inputValue) > 1):
    print(f'O número {inputValue} está presente {vector.count(inputValue)} vezes no vetor.');
else:
    print(f'O número {inputValue} não está presente no vetor.');