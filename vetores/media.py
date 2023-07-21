from exemplo1 import sumVectorIndices;
import time

vector = [];
inputValue = int(0);
sumValues = int(0);
result = float(0);

print(f'Esse algoritmo irá calcular a média aritmética dos números inteiros armazenados no vetor.');
print(f'Digite 0 (zero) para encerrar o algoritmo.');

while(True):

    inputValue = int(input("Digite um número inteiro:"));

    if(inputValue != 0):
       vector.append(inputValue);
       
    
    else:
        False;
        break;

if(len(vector) == 0):
    print(f'O programa será encerrado.');
    exit();

print(f'Calculando a média aritmética...');

time.sleep(1);
print("1..");
time.sleep(1);
print("2...");
time.sleep(1);
print("3...");
time.sleep(1);
print("Pronto! O cálculo foi realizado...");

sumValues = sumVectorIndices(vector);
result = float((sumValues)/len(vector));

print(f'A média aritmética dos números {vector} é igual a {result}');