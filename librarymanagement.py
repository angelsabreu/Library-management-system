import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

window = tk.Tk()
window.title("Library Management System")
window.geometry("800x600")

button_check = tk.Button(window,
                         text="Check Book",
                         command = lambda: check_book_exists,
                         font=("Arial", 14))
button_check.pack(pady=20)

book_entry = tk.Entry(window,
                            width=40,
                            font=("Arial", 14))
book_entry.pack(pady=10)

book_list = [
    "The Great Gatsby",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Catcher in the Rye",
    "Moby Dick",
    "The Lord of the Rings",
    "War and Peace",
    "The Odyssey",
    "Crime and Punishment"
]
def check_book_exists():
    book_name = book_entry.get()
    if book_name in book_list:
        messagebox.showinfo("Book Found", f"The book {book_name} exists in the library.")
    else:
        messagebox.showerror("Book Not Found", f"The book {book_name} does not exist in the library.")

window.mainloop()