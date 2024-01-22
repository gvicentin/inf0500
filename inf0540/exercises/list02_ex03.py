
if __name__ == "__main__":
    s = input("Escolha uma opcao (F/M): ").upper()
    if len(s) > 1:
        print("Opcao invalida")
        exit(1)

    if s[0] == 'F':
        print("F - Feminino")
    elif s[0] == 'M':
        print("M - Masculino")
    else:
        print("Opcao invalida")
        exit(1)
