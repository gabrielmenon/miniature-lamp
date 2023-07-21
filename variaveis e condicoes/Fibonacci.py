Num1 = int(0);
Num2 = int(1);
Result = (int);
InputValue = (int);

print(f'O código a seguir irá apresentar os elementos de sequencia Fibonacci.');

InputValue = int(input("Digite o número de elementos da sequência Fibonacci: "));

#print(Num1);
#print(Num2);

for count in range (0, InputValue, +1):
    result = Num1 + Num2;
    Num1 = Num2;
    Num2 = result;
    print(result);  
