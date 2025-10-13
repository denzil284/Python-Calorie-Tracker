import csv
from datetime import date
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


root = tk.Tk()
root.title("Welcome To Calorie Tracker!")
root.geometry('1400x800')

container = ttk.Frame(root)
container.pack(fill="both", expand=True)

frames = {}


def add_calories(item, calories):
    with open('calorie.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item, calories, date.today()])
        messagebox.showinfo("Success", "Food added successfully!")


class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="Home Page")
        label.pack(pady=20)
        button = ttk.Button(self, text="Add Calories Manually",
                            command=lambda: controller.show_frame("ManualTrackerPage"))
        button.pack()
        view_button = ttk.Button(self, text="View Calories",
                                 command=lambda: controller.show_frame("ViewCaloriesPage"))
        view_button.pack()


class ViewCaloriesPage(ttk.Frame):

    def view_calories(self):
        tree = ttk.Treeview(self, columns=(
            "Food", "Calories", "Date"), show="headings")
        tree.heading("Food", text="Food")
        tree.heading("Calories", text="Calories")
        tree.heading("Date", text="Date")
        tree.pack()

        with open('calorie.csv', 'r', newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                tree.insert("", "end", values=row)

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.view_calories()


class ManualTrackerPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="Add your calories manually here")
        expense_lbl = ttk.Label(self, text="Item: ")
        expense_lbl.grid(column=2, row=1)
        expense_txt = ttk.Entry(self, width=10)
        expense_txt.grid(column=3, row=1)

        amount_lbl = ttk.Label(self, text="Calories: ")
        amount_lbl.grid(column=2, row=2)
        amount_txt = ttk.Entry(self, width=10)
        amount_txt.grid(column=3, row=2)
        save_btn = ttk.Button(self, text="Save",
                              command=lambda: self.add_calories(expense_txt.get(), amount_txt.get()))
        save_btn.grid(column=3, row=3)
        back_btn = ttk.Button(self, text="Homepage",
                              command=lambda: controller.show_frame("HomePage"))
        back_btn.grid(column=1, row=1)

    def add_calories(self, item, calories):
        with open('calorie.csv', 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow([item, calories, date.today()])
            messagebox.showinfo("Success", "Food added successfully!")


class App:
    def __init__(self, root):
        self.root = root
        self.frames = {}
        for F in (HomePage, ManualTrackerPage, ViewCaloriesPage):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


app = App(root)
root.mainloop()
