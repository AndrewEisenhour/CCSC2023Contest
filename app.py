import tkinter as tk
from map import getTravelTime
import json
from tkinter import messagebox
from tkinter.simpledialog import askstring
import datetime
# This app works
class Employee:
    def __init__(self, name, address, patients):
        self.name = name
        self.address = address
        self.patients = patients
        self.startTimes = []

    def add_patient(self, patient, time):
        self.patients.append(patient)
        self.startTimes.append(time)

    def get_patients(self):
        return self.patients
    
    def get_startTimes(self):
        return self.startTimes

class Patient:
    def __init__(self, name, address, careTime):
        self.name = name
        self.address = address
        self.careTime = careTime
        
class App:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry("500x250")
        self.employees = []
        self.patients = []
        self.current_employee = None
        self.employees, self.patients = self.calculate()

        # Create main screen with list view of employees
        self.main_screen = tk.Frame(self.root)
        self.main_screen.pack()

        # Create app bar
        self.app_bar = tk.Frame(self.root)
        self.app_bar.pack(side=tk.TOP,fill=tk.X)

        # Create app title label
        self.app_title = tk.Label(self.app_bar,text="Nurse's Homepage")
        self.app_title.pack(side=tk.TOP, padx=0)
        Font_tuple = ("Microsoft Sans Serif", 40)
        self.app_title.configure(font = Font_tuple)
        # Create app menu
        self.app_menu = tk.OptionMenu(self.app_bar, tk.StringVar(), "Menu", "Add User", command=self.add_employee)
        self.app_menu.pack(side=tk.RIGHT, padx=0)
        self.app_menu.configure(width=0)
        
        # Create list view of employees
        self.employee_listbox = tk.Listbox(self.main_screen)
        Font_tuple = ("Microsoft Sans Serif", 20)
        self.employee_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.employee_listbox.configure(justify = 'center', font = Font_tuple)
        self.employee_listbox.bind('<Double-1>', lambda e:self.view_employee())
        self.employee_listbox.pack(pady=10)
        for employee in self.employees:
            self.employee_listbox.insert(tk.END, employee.name)
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
            employee = Employee(employee_name, "", [])
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
            patient_address = askstring("Assign Patient", "Enter Patient Address:")
            patient_care = askstring("Assign Patient", "Enter time of care:")
            if patient_name:
                patient = Patient(patient_name, patient_address, patient_care)
                self.patients.append(patient)
                for employee in self.employees:
                    if employee.name == self.current_employee:
                        employee.add_patient(patient_name, 34)
                        self.update_patient_listbox()
                        break
        
    def update_patient_listbox(self):
        self.patient_listbox.delete(0, tk.END)
        if self.current_employee:
            for employee in self.employees:
                if employee.name == self.current_employee:
                    patients = employee.get_patients()
                    startTimes = employee.get_startTimes()
                    count = 1
                    time = datetime.datetime(100,1,1,8,0,0)
                    for i in range(len(patients)):
                        time2 = time + datetime.timedelta(0,startTimes[i])
                        self.patient_listbox.insert(tk.END, str(count) + ". " + patients[i] + " " + str(time2.time()))
                        count += 1

    def calculate(self):
        data = json.load(open('data.json'))
        employees = []
        patients = []
        for person in data["Employees"]:
                employee = Employee(person["name"], person["address"], person["patients"])
                employees.append(employee)
        for person in data["Patients"]:
                patient = Patient(person["name"], person["address"], person["careTime"])
                patients.append(patient)

        cols = len(employees)
        rows = len(patients)
        arr = [[0 for i in range(cols)] for j in range(rows)]
        minValue = 1000000000000000000
        minI = 0
        minJ = 0
        for i in range(rows):
            for j in range(cols):
                patient = patients[i]
                nurse = employees[j]
                arr[i][j]=getTravelTime(patient.address, nurse.address)
                if arr[i][j]<minValue:
                    minValue=arr[i][j]
                    minI = i
                    minJ = j
        for l in range(rows):
            employees[minJ].add_patient(patients[minI].name, minValue)
            print("Nurse " + employees[minJ].name + " has Patient " + patients[minI].name)
            for n in range(rows):
                if arr[n][minJ]!=-1:
                    arr[n][minJ]+=minValue+patients[minI].careTime
            for m in range(cols):
                arr[minI][m]=-1
            minValue=1000000000000000000
            for i in range(rows):
                for j in range(cols):
                    patient = patients[i]
                    nurse = employees[j]
                    if arr[i][j]<minValue and arr[i][j]>=0:
                        minValue=arr[i][j]
                        minI = i
                        minJ = j
        return employees, patients                   
if __name__ == '__main__':
    app = App()