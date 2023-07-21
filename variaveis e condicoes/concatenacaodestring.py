nome = (str);
sobrenome = (str);
result = (str);

nome = str(input("Usuário, digite seu primeiro nome: "));
sobrenome = str(input("Usuário, digite o seu último sobrenome: "));

nome = nome.capitalize();
sobrenome = sobrenome.capitalize();

result = (nome) + (" ") + (sobrenome);

print(f'O nome do usuário é:\n{result}');