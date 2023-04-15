import tkinter as tk
from tkinter import ttk

def add_user():
    print("Add User")  # Placeholder for actual implementation

root = tk.Tk()

# Create app bar
app_bar = ttk.Frame(root)
app_bar.pack(side=tk.TOP,fill=tk.X)

# Create app title label
app_title = ttk.Label(app_bar,text="Nurse's Homepage")
app_title.pack(side=tk.TOP, padx=0)
Font_tuple = ("Microsoft Sans Serif", 40)
app_title.configure(font = Font_tuple)



# Create app menu
app_menu = ttk.OptionMenu(app_bar, tk.StringVar(), "Menu", "Add User", command=add_user)
app_menu.pack(side=tk.RIGHT, padx=0)
app_menu.configure(width=0)

# Create list view

Font_tuple = ("Microsoft Sans Serif", 20)
list_view = tk.Listbox(root)
list_view.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
list_view.configure(justify = 'center', font = Font_tuple)
# Add nurse names to list view (placeholder)
nurse_names = ["Nurse 1", "Nurse 2", "Nurse 3", "Nurse 4", "Nurse 5"]
for name in nurse_names:
    list_view.insert(tk.END, name)

root.mainloop()

