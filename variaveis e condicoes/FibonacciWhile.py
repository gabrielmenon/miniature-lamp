Num1 = int(0);
Num2 = int(1);
Count = (0);
Result = (0);

print(f'O código a seguir irá apresentar os elementos de sequencia Fibonacci.');

InputValue = int(input("Informe o número limite da sequência Fibonacci: "));

while(Result < InputValue):
    
    Result = Num1 + Num2;
    if(Result > InputValue):
        break
    Num1 = Num2;
    Num2 = Result;
    Count +=1;
    
    print(Result);

    