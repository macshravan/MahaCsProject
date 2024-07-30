
import tkinter as tk
import csv
import os

def load_data():
    if os.path.exists('request.csv'):
        with open('request.csv', mode='r') as file:
            reader = csv.reader(file)
            return list(reader)
    else:
        return []

def update_csv(data):
    with open('request.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def refresh_display():
    for widget in frame.winfo_children():
        widget.destroy()

    data = load_data()

    for index, row in enumerate(data):
        row_str = tk.Label(frame, text=', '.join(row))
        row_str.grid(row=index, column=0, sticky='w')

        done_button = tk.Button(frame, text="Done", command=lambda idx=index: mark_done(idx))
        done_button.grid(row=index, column=1)

def mark_done(index):
    data = load_data()
    data.pop(index)
    update_csv(data)
    refresh_display()

root = tk.Tk()
root.title("CSV Request Viewer")
root.geometry("600x300")
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
frame = tk.Frame(canvas)

frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

refresh_display()

root.mainloop()
