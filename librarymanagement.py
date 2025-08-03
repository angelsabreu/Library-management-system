import tkinter as tk
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self, master):
        self.master = master
        master.title("Library Management System")
        master.geometry("800x600")

        self.books = {
            "Don Quixote": True,
            "Alice's Adventures in Wonderland": True,
            "The Adventures of Huckleberry Finn": True,
            "The Adventures of Tom Sawyer": True,
            "Treasure Island": True,
            "Pride and Prejudice": True,
            "Wuthering Heights": True,
            "Jane Eyre": True,
            "Moby Dick": True,
            "The Scarlet Letter": True,
            "Gulliver's Travels": True,
            "The Pilgrim's Progress": True,
            "A Christmas Carol": True,
            "David Copperfield": True,
            "A Tale of Two Cities": True,
            "Little Women": True,
            "Great Expectations": True,
            "The Hobbit, or, There and Back Again": True,
            "Frankenstein, or, the Modern Prometheus": True,
            "Oliver Twist": True,
            "Uncle Tom's Cabin": True,
            "Crime and Punishment": True,
            "Madame Bovary: Patterns of Provincial life": True,
            "The Return of the King": True,
            "Dracula": True,
            "The Three Musketeers": True,
            "Brave New World": True,
            "War and Peace": True,
            "To Kill a Mockingbird": True,
            "The Wizard of Oz": True,
            "Les Misérables": True,
            "The Secret Garden": True,
            "Animal Farm": True,
            "The Great Gatsby": True,
            "The Little Prince": True,
            "The Call of the Wild": True,
            "20,000 Leagues Under the Sea": True,
            "Anna Karenina": True,
            "The Wind in the Willows": True,
            "The Picture of Dorian Gray": True,
            "The Grapes of Wrath": True,
            "Sense and Sensibility": True,
            "The Last of the Mohicans": True,
            "Tess of the d'Urbervilles": True,
            "Harry Potter and the Sorcerer's Stone": True,
            "Heidi": True,
            "Ulysses": True,
            "The Complete Sherlock Holmes": True,
            "The Count of Monte Cristo": True,
            "The Old Man and the Sea": True,
            "The Lion, the Witch, and the Wardrobe": True,
            "The Hunchback of Notre Dame": True,
            "Pinocchio": True,
            "One Hundred Years of Solitude": True,
            "Ivanhoe": True,
            "The Red Badge of Courage": True,
            "Anne of Green Gables": True,
            "Black Beauty": True,
            "Peter Pan": True,
            "A Farewell to Arms": True,
            "The House of the Seven Gables": True,
            "Lord of the Flies": True,
            "The Prince and the Pauper": True,
            "A Portrait of the Artist as a Young Man": True,
            "Lord Jim": True,
            "Harry Potter and the Chamber of Secrets": True,
            "The Red & the Black": True,
            "The Stranger": True,
            "The Trial": True,
            "Lady Chatterley's Lover": True,
            "Kidnapped: The Adventures of David Balfour": True,
            "The Catcher in the Rye": True,
            "Fahrenheit 451": True,
            "A Journey to the Center of the Earth": True,
            "Vanity Fair": True,
            "All Quiet on the Western Front": True,
            "Gone with the Wind": True,
            "My Ántonia": True,
            "Of Mice and Men": True,
            "The Vicar of Wakefield": True,
            "A Connecticut Yankee in King Arthur's Court": True,
            "White Fang": True,
            "Fathers and Sons": True,
            "Doctor Zhivago": True,
            "The Decameron": True,
            "Nineteen Eighty-Four": True,
            "The Jungle": True,
            "The Da Vinci Code": True,
            "Persuasion": True,
            "Mansfield Park": True,
            "Candide": True,
            "For Whom the Bell Tolls": True,
            "Far from the Madding Crowd": True,
            "The Fellowship of the Ring": True,
            "The Return of the Native": True,
            "Sons and Lovers": True,
            "Charlotte's Web": True,
            "The Swiss Family Robinson": True,
            "Bleak House": True,
            "Père Goriot": True,
            "Utopia": True,
            "The History of Tom Jones, a Foundling": True,
            "Harry Potter and the Prisoner of Azkaban": True,
            "Kim": True,
            "The Sound and the Fury": True,
            "Harry Potter and the Goblet of Fire": True,
            "The Mill on the Floss": True,
            "A Wrinkle in Time": True,
            "The Hound of the Baskervilles": True,
            "The Two Towers": True,
            "The War of the Worlds": True,
            "Middlemarch": True,
            "The Age of Innocence": True,
            "The Color Purple": True,
            "Northanger Abbey": True,
            "East of Eden": True,
            "On the Road": True,
            "Catch-22": True,
            "Around the World in Eighty Days": True,
            "Hard Times": True,
            "Beloved": True,
            "Mrs. Dalloway": True,
            "To the Lighthouse": True,
            "The Magician's Nephew": True,
            "Harry Potter and the Order of the Phoenix": True,
            "The Sun Also Rises": True,
            "The Good Earth": True,
            "Silas Marner": True,
            "Love in the Time of Cholera": True,
            "Rebecca": True,
            "Jude the Obscure": True,
            "Twilight": True,
            "A Passage to India": True,
            "The Plague": True,
            "Nicholas Nickleby": True,
            "The Pearl": True,
            "Ethan Frome": True,
            "The Tale of Genji": True,
            "The Giver": True,
            "The Alchemist": True,
            "The Strange Case of Dr. Jekyll and Mr. Hyde": True,
            "Robinson Crusoe": True,
            "Tender is the Night": True,
            "The Idiot": True,
            "Hatchet": True,
            "The Kite Runner": True,
            "One Flew Over the Cuckoo's Nest": True,
            "The Portrait of a Lady": True,
            "The Outsiders": True,
            "Ben-Hur": True,
            "The Mayor of Casterbridge": True,
            "Cry, The Beloved Country": True,
            "The Last Battle": True,
            "Captains Courageous": True,
            "The Castle": True,
            "The Metamorphosis": True,
            "The Magic Mountain (Der Zauberberg)": True,
            "James and the Giant Peach": True,
            "The Horse and His Boy": True,
            "Angels & Demons": True,
            "The Voyage of the Dawn Treader": True,
            "The Bell Jar": True,
            "Women in Love": True,
            "The Yearling": True,
            "O Pioneers!": True,
            "The Handmaid's Tale": True,
            "The Moonstone": True,
            "The Old Curiosity Shop": True,
            "Little Dorrit": True,
            "Prince Caspian: The Return to Narnia": True,
            "Sister Carrie": True,
            "The Silver Chair": True,
            "The Hunger Games": True,
            "This Side of Paradise": True,
            "Eugénie Grandet": True,
            "Of Human Bondage": True,
            "Dream of the Red Chamber": True,
            "Life of Pi": True,
            "Harry Potter and the Deathly Hallows": True,
            "Invisible Man": True,
            "Steppenwolf": True,
            "The Sorrows of Young Werther": True,
            "Bridge to Terabithia": True,
            "The Invisible Man": True,
            "Holes": True,
            "Siddhartha": True,
            "A Tree Grows in Brooklyn": True,
            "Through the Looking-Glass, and What Alice Found There": True,
            "In Cold Blood": True,
            "The House of the Spirits": True,
            "Adam Bede": True,
            "The Betrothed": True,
            "The Book Thief": True,
            "Their Eyes Were Watching God": True,
            "One Day in the Life of Ivan Denisovich": True,
            "The Sea Wolf": True,
            "Catching Fire": True,
            "Roll of Thunder, Hear My Cry": True,
            "Death Comes for the Archbishop": True,
            "The House of Mirth": True
        }

        # Book Entry
        self.book_entry = tk.Entry(master, width=40, font=("Arial", 14))
        self.book_entry.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Search Book", 
                  command=self.search_book, 
                  font=("Arial", 12)).grid(row=0, 
                                           column=0, 
                                           padx=5)
        tk.Button(btn_frame, text="Check Existence", 
                  command=self.check_book_exists, 
                  font=("Arial", 12)).grid(row=0, 
                                           column=1, 
                                           padx=5)
        tk.Button(btn_frame, text="Reserve Book", 
                  command=self.reserve_book, 
                  font=("Arial", 12)).grid(row=0, 
                                           column=2, 
                                           padx=5)
        tk.Button(btn_frame, text="Show All Books", 
                  command=self.show_all_books, 
                  font=("Arial", 12)).grid(row=0, 
                                           column=3, 
                                           padx=5)
        tk.Button(btn_frame, text="Unreserve Book", 
                  command=self.unreserve_book, 
                  font=("Arial", 12)).grid(row=0, 
                                           column=4, 
                                           padx=5)

        # Listbox to show books
        self.listbox = tk.Listbox(master, width=60, height=15, font=("Arial", 12))
        self.listbox.pack(pady=20)
        self.show_all_books()

    def show_all_books(self):
        self.listbox.delete(0, tk.END)
        for book, available in self.books.items():
            status = "Available" if available else "Reserved"
            self.listbox.insert(tk.END, f"{book} - {status}")

    def search_book(self):
        name = self.book_entry.get().strip()
        found = False
        self.listbox.delete(0, tk.END)
        for book, available in self.books.items():
            if name.lower() in book.lower():
                status = "Available" if available else "Reserved"
                self.listbox.insert(tk.END, f"{book} - {status}")
                found = True
        if not found:
            messagebox.showinfo("Search Result", f"No books found matching '{name}'.")

    def check_book_exists(self):
        name = self.book_entry.get().strip()
        if name in self.books:
            status = "Available" if self.books[name] else "Reserved"
            messagebox.showinfo("Book Found", f"'{name}' exists in the library. Status: {status}")
        else:
            messagebox.showerror("Book Not Found", f"'{name}' does not exist in the library.")

    def reserve_book(self):
        name = self.book_entry.get().strip()
        if name in self.books:
            if self.books[name]:
                self.books[name] = False
                messagebox.showinfo("Reserved", f"You have reserved '{name}'.")
                self.show_all_books()
            else:
                messagebox.showwarning("Already Reserved", f"'{name}' is already reserved.")
        else:
            messagebox.showerror("Book Not Found", f"'{name}' does not exist in the library.")
    
    def unreserve_book(self):
        name = self.book_entry.get().strip()
        if name in self.books:
            if not self.books[name]:
                self.books[name] = True
                messagebox.showinfo("Unreserved", f"'{name}' has been unreserved.")
                self.show_all_books()
            else:
                messagebox.showwarning("Not Reserved", f"'{name}' is not currently reserved.")
        else:
            messagebox.showerror("Book Not Found", f"'{name}' does not exist in the library.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
