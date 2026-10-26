# program to find Password Policy Checker

password = input("Enter a password: ")

has_number = False

for character in password:
    if character >= "0" and character <= "9":
        has_number = True

if len(password) >= 8 and has_number:
    print("Password is accepted")
else:
    print("Password is not accepted")

    if len(password) < 8:
        print("It must have at least 8 characters")

    if has_number == False:
        print("It must contain a number")