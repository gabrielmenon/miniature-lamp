valor = (float);
periodo = (int);
taxa = (float);
result = (float);
resultjuros = (float);

valor = float(input("Digite o valor do boleto em R$: "));
periodo = int (input("Digite o período de dias para o pagamento após o vencimento do boleto: "));
taxa = float(input("Digite a taxa de juros em percentagem (de 0% a 100%) aplicada sobre o valor do boleto: "));

resultjuros = (valor * periodo * taxa / 100 )
result = (valor) + (resultjuros);


print(f'O valor total do boleto após o periodo de {periodo} dias com taxa de {taxa}% é de R${result:,.2f}, sendo o valor cobrado de juros igual a R${resultjuros:,.2f}');