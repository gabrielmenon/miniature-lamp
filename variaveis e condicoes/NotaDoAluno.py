InputNota1 = (float);
InputNota2 = (float);
InputNota3 = (float);
NotaAprovado = (int);
NotaRecuperacao = (int);
MediaFinal = (float);
result = (str);

InputNota1 = input("Digite a nota do aluno na primeira prova: ");
InputNota2 = input("Digite a nota do aluno na segunda prova: ");
InputNota3 = input("Digite a nota do aluno na terceira prova: ");

NotaAprovado = 7;
NotaRecuperacao = 5;

if(InputNota1.isdigit() and InputNota2.isdigit() and InputNota3.isdigit()):
        InputNota1 = float(InputNota1);
        InputNota2 = float(InputNota2);
        InputNota3 = float(InputNota3);

if(type(InputNota1) != float or type(InputNota2) != float or type(InputNota3) != float):
    result = "A nota não foi informada corretamente";
    print(result);
    exit();

if((InputNota1 >= 0 and InputNota1 <= 10) and (InputNota2 >= 0 and InputNota2 <= 10) and (InputNota3 >= 0 and InputNota3 <= 10)):
    MediaFinal = (InputNota1 + InputNota2 + InputNota3)/3;
    if(MediaFinal >= NotaAprovado):
        result = "O aluno foi aprovado com média final de " + str(MediaFinal);
        print(result);
        exit();
    else:
        if(MediaFinal >= NotaRecuperacao and MediaFinal <= NotaAprovado):
            result = "O aluno está em recuperação com nota igual a " + str(MediaFinal);
            print(result);
            exit();
        else:
            result = "O aluno foi reprovado com nota igual a " + str(MediaFinal);
            print(result);
            exit();
else:
    print(f'A nota informada não comprende a faixa de valores para avaliação');