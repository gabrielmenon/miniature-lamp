valordoinvestimento = (float);
periododerendimento = (int);
taxa = (float);
result = (float);
x = 1;

valordoinvestimento = float(input("Digite o valor do investimento em R$: "));
periododerendimento = int(input("Digite o periodo de rendimento em meses: "));
taxa = float(input("Digite a taxa de rendimento da aplicação financeira em percentagem: "));

x += 1;
for x in range(periododerendimento):

result = valordoinvestimento*taxa/100;

print(f'O valor do rendimento é R${result}');

