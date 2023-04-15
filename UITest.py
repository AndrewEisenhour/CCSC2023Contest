import tkinter as tk
from tkinter import ttk

def add_user():
    print("Add User")  # Placeholder for actual implementation

def add_patient():
    print("Add Patient")  # Placeholder for actual implementation

def show_patient_load(nurse_name):
    # Hide main screen
    main_frame.pack_forget()

    # Show patient load screen
    patient_load_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    patient_load_title.config(text=f"Patient Load - {nurse_name}")
    back_button.pack(side=tk.RIGHT)  # Show back button on right corner of app bar

def back_to_main():
    # Show main screen
    main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Hide patient load screen
    patient_load_frame.pack_forget()
    back_button.pack_forget()  # Hide back button

root = tk.Tk()

# Create main screen
main_frame = ttk.Frame(root)
main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create app bar for main screen
app_bar = ttk.Frame(main_frame)
app_bar.pack(side=tk.TOP, fill=tk.X)

# Create app title label for main screen
app_title = ttk.Label(app_bar, text="Nurses")
app_title.pack(side=tk.LEFT, padx=10)

# Create app menu for main screen
app_menu = ttk.OptionMenu(app_bar, tk.StringVar(), "Menu", "Add User", command=add_user)
app_menu.pack(side=tk.RIGHT, padx=10)
app_menu.configure(width=10)

# Create list view for main screen
list_view = tk.Listbox(main_frame)
list_view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add nurse names to list view (placeholder)
nurse_names = ["Nurse 1", "Nurse 2", "Nurse 3", "Nurse 4", "Nurse 5"]
for name in nurse_names:
    list_view.insert(tk.END, name)
    list_view.bind("<Double-Button-1>", lambda event, name=name: show_patient_load(name))

# Create patient load screen
patient_load_frame = ttk.Frame(root)

# Create app bar for patient load screen
patient_load_app_bar = ttk.Frame(patient_load_frame)
patient_load_app_bar.pack(side=tk.TOP, fill=tk.X)

# Create app title label for patient load screen
patient_load_title = ttk.Label(patient_load_app_bar, text="Patient Load")
patient_load_title.pack(side=tk.LEFT, padx=10)

# Create back button for patient load screen
back_button = ttk.Button(patient_load_app_bar, text="Back", command=back_to_main)
back_button.pack(side=tk.RIGHT, padx=10)  # Place back button on right corner of app bar
back_button.configure(width=8)

# Create list view for patient load screen
patient_list_view = tk.Listbox(patient_load_frame)
patient_list_view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create add patient button for patient load screen
add_patient_button = ttk.Button(patient_load_frame, text="Add Patient", command=add_patient)
add_patient_button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
