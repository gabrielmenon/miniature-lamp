InputAno = (int);
Ano = (int);
ProxAno = (int);
AnteriorAno = (int);
result = (str);
Checked = bool(False);

print(f'O algoritmo a seguir irá conferir se o ano informado é bissexto ou não.');
print(f'Digite o numero "sair" para encerrar o algoritmo.');

while(Checked == False):

    InputAno = input("Informe o ano para verificação: ");
    if(InputAno == "sair"):
        Checked = True;
        print(f'O programa encerrou.');
        exit();

    result = "O ano foi informado incorretamente. Verifique se foi digitado um número inteiro.";

    if(InputAno.isdigit()):
        Checked = True;
        Ano = int(InputAno);
        InputAno = int(InputAno);
        InputAno = InputAno%4;
    
        if(InputAno == 0):
            result = "O ano informado é bissexto.";
            print (result);
            ProxAno = Ano + 4;
            AnteriorAno = Ano - 4;

            print(f'O ano bissexto anterior a {Ano} é {AnteriorAno} e o ano bissexto posterior é {ProxAno}.');     
            exit();
    

        else:
            result = "O ano informado não é bissexto.";
            print(result);      
            exit();
    

    else:

        print(result);
