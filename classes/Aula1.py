from classPessoa import Pessoa

class Livro:
    def __init__(self,_titulo:str, _autor:str, _editora:str, _anoPublicaçao:int):
        self.titulo = _titulo;
        self.autor = _autor;
        self.editora = _editora;
        self.anoPublicacao = _anoPublicaçao;
        self.disponivel = True;
        self.locador = None; 

    def verificarDisponibilidade(self):
        #código para verificar se o livro está disponível ou não.
        if(self.disponivel == True):
            print(f'O livro {self.titulo} está disponível.');
        else:
            print(f'O livro {self.titulo} não está disponível.');
            print(f'Atualmente locado por: ');
            self.locador.exibirInformacoes();

    def emprestar(self, _locador: Pessoa):
        #código para emprestar o livro.
        if(self.disponivel == True):
            print(f'O livro {self.titulo} está disponível e será emprestado.');
            self.disponivel = False;
            self.locador = _locador;
                    
        else:
            print(f'O livro {self.titulo} não está disponível.');

    def devolver(self):
        #código para devolver o livro.
        if(self.disponivel == True):
            print(f'O livro {self.titulo} não está emprestado.');
        else:
            print(f'O livro {self.titulo} está emprestado e será devolvido.');
            self.disponivel = True;
            self.locador = None;

    def exibirInfos(self):
        print(self.titulo);
        print(self.autor);
        print(self.editora);
        print(self.anoPublicacao);
        print(self.disponivel);
        
livro_1 = Livro("Bíblia Sagrada", "Jesus", "Belém", -2000);
livro_2 = Livro("Harry Potter", "J. K. H.", "Brasil", 2002);

Pessoa_1 = Pessoa("João", "1234567-80", "01/01/01", "H. da Silva");
Pessoa_2 = Pessoa("Maria", "7654321-10", "02/02/02");

livro_2.emprestar(Pessoa_1);

livro_2.verificarDisponibilidade();