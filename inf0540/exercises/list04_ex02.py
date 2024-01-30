def add_people(people):
    print("---=[ ADICIONAR PESSOA ]=---")
    name = input(">> Nome: ")
    age = int(input(">> Idade: "))
    phone = input(">> Phone: ")
    cpf = input(">> CPF: ")
    people[cpf] = {"name": name, "age": age, "phone": phone}


def list_people(people):
    print("---=[ LISTAR PESSOAS ]=---")
    for key, val in people.items():
        print(f"{key} - {val}")


if __name__ == "__main__":
    people = {}

    should_exit = 0
    while not should_exit:
        print("---=[ MENU ]=---")
        print("1 - Adicionar pessoa")
        print("2 - Listar pessoas")
        print("3 - Sair")
        option = int(input(">> Selecione uma opcao (1-3): "))

        if option == 1:
            print("")
            add_people(people)
        elif option == 2:
            print("")
            list_people(people)
        elif option == 3:
            should_exit = 1
        else:
            print(f"Opcao invalida: {option}")

        print("")
