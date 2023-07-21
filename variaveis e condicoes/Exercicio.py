import time;

InputValue = (int);
StopCondition = (int);

print(f'O algoritmo a seguir fará uma contagem crescente do número digitado.\n');
InputValue = int(input("Digite um número positivo: "));
StopCondition = int(input("Digite um critério de parada: "));

while(InputValue <= StopCondition):
    
    print(InputValue);
    if(InputValue >= StopCondition):
        print(f'O programa encerrou.');
    time.sleep(1);
    InputValue += 1;

