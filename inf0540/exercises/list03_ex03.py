
def add_product(names, counts):
    print("---=[ ADICIONAR PRODUTO ]=---")
    name = input(">> Nome do produto: ")
    count = int(input(">> Quantidade: "))
    names.append(name)
    counts.append(count)


def alter_product(names, counts):
    print("---=[ ALTERAR ESTOQUE ]=---")
    i = 0
    while i < len(names):
        print(f"{i + 1} - {names[i]}, {counts[i]}")
        i += 1

    id = int(input(f">> Selecione um produto (1-{i}): ")) - 1
    if id >= 0 and id < i:
        new_count = int(input(">> Digite nova quantidade: "))
        counts[id] = new_count
    else:
        print(f"Opcao invalida: {id}")


def remove_product(names, counts):
    print("---=[ REMOVER PRODUTO ]=---")
    i = 0
    while i < len(names):
        print(f"{i + 1} - {names[i]}, {counts[i]}")
        i += 1

    id = int(input(f">> Selecione um produto (1-{i}): ")) - 1
    if id >= 0 and id < i:
        names.pop(id)
        counts.pop(id)
    else:
        print(f"Opcao invalida: {id}")


def list_products(names, counts):
    print("---=[ ESTOQUE ]=---")
    for i in range(len(names)):
        print(f"({names[i]}, {counts[i]})")


if __name__ == "__main__":
    product_names = []
    product_counts = []

    should_exit = 0
    while not should_exit:
        print("---=[ MENU ]=---")
        print("1 - Adicionar produto")
        print("2 - Alterar estoque")
        print("3 - Remover produto")
        print("4 - Listar estoque")
        print("5 - Sair")
        option = int(input(">> Selecione uma opcao (1-5): "))

        if option == 1:
            print("")
            add_product(product_names, product_counts)
        elif option == 2:
            print("")
            alter_product(product_names, product_counts)
        elif option == 3:
            print("")
            remove_product(product_names, product_counts)
        elif option == 4:
            print("")
            list_products(product_names, product_counts)
        elif option == 5:
            should_exit = 1
        else:
            print(f"Opcao invalida: {option}")

        print("")
