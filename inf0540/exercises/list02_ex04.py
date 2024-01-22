
if __name__ == "__main__":
    v = ['A', 'E', 'I', 'O', 'U']
    letter = input("Digite uma letra: ").upper()

    if len(letter) > 1:
        print("Digite apenas uma letra")
        exit(1)

    if letter in v:
        print("Vogal")
    else:
        print("Consoante")
