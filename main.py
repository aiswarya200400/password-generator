import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_l = int(input("How many letters do you want: "))
numbers_n = int(input("How many numbers: "))
symbols_s = int(input("How many special characters: "))
password_n = int(input("How many passwords do you want: "))

for _ in range(password_n):
    password_list = []

    for _ in range(letters_l):
        password_list.append(random.choice(letters))

    for _ in range(numbers_n):
        password_list.append(random.choice(numbers))

    for _ in range(symbols_s):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    password = "".join(password_list)
    print("Password =", password)