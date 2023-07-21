#O altoritmo irá transferir os elementos de um vetor para outro vetor.

from insert import insertVectorValues;

vector1 = [];
vector2 = [];
aux = int(0);

print(f'O programa irá preencher um vetor transferir os números inteiros desse vetor para outro vetor.');
print(f'Digite 0 (zero) para encerrar a inserção de números inteiros no vetor.')

vector1 = insertVectorValues();

print(vector1);
print(vector2);

while(len(vector1) != 0):
    aux = vector1[0];
    print(aux);
    vector1.remove(aux);
    vector2.append(aux);

print(vector1);
print(vector2);