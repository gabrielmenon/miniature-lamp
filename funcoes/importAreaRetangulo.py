from AreaRetangulo import CalcAreaRetangulo;
from Checktype import convertFloat;

inputAltura = str("");
inputLargura = str("");
result = str("");

print(f'O código a seguri calcula a área (cm²) de um retangulo.')

inputAltura = input("Digite a altura do retângulo em centímetros: ");
inputLargura = input("Digite a largura do retângulo em centímetros: ");

inputAltura = convertFloat(inputAltura);
inputLargura = convertFloat(inputLargura);

result = CalcAreaRetangulo(inputAltura, inputLargura);

print(f'A área do retângulo, com altura de {inputAltura} cm e largura de {inputLargura} cm, é {result} cm²');