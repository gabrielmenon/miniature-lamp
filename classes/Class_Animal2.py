class Animal:
    def __init__(self, _nome, _especie) -> None:

        animais = ["Gato", "Grilo", "Galo"];
        self.nome = _nome;
        self.especie  = _especie;

        if(_especie in animais):
            self.especie = _especie;
            if(_especie == "Galo"):
                self.sound = "Cocoricó";
            if(_especie == "Gato"):
                self.sound = "Miau";
            if(_especie == "Grilo"):
                self.sound = "Cricri"
        
        else:
            raise Exception("Especie not defined");
            
    def show(self):
        print(f'O animal é da espécie: {self.especie}');
        print(f'O nome do {self.especie} é {self.nome}');

    def Emitir_Som(self):
        print(f'O {self.especie} fez {self.sound}');

