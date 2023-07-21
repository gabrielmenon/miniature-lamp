InputAno = (int);
Ano = (int);
ProxAno = (int);
AnteriorAno = (int);
result = (str);

InputAno = input("Informe o ano para verificação se ele é bissexto ou não: ");

result = "O ano foi informado incorretamente.";

if(InputAno.isdigit()):
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
    exit();