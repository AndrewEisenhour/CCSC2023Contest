import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
# This app works
class Employee:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, patient_name):
        self.patients.append(patient_name)

    def get_patients(self):
        return self.patients

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x250")
        self.employees = []
        self.current_employee = None

        # Create main screen with list view of employees
        self.main_screen = tk.Frame(self.root)
        self.main_screen.pack()

        self.employee_listbox = tk.Listbox(self.main_screen)
        self.employee_listbox.pack(pady=10)

        self.add_employee_button = tk.Button(self.main_screen, text="Add Employee", command=self.add_employee)
        self.add_employee_button.pack()

        self.view_employee_button = tk.Button(self.main_screen, text="View Employee", command=self.view_employee)
        self.view_employee_button.pack()

        # Create second screen for viewing and assigning patients
        self.view_employee_screen = tk.Frame(self.root)

        self.back_button = tk.Button(self.view_employee_screen, text="Back", command=self.back_to_main_screen)
        self.back_button.pack(pady=10)

        self.patient_listbox = tk.Listbox(self.view_employee_screen, selectmode="multiple")
        self.patient_listbox.pack()

        self.assign_patient_button = tk.Button(self.view_employee_screen, text="Assign Patient", command=self.assign_patient)
        self.assign_patient_button.pack(pady=10)

        self.root.mainloop()

    def add_employee(self):
        employee_name = askstring("Add Employee", "Enter Employee Name:")
        if employee_name:
            employee = Employee(employee_name)
            self.employees.append(employee)
            self.employee_listbox.insert(tk.END, employee_name)

    def view_employee(self):
        selected_employee = self.employee_listbox.get(tk.ACTIVE)
        if selected_employee:
            self.current_employee = selected_employee
            self.main_screen.pack_forget()
            self.view_employee_screen.pack()
            self.root.title(f"Viewing Employee: {self.current_employee}")
            self.update_patient_listbox()

    def back_to_main_screen(self):
        self.current_employee = None
        self.view_employee_screen.pack_forget()
        self.main_screen.pack()
        self.root.title("Employee List")

    def assign_patient(self):
        if self.current_employee:
            patient_name = askstring("Assign Patient", "Enter Patient Name:")
            if patient_name:
                for employee in self.employees:
                    if employee.name == self.current_employee:
                        employee.add_patient(patient_name)
                        self.update_patient_listbox()
                        break

    def update_patient_listbox(self):
        self.patient_listbox.delete(0, tk.END)
        if self.current_employee:
            for employee in self.employees:
                if employee.name == self.current_employee:
                    patients = employee.get_patients()
                    for patient in patients:
                        self.patient_listbox.insert(tk.END, patient)

if __name__ == '__main__':
    app = App()