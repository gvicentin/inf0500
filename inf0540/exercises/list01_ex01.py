
def calculate_imc(weight, height):
    return weight / (height * height)


if __name__ == "__main__":
    weight = float(input("Informe o peso (kg): "))
    height = float(input("Informe a altura (m): "))
    print(f"IMC: {calculate_imc(weight, height)}")
