from ClassAnimal import Animal;

inputName = str("");
InputSpecie = str("");
vetorAnimal = [];

while True:
    print("");
    print("Digite o nome do animal e a espécie do animal. Digite 0 (zero) para sair.")

    inputName = input("\nDigite o nome do animal: ");
    if(inputName == "0"):
        print("\nO usuário digitou 0 (zero). O programa será encerrado.\n");
        break;

    inputSpecie = input("Digite a espécie do animal: ");
    if(inputSpecie == "0"):
        print("\nO usuário digitou 0 (zero). O programa será encerrado.\n");
        break;

    else:
        animal_1 = Animal(inputName, inputSpecie);
        vetorAnimal.append(animal_1.especie);

        print(f'\nO nome do animal é: {animal_1.nome}.\nA espécie do animal é: {animal_1.especie}')

        animal_1.Emitir_Som_Animal();

print(f'As espécies de animais digitadas no programa foram: \n{vetorAnimal}');          