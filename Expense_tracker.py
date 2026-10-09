
import tkinter as tk
from tkinter import messagebox   

total = 0   

def add_expense():

    global total

    item = item_entry.get()
    amount = amount_entry.get()

    if item == "" or amount == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return

    expense_list.insert(tk.END, f"{item:<25} Rs. {amount:>10.2f}")

    total = total + amount
    total_label.config(text=f"Total: Rs. {total:.2f}")

    item_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


def delete_expense():
    
    global total

    selected = expense_list.curselection()   
    if not selected:
        messagebox.showinfo("Info", "Please select an expense to delete")
        return

    row_text = expense_list.get(selected[0])   
    amount = float(row_text.split("Rs.")[1])      

    expense_list.delete(selected[0])
    total = total - amount
    total_label.config(text=f"Total: Rs. {total:.2f}")


def clear_all():
   
    global total
    expense_list.delete(0, tk.END)
    total = 0
    total_label.config(text="Total: Rs. 0.00")


#  WINDOW 
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("380x450")


# Title
tk.Label(root, text="Expense Tracker", font=("Arial", 16, "bold")).grid(
    row=0, column=0, columnspan=2, pady=15)

# Item
tk.Label(root, text="Item:", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
item_entry = tk.Entry(root, width=25)
item_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Amount
tk.Label(root, text="Amount:", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
amount_entry = tk.Entry(root, width=25)
amount_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Buttons
tk.Button(root, text="Add Expense", width=14, command=add_expense).grid(row=3, column=0, pady=10)
tk.Button(root, text="Delete Selected", width=14, command=delete_expense).grid(row=3, column=1, pady=10)

# List of expenses 
expense_list = tk.Listbox(root, width=40, height=10, font=("Courier", 10))
expense_list.grid(row=4, column=0, columnspan=2, padx=15)

# Total
total_label = tk.Label(root, text="Total: Rs. 0.00", font=("Arial", 12, "bold"))
total_label.grid(row=5, column=0, columnspan=2, pady=10)

# Clear All
tk.Button(root, text="Clear All", width=14, command=clear_all).grid(row=6, column=0, columnspan=2)


root.mainloop()