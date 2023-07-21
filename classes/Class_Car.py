class Carros:
    def __init__(self, _modelo:str):
        models = ["Uno", "Golf", "Up"];
        self.velocidadeAtual = int(0);
        self.isLigado = False;

        if(_modelo in models):
            self.modelo = _modelo;
            if(self.modelo == "Uno"):
                self.modelo = "Uno";
                self.marca = "Volkswagen";
                self.ano = 2010
                self.velocidadeMaxima = 180;
                self.aceleracao = 5;
     
            if(self.modelo == "Golf"):
                self.modelo = "Golf";
                self.marca = "volkswagen";
                self.ano = 2018;
                self.velocidadeMaxima = 270;
                self.aceleracao = 10.4;
            if(self.modelo == "Up"):
                self.modelo = "Up";
                self.marca = "volkswagen";
                self.ano = 2019;
                self.velocidadeMaxima = 240;
                self.aceleracao = 8.5;
             
        else:
            raise Exception("Model not defined.");

    def Ligar(self):
        if(self.isLigado == False):
            self.isLigado = True;
            print(f'O {self.modelo} está ligado e funcionando.');
        else:
            print(f'O {self.modelo} já está ligado.');

    def Desligar(self):
        if(self.isLigado == False):
            print(f'O {self.modelo} já está desligado.');
        else:
            if(self.velocidadeAtual == 0):
                self.isLigado = False;
                print(f'O {self.modelo} foi desligado.');
            else:
                print(f'Não é possível desligar o carro está em movimento.')
    
    def Acelerar(self):
        if(self.isLigado == True):
            velocidadeAcelerando = self.velocidadeAtual + self.aceleracao;
            if(velocidadeAcelerando <= self.velocidadeMaxima):
                self.velocidadeAtual += self.aceleracao;
                print(f'A velocidade atual do {self.modelo} é {self.velocidadeAtual} km/h.');
            else:
                print(f'O {self.modelo} atingiu a velocidade limite igual a {self.velocidadeAtual} km/h');

        else:
            self.velocidadeAtual = self.velocidadeMaxima;
            print(f'O {self.modelo} está desligado.');

    def Frear(self):        
        if(self.isLigado == True):
            velocidadeAcelerando = self.velocidadeAtual - self.aceleracao;
            if(velocidadeAcelerando >= 0):
                self.velocidadeAtual -= self.aceleracao;
                print(f'A velocidade atual do {self.modelo} é {self.velocidadeAtual} km/h.');
            else:
                self.velocidadeAtual = 0;
                print(f'O {self.modelo} está parado com velocidade igual a {self.velocidadeAtual} km/h');

        else:
            self.velocidadeAtual = self.velocidadeMaxima;
            print(f'O {self.modelo} está desligado.');
