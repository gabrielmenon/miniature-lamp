vector = [];
maxValue = float(0);

print(f'O algoritmo a seguir irá armazenar número em um vetor e retornar o maior valor armazenado.');
print(f'Digite 0 (zero) para encerrar o algoritmo.');

while(True):

    inputValue = float(0);
    inputValue = float(input("Digite um número: "));
    
    if(inputValue != 0):

        vector.append(inputValue);

    else:
        break;

for i in range(0, len(vector), 1):
    if(vector[i] >= maxValue):
        maxValue = vector[i];

print(f'O maior valor armazenado no vetor {vector} é igual a {maxValue}');