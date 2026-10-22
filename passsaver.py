def menu():
    print("\n====================")
    print("Password Saver v0.0.1")
    print("====================")
    print("1.Add Password")
    print("2.Show Password")
    print("3.Exit")
while True:
    menu()
    inp = int(input("\nPress a Key... "))
    if inp == 1:
        website = input("\nEnter The Website: ")
        username = input("Enter The Username: ")
        password = input("Enter The Password: ")
        namefile = input("Enter Name File: ")
        with open(f"{namefile}.txt", "w") as file:
            file.write(f"Website : {website}\n")
            file.write(f"Username : {username}\n")
            file.write(f"Password : {password}\n")
            print("\nSaved Success")
    elif inp == 2:
        names = input("Enter the name file: ")
        with open(f"{names}.txt", "r") as filee:
            print(filee.read())
    elif inp == 3:
        break
    else:
        print("Invalid Option!!!")
