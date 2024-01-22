
if __name__ == "__main__":
    fullname = input("Digite o nome complete: ").lower().strip()
    firstname = fullname.split(' ')[0]
    lastname = fullname.split(' ')[-1]
    mail = f"{firstname}.{lastname}"
    username = f"{firstname[0]}{lastname}"

    print(f"Fullname: {fullname.title()}")
    print(f"First Name: {firstname.title()}")
    print(f"Last Name: {lastname.title()}")
    print(f"Mail Alias: {mail}")
    print(f"Username: {username}")
