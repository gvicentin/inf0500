def create_contact(contacts):
    print("---=[ ADICIONAR CONTATO ]=---")
    name = input(">> Nome: ")
    phone = input(">> Telefone: ")
    contacts.append({"name": name, "phone": phone})


def list_contacts(contacts):
    print("---=[ LISTA DE CONTATOS ]=---")
    i = 1
    for con in contacts:
        print(f"{i} -> {con['name']}, {con['phone']}")
        i += 1


def remove_contact(contacts):
    print("---=[ REMOVER CONTATO ]=---")
    i = 1
    for con in contacts:
        print(f"{i} -> {con['name']}, {con['phone']}")
        i += 1

    id = int(input(f">> Selecione um contato (1-{i}): ")) - 1
    if id >= 0 and id < i:
        contacts.pop(id)
    else:
        print(f"Opcao invalida: {id}")


if __name__ == "__main__":
    contacts = []

    should_exit = 0
    while not should_exit:
        print("---=[ MENU ]=---")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Remover contato")
        print("4 - Sair")
        option = int(input(">> Selecione uma opcao (1-4): "))

        if option == 1:
            print("")
            create_contact(contacts)
        elif option == 2:
            print("")
            list_contacts(contacts)
        elif option == 3:
            print("")
            remove_contact(contacts)
        elif option == 4:
            should_exit = 1
        else:
            print(f"Opcao invalida: {option}")

        print("")
