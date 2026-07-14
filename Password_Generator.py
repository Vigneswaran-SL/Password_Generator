import random
characters = "abcdefghijklmnopqrstuvwxyz!@#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
choice = "y"
while choice == "y":
    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Please enter only number")
        continue
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print(password)
    choice = input("Do you want to enter another password?(y?n): ").lower()
    if choice == "n":
        print("Thank you for using password generator!")
