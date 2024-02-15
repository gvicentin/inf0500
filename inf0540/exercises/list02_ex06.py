import os

if __name__ == "__main__":
    cmd = input("Digite um comando: ")
    result = os.system(f"{cmd} > /dev/null")

    if result == 0:
        print("Comando foi executado com sucesso")
    else:
        print(f"Comando falhou com saida: {result}")
