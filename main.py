import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Button, Entry
from PIL import Image, ImageTk
import csv
import os

# Paths for menu CSV files
menu_files = {
    "Starters": "starters.csv",
    "Chinese": "chinese.csv",
    "Juices": "juices.csv",
    "Ice Cream": "icecream.csv"
}

# Dummy data for menus
dummy_image_path = "/home/pvshravan/Desktop/meena/CS PROJECT/dummy.jpeg"
dummy_data = {
    "Starters": [[dummy_image_path, "Spring Roll", "5"], ["Nachos", dummy_image_path, "4"]],
    "Chinese": [[dummy_image_path, "Fried Rice", "8"], ["Noodles", dummy_image_path, "7"]],
    "Juices": [[dummy_image_path, "Orange Juice", "3"], ["Apple Juice", dummy_image_path, "3"]],
    "Ice Cream": [[dummy_image_path, "Vanilla", "2"], ["Chocolate", dummy_image_path, "2"]]
}

# Ensure CSV files exist with dummy data
for category, file in menu_files.items():
    if not os.path.exists(file):
        with open(file, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(dummy_data[category])

# Function to check if a user exists in the CSV file
def user_exists(email):
    if not os.path.exists('user.csv'):
        return False
    with open('user.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == email:  # Email is in the second column
                return True
    return False

# Function to add a new user to the CSV file
def add_user(username, email, password):
    with open('user.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, email, password])

# Function to validate user login
def validate_login(email, password):
    if not os.path.exists('user.csv'):
        return False
    with open('user.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == email and row[2] == password:  # Email is in the second column, password in the third
                return True
    return False

def login():
    email = email_entry.get()
    password = password_entry.get()
    if validate_login(email, password):
        messagebox.showinfo("Login Success", "Logged in successfully!")
        login_window.destroy()
        home_page()
    else:
        messagebox.showerror("Login Error", "Invalid email or password.")

def mainlogin():
    global email_entry, password_entry, login_window
    login_window = Toplevel(root)
    login_window.title('Login')
    login_window.geometry('400x400')  # Normal window size

    email_label = tk.Label(login_window, text="Email:")
    email_label.pack(pady=10)
    email_entry = tk.Entry(login_window)
    email_entry.pack(pady=10)

    password_label = tk.Label(login_window, text="Password:")
    password_label.pack(pady=10)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=10)

    login_button = tk.Button(login_window, text="Login", command=login)
    login_button.pack(pady=20)

def signUp():
    signUpWindow = Toplevel(root)
    signUpWindow.title('Sign Up')
    signUpWindow.geometry('400x400')  # Normal window size

    username_label = tk.Label(signUpWindow, text="Username:")
    username_label.pack(pady=10)
    username_entry = tk.Entry(signUpWindow)
    username_entry.pack(pady=10)

    email_label = tk.Label(signUpWindow, text="Email:")
    email_label.pack(pady=10)
    email_entry = tk.Entry(signUpWindow)
    email_entry.pack(pady=10)

    password_label = tk.Label(signUpWindow, text="Password:")
    password_label.pack(pady=10)
    password_entry = tk.Entry(signUpWindow, show="*")
    password_entry.pack(pady=10)

    def processSignUp():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        if user_exists(email):
            messagebox.showerror("Sign Up Error", "User already exists.")
        else:
            add_user(username, email, password)
            messagebox.showinfo("Sign Up Success", "Signed up successfully!")
            signUpWindow.destroy()

    signUpButton = tk.Button(signUpWindow, text="Sign Up", command=processSignUp)
    signUpButton.pack(pady=20)

def home_page():
    home_window = Toplevel(root)
    home_window.title('Home Page')
    home_window.attributes('-zoomed', True)  # Maximized state
    root.withdraw()

    welcome_label = tk.Label(home_window, text="Welcome to the Hotel Management System", font=("Arial", 18, "bold"))
    welcome_label.pack(pady=20)

    menu_label = tk.Label(home_window, text="Menu", font=("Arial", 16, "bold"))
    menu_label.pack(pady=10)

    menu_frame = tk.Frame(home_window)
    menu_frame.pack(pady=20)

    def show_menu(category):
        menu_window = Toplevel(home_window)
        menu_window.title(category)
        menu_window.attributes('-zoomed', True)  # Maximized state

        with open(menu_files[category], mode='r') as file:
            reader = csv.reader(file)
            items = list(reader)

        for idx, (img_path, name, cost) in enumerate(items):
            frame = tk.Frame(menu_window, relief=tk.RAISED, borderwidth=2)
            frame.grid(row=idx // 2, column=idx % 2, padx=10, pady=10)

            try:
                img = Image.open(img_path)
                img = img.resize((150, 150), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
            except Exception:
                img = Image.open("/home/pvshravan/Desktop/meena/CS PROJECT/dummy.jpeg")
                img = img.resize((150, 150), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)

            img_label = Label(frame, image=img)
            img_label.image = img  # Keep a reference to avoid garbage collection
            img_label.pack()

            name_label = Label(frame, text=name, font=("Arial", 14))
            name_label.pack()

            cost_label = Label(frame, text=f"Cost: ${cost}", font=("Arial", 12))
            cost_label.pack()

            quantity_label = Label(frame, text="Quantity:", font=("Arial", 12))
            quantity_label.pack()

            quantity_entry = Entry(frame)
            quantity_entry.pack()

            def add_to_cart(name=name, cost=cost, quantity_entry=quantity_entry):
                quantity = quantity_entry.get()
                if quantity.isdigit() and int(quantity) > 0:
                    messagebox.showinfo("Add to Cart", f"Added {quantity} x {name} to cart")
                else:
                    messagebox.showerror("Invalid Input", "Please enter a valid quantity")

            add_button = Button(frame, text="Add to Cart", command=add_to_cart)
            add_button.pack(pady=5)

    starters_button = tk.Button(menu_frame, text="Starters", font=("Arial", 14), width=20, command=lambda: show_menu("Starters"))
    starters_button.grid(row=0, column=0, padx=20, pady=10)
    chinese_button = tk.Button(menu_frame, text="Chinese", font=("Arial", 14), width=20, command=lambda: show_menu("Chinese"))
    chinese_button.grid(row=0, column=1, padx=20, pady=10)
    juices_button = tk.Button(menu_frame, text="Juices", font=("Arial", 14), width=20, command=lambda: show_menu("Juices"))
    juices_button.grid(row=1, column=0, padx=20, pady=10)
    icecream_button = tk.Button(menu_frame, text="Ice Cream", font=("Arial", 14), width=20, command=lambda: show_menu("Ice Cream"))
    icecream_button.grid(row=1, column=1, padx=20, pady=10)

    def on_closing():
        root.deiconify()
        home_window.destroy()

    home_window.protocol("WM_DELETE_WINDOW", on_closing)

root = tk.Tk()
root.title('FIKA')
root.attributes('-zoomed', True)  # Maximized state

welcome_label = tk.Label(root, text="Welcome to FIKA", font=("Arial", 18, "bold"))
welcome_label.pack(pady=20)

signup_label = tk.Label(root, text="Sign Up")
signup_label.pack(pady=10)

signup_button = tk.Button(root, text="Sign Up", command=signUp)
signup_button.pack(pady=10)

login_label = tk.Label(root, text="Login")
login_label.pack(pady=10)

login_button = tk.Button(root, text="Login", command=mainlogin)
login_button.pack(pady=10)

root.mainloop()


