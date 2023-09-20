letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random
import tkinter as tk
from tkinter import messagebox
import random



# Function to check user login
def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "user123" and password == "password123":
        login_window.destroy()
        open_password_generator()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Function to open password generator
def open_password_generator():
    password_generator_window = tk.Tk()
    password_generator_window.title("Password Generator")

    # Rest of your password generator code (excluding the login part)
    password_generator_window.mainloop()

    # Create the main login window
login_window = tk.Tk()
login_window.title("Login")

username_label = tk.Label(login_window, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

login_button = tk.Button(login_window, text="Login", command=check_login)
login_button.pack()

login_window.mainloop()

letters_l = int(input("how many letters do you want:"))
numbers_n = int(input("how many numbers do you want"))
symbols_s = int(input("how many special characters do you want:"))
password_n = int(input("how many passwords do you want:"))

for n in range(password_n):
    password_list =[]

    for char in range(1,letters_l + 1):
       password_list.append(random.choice(letters))
    for char in range(1, numbers_n + 1):
       password_list.append(random.choice(numbers))
    for char in range(1, symbols_s + 1):
       password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password +=char

    password = "".join(password_list)
    print("password =",password)
