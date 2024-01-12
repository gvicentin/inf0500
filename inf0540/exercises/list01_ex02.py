
def decompose_base10(num):
    num_str = str(num)
    print(f"{num_str[0]} centenas, "
          f"{num_str[1]} dezenas, "
          f"{num_str[2]} unidades")


if __name__ == "__main__":
    num = int(input("Informe um número de 3 dígitos: "))
    if num < 100 or num >= 1000:
        print("Número inválido")

    decompose_base10(num)
