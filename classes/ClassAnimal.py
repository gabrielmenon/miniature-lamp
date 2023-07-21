class Animal:
    def __init__(self, _nome: str, _especie: str) -> None:
        self.nome = _nome;
        self.especie = _especie;

    def Emitir_Som_Animal(self):

        if(self.especie == "cachorro"):
            print(f'A espécie {self.especie} emite o som: AU-AU');
        else:
            if(self.especie == "gato"):
                print(f'A espécie {self.especie} emite o som: MIAU-MIAU');
            else:
                if(self.especie == "peixe"):
                    print(f'A espécie {self.especie} emite o som: GLUB-GLUB');
                else:
                    print(f'O som da espécie "{self.especie}" não foi catalogado.')
