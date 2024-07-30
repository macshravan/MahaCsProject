import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Button, Entry
from PIL import Image, ImageTk
import csv
import os
from datetime import datetime
from functools import partial
# Paths for menu CSV files
menu_files = {
    "rooms": "room.csv",
    "facilities": "facilities.csv",
    "beverages": "beverages.csv",
    "others": "others.csv"
}

# Dummy data for menus
dummy_image_path = "dummy.jpeg"
dummy_data = {
    "rooms": [["1", dummy_image_path, "Spring Roll", "5", "10"], ["2", dummy_image_path, "Nachos", "4", "8"]],
    "facilities": [["1", dummy_image_path, "Fried Rice", "8", "15"], ["2", dummy_image_path, "Noodles", "7", "20"]],
    "beverages": [["1", dummy_image_path, "Orange Juice", "3", "25"], ["2", dummy_image_path, "Apple Juice", "3", "30"]],
    "others": [["1", dummy_image_path, "Vanilla", "2", "50"], ["2", dummy_image_path, "Chocolate", "2", "45"]]
}

# Ensure CSV files exist with dummy data
for category, file in menu_files.items():
    if not os.path.exists(file):
        with open(file, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["RoomID", "ImagePath", "Name", "Cost", "Stock"])
            writer.writerows(dummy_data[category])

if not os.path.exists('request.csv'):
    with open('request.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Time', 'Category', 'Item', 'Quantity', 'Cost', 'Email', 'Username'])

# Variables to store the logged-in user's email and username
current_user_email = None
current_user_username = None

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
                global current_user_username
                current_user_username = row[0]  # Username is in the first column
                return True
    return False

def login():
    global current_user_email
    email = email_entry.get()
    password = password_entry.get()
    ##Loading the image using PIL
    image_path = "login.jpeg"  
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Create a Label widget to hold the image
    label = tk.Label(login_window, image=photo)
    label.pack()
    if validate_login(email, password):
        current_user_email = email
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

    image_path = "signup.jpeg"  
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(signUpWindow, image=photo)
    label.pack()
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
    home_window.title("Home Page")
    home_window.wm_state("zoomed")  # Maximized state
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
        menu_window.wm_state("zoomed")  # Maximized state

        canvas = tk.Canvas(menu_window)
        scrollbar = tk.Scrollbar(menu_window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        with open(menu_files[category], mode="r") as file:
            reader = csv.DictReader(file)
            items = list(reader)

        def go_back():
            menu_window.destroy()
        row=0
        column=0
        for idx, item in enumerate(items):
            food_id, img_path, name, cost, stock = item["RoomID"], item["ImagePath"], item["Name"], item["Cost"], item["Stock"]
            frame = tk.Frame(scrollable_frame, relief=tk.RAISED, borderwidth=2)
            if idx%4==0:
                row+=1
                column=1
                
            frame.grid(row=row, column=column, padx=10, pady=10)
            column+=1
        
            try:
                img = Image.open(img_path)
                img = img.resize((150, 150), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)
            except Exception:
                img = Image.open(dummy_image_path)
                img = img.resize((150, 150), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)

            img_label = tk.Label(frame, image=img)
            img_label.image = img
            img_label.pack(pady=5)

            name_label = tk.Label(frame, text=name, font=("Arial", 14))
            name_label.pack(pady=5)

            cost_label = tk.Label(frame, text=f"Cost: Rs.{cost}", font=("Arial", 12))
            cost_label.pack(pady=5)

            stock_label = tk.Label(frame, text=f"Stock: {stock}", font=("Arial", 12))
            stock_label.pack(pady=5)

            quantity_label = tk.Label(frame, text="Quantity:")
            quantity_label.pack(pady=5)
            quantity_entry = tk.Entry(frame)
            quantity_entry.pack(pady=5)

            add_to_cart_button = tk.Button(frame, text="Add to Cart", command=partial(add_to_cart,category, food_id, name, cost, stock, quantity_entry))
            add_to_cart_button.pack(pady=10)

        go_back_button = tk.Button(scrollable_frame, text="Go Back", command=go_back)
        go_back_button.grid(row=0, column=0, padx=10, pady=10)

    def add_to_cart(category,food_id, name, cost, stock, quantity_entry):
        try:
            quantity = int(quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity. Please enter a valid number.")
            return

        if quantity <= 0:
            messagebox.showerror("Error", "Quantity must be greater than zero.")
            return

        if quantity > int(stock):
            messagebox.showerror("Error", "Not available")
            return

        with open("view.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([category, name, cost, quantity, food_id])
        messagebox.showinfo("Success", f"Added {quantity} x {name} to cart.")
        response=messagebox.askyesno("process","do you want to continue?(yes or no)")
        print(response)
        if response:
            add_facilities()
        else:
            view_cart()
    def add_facilities():
        add_window=Toplevel(home_window)
        add_window.title("other facilities")
        add_window.geometry('600x600')
        facilities_button = tk.Button(add_window, text="facilities", font=("Arial", 14), width=20, command=lambda: show_menu("facilities"))
        facilities_button.grid(row=0, column=1, padx=20, pady=10)
        beverages_button = tk.Button(add_window, text="beverages", font=("Arial", 14), width=20, command=lambda: show_menu("beverages"))
        beverages_button.grid(row=1, column=0, padx=20, pady=10)
        others_button = tk.Button(add_window, text="others", font=("Arial", 14), width=20, command=lambda: show_menu("others"))
        others_button.grid(row=1, column=1, padx=20, pady=10)
    def view_cart():
        cart_window = Toplevel(home_window)
        cart_window.title("Cart")
        cart_window.wm_state("zoomed")  # Maximized state

        with open("view.csv", mode="r") as file:
            reader = csv.reader(file)
            cart_items = list(reader)

        if not cart_items:
            messagebox.showinfo("Cart", "Your cart is empty.")
            cart_window.destroy()
            return

        total_cost = 0
        for idx, item in enumerate(cart_items):
            category, name, cost, quantity, food_id = item
            quantity = int(quantity)
            cost = int(cost)
            total_cost += cost * quantity
            item_label = tk.Label(cart_window, text=f"Item: {name}, Quantity: {quantity}, Cost: Rs.{cost * quantity:.2f}", font=("Arial", 12))
            item_label.pack(pady=5)

        total_cost_label = tk.Label(cart_window, text=f"Total Cost: Rs.{total_cost:.2f}", font=("Arial", 14, "bold"))
        total_cost_label.pack(pady=10)

        def checkout():
            with open("view.csv", mode="r") as file:
                reader = csv.reader(file)
                cart_items = list(reader)

            total_cost = sum(int(item[2]) * int(item[3]) for item in cart_items)
            messagebox.showinfo("Checkout", f"Total cost: Rs.{total_cost:.2f}\nThank you for your purchase!")

            # Log the request
            with open("request.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                for item in cart_items:
                    category, name, cost, quantity, food_id = item
                    writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), category, name, quantity, cost, current_user_email, current_user_username])

            # Update stock
            for item in cart_items:
                category, name, cost, quantity, food_id = item
                quantity = int(quantity)
                menu_file = menu_files[category]
                updated_items = []
                print(item,"items")

                with open(menu_file, mode="r") as file:
                    reader = csv.DictReader(file)
                    items = list(reader)
                    for menu_item in items:
                        print(menu_item,"menu")
                        if menu_item["RoomID"] == food_id:
                            menu_item["Stock"] = str(int(menu_item["Stock"]) - quantity)
                        updated_items.append(menu_item)
                print(updated_items,"updated")

                with open(menu_file, mode="w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=["RoomID", "ImagePath", "Name", "Cost", "Stock"])
                    writer.writeheader()
                    writer.writerows(updated_items)

            # Clear the cart after checkout
            with open("view.csv", mode="w", newline="") as file:
                file.truncate()

            cart_window.destroy()

        checkout_button = tk.Button(cart_window, text="Pay", command=checkout)
        checkout_button.pack(pady=20)

    rooms_button = tk.Button(menu_frame, text="rooms", font=("Arial", 14), width=20, command=lambda: show_menu("rooms"))
    rooms_button.grid(row=0, column=0, padx=20, pady=10)

    view_cart_button = tk.Button(home_window, text="View Cart", font=("Arial", 14), command=view_cart)
    view_cart_button.pack(pady=20)

    def on_closing():
        root.deiconify()
        home_window.destroy()

    home_window.protocol("WM_DELETE_WINDOW", on_closing)
root = tk.Tk()
root.title('FIKA')
root.wm_state('zoomed')  # Maximized stateh

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
