from exemplo1 import somarDoisNum;

inputnum = int(0);
resultado = int(0);
verification = (str);
checked = False;

print(f'O codigo a seguir é um somador. Difite um número para acumular com o resultado.');

while(checked == False):
    inputnum = int(input("Digite um número: "));

    resultado = somarDoisNum(resultado, inputnum);
    print(resultado);

    verification = input("Você quer continuar? (y/n): ");  

    if(verification == "N" or verification == "n"):
        checked = True;
        print(f'O código será encerrado.')
        break;

    