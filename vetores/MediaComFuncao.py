from exemplo1 import sumVectorIndices;
from ..funcoes.insertValues import insertVectorValues;


vector = [];
inputValue = int(0);
sumValues = int(0);
result = float(0);

print(f'Esse algoritmo irá calcular a média aritmética dos números inteiros armazenados no vetor.');
print(f'Digite 0 (zero) para encerrar o algoritmo.');

vector = insertVectorValues();

if(len(vector) == 0):
    print(f'O programa será encerrado.');
    exit();


sumValues = sumVectorIndices(vector);
result = float((sumValues)/len(vector));

print(f'A média aritmética dos números {vector} é igual a {result}');