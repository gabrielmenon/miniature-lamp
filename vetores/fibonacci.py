fibonacci = [0,1];
sumnumbers = int(0);
inputIndex = int(0);

print(f'O algoritmo a seguir calculará a sequência Fibonacci.');

inputIndex = int(input("Digite a quantidade de números a serem exibidos: "));

#for i in range (inputIndex-2):
#    sumnumbers = fibonacci[i] + fibonacci[i+1];
#    fibonacci.append(sumnumbers);

for i in range (2, inputIndex, 1):
    sumnumbers = fibonacci[i-1] + fibonacci[i-2];
    fibonacci.append(sumnumbers);

print(f'O resultado a seguir apresenta os {inputIndex} primeiros elementos da sequência Fibonacci:');
print(fibonacci);