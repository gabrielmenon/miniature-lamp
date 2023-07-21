valor = (float);
desconto = (float);
valorcomdesconto = (float);
valordesconto = (float);

valor = float(input("Digite o valor do produto em R$: "));
desconto = float(input("Digite o desconto em percentagem (%): "));

valorcomdesconto = valor - (valor*desconto/100);
valordesconto = valor - valorcomdesconto;

print(f'O valor do produto é igual a R$% {valor:,.2f}, o valor do produto com desconto de {desconto} % é igual a R$ {valorcomdesconto:,.2f}, sendo o valor do desconto é de R$ {valordesconto:,.2f}');