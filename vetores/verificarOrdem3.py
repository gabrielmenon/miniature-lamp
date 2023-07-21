#algoritmo para verificar se o vetor está ordenado de forma crescente.

numbers = [1,2,3,5,4,6,7,8];
isOrdenado = True;

for i in range (0, len(numbers)-1, 1):
    if(numbers[i]>numbers[i+1]):
        isOrdenado = False;
        break;

if(isOrdenado):
    print("O vetor está ordenado.");
else:
    print("O vetor não está ordenado.");