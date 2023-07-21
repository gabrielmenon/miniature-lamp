from Class_Car import Carros;

print("O algoritmo irá simular um carro.")

inputCar = input("Digite um modelo de carro: ");

car_1 = Carros(inputCar)

while True:
    print("0 - sair.\n1 - ligar.\n2 - desligar.\n 3 - acelerar.\n4 - frear.");
    inputMenu = int(input("Digite: "));
    
    if(inputMenu == 0):
        print("Saindo do programa.");
        break;
    else:
        if(inputMenu == 1):
            car_1.Ligar();
        if(inputMenu == 2):
            car_1.Desligar();
        if(inputMenu == 3):
            car_1.Acelerar();
        if(inputMenu == 4):
            car_1.Frear();