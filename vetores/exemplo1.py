def sumVectorIndices(numbers):
    sumVector = float(0);

    for i in range (len(numbers)):
        sumVector += numbers[i];

    return sumVector;


#vectors = [];
#sumVector = float(0);
 

#print(f'O algotirmo a seguir fará a soma de todos os elementos de um vetor.');

#print(f'Digite um número para ser inserido no vetor.\nDigite 0 (zero) para parar de inserir.');

#while(True):
#    inputValue = float(0);
#    inputValue = float(input("Digite um número: "));
    
#    if(inputValue != 0):
#        vectors.append(inputValue);

#    else:
#        break;

#print(f'Calculando a soma dos elementos...\n');

#sumVector = sumVectorIndices(vectors);

#print(f'O resultado da soma dos números informados é {sumVector}.');