import tkinter as tk
from map import getTravelTime
import json
from tkinter import *
from tkinter.simpledialog import askstring
import datetime
import customtkinter

# This app works
screenWidth= 0
screenHeight = 0
curEmp = "Employee"

buttonColor = "#3b8ed0"

headerFont = ("Microsoft Sans Serif", 40)
headerHeight = 50
headerWidth = screenWidth
headerColor = ("#f69220", "gray75")

listFont = ("Microsoft Sans Serif", 20)
listWidth = 30

patientInfoFont = ("Microsoft Sans Serif", 15)
frameSeperation = 10

class Employee:
    def __init__(self, name, address, patients):
        self.name = name
        self.address = address
        self.patients = patients
        self.startTimes = []
        self.endTime = 0

    def add_patient(self, patient, time):
        self.patients.append(patient)
        self.startTimes.append(time)

    def get_patients(self):
        return self.patients
    
    def get_startTimes(self):
        return self.startTimes
    
    def get_endTime(self):
        return self.endTime

class Patient:
    def __init__(self, name, address, careTime):
        self.name = name
        self.address = address
        self.careTime = careTime
        
class App:
    def __init__(self):
        self.root = customtkinter.CTk()

        #setting tkinter window size
        screenWidth= self.root.winfo_screenwidth()
        screenHeight= self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (screenWidth, screenHeight))
        
        #Calculation
        self.employees = []
        self.patients = []
        self.current_employee = None
        self.employees, self.patients = self.calculate()

        #Background??
        bgimg=tk.PhotoImage(file="image.png")
        self.background = Label(self.root, image=bgimg)
        self.background.place(x=0,y=0, relwidth=1, relheight=1)
        
        # Create main screen with list view of employees
        self.main_screen = tk.Frame(self.root)
        self.main_screen.pack()
        
        self.main_screen2 = tk.Frame(self.root)
        self.main_screen2.pack(pady=frameSeperation)
     

        # Create app title label/HEADER
        self.app_title = customtkinter.CTkLabel(self.main_screen,text="Nurse's Homepage",fg_color=headerColor,
                                                width=screenWidth,text_color="black",height=headerHeight)
        self.app_title.pack(side=tk.TOP)
        self.app_title.configure(font = headerFont)

        # Create list view of employees
        self.employee_listbox = tk.Listbox(self.main_screen2,width=listWidth)
        self.employee_listbox.pack()
        self.employee_listbox.configure(justify = 'center', font = listFont)
        self.employee_listbox.bind('<Double-1>', lambda e:self.view_employee())
        self.employee_listbox.pack()
        for employee in self.employees:
            self.employee_listbox.insert(tk.END, employee.name)
        
        #Assign Patient Button
        self.assign_patient_button = customtkinter.CTkButton(self.main_screen2, text="Add Patient", command=self.add_patient)
        self.assign_patient_button.pack(pady=0)




        # Create second screen for viewing and assigning patients
        self.view_employee_screen = tk.Frame(self.root)
        self.view_employee_screen2 = tk.Frame(self.root)

        #Employee screen Header
        self.nurse_title=customtkinter.CTkLabel(self.view_employee_screen,fg_color=("#f69220", "gray75"),
corner_radius=0,width=screenWidth,text_color="black",height=headerHeight)
        self.nurse_title.pack(side=tk.TOP)
        self.nurse_title.configure(font = headerFont)

        #Employee screen listbox
        self.patient_listbox = tk.Listbox(self.view_employee_screen2, selectmode="extended",width=listWidth)
        self.patient_listbox.pack()
        self.patient_listbox.configure(justify = 'center', font = listFont)
        self.patient_listbox.bind('<Double-1>', lambda e:self.view_patient())

        #Employee screen back button
        self.back_button = customtkinter.CTkButton(self.view_employee_screen2, text="Back", command=self.back_to_main_screen)
        self.back_button.pack(pady=10)

        #Employee screen Assign button
        self.assign_patient_button = customtkinter.CTkButton(self.view_employee_screen2, text="Assign Patient", command=self.assign_patient)
        self.assign_patient_button.pack()

        self.root.mainloop()

    def view_employee(self):
        selected_employee = self.employee_listbox.get(tk.ACTIVE)
        if selected_employee:
            self.current_employee = selected_employee
            curEmp = self.current_employee

            self.main_screen.pack_forget()
            self.main_screen2.pack_forget()
            self.nurse_title.configure(text=curEmp+"'s Patients")
            self.view_employee_screen.pack()
            self.view_employee_screen2.pack(pady=10)
            self.root.title(f"Viewing Employee: {self.current_employee}")
            
            
            self.update_patient_listbox()

    def view_patient(self):
        selected_patient = self.patient_listbox.get(tk.ACTIVE)
        if selected_patient:
            self.current_patient = selected_patient
            length = len(selected_patient)
            patName = selected_patient[3:length]
            index = patName.find('0')
            if index == -1:
                 index = patName.find('1')
                 if index == -1:
                      index = patName.find('2')
            patName = patName[0:index-1]
            for patient in self.patients:
                 if patName.__eq__(patient.name):
                    patAddress = patient.address
                    patWork = patient.careTime

            global pop
            pop=Toplevel(self.root)
            pop.title("Patient Info")
            pop.geometry("500x200")

            patient_name = Label(pop, text="Patient Name: "+patName,fg="black",justify=LEFT,font = patientInfoFont)
            patient_name.pack()
            patient_address = Label(pop,text="Patient Address: "+patAddress, fg="black",justify=LEFT,font = patientInfoFont)
            patient_address.pack()
            patient_work = Label(pop,text="Patient Worktime: "+str(patWork), fg="black",justify=LEFT,font = patientInfoFont)
            patient_work.pack()

            pop_frame = Frame(pop)
            pop_frame.pack()
    

           

    def back_to_main_screen(self):
        self.current_employee = None
        self.view_employee_screen.pack_forget()
        self.view_employee_screen2.pack_forget()
        self.main_screen.pack()
        self.main_screen2.pack(pady=10)
        self.root.title("Employee List")

    def assign_patient(self):
        if self.current_employee:
            patient_name = askstring("Assign Patient", "Enter Patient Name:",parent=self.root)
            patient_address = askstring("Assign Patient", "Enter Patient Address:",parent=self.root)
            patient_care = askstring("Assign Patient", "Enter time of care in minutes:",parent=self.root)
            if patient_name:
                patient = Patient(patient_name, patient_address, patient_care)
                self.patients.append(patient)
                for employee in self.employees:
                    if employee.name == self.current_employee:
                        travelTime = getTravelTime(employee.address, patient_address)
                        employee.add_patient(patient_name, travelTime+employee.get_endTime())
                        employee.endTime=employee.get_endTime()+int(patient_care)*60+travelTime
                        employee.address=patient_address
                        self.update_patient_listbox()
                        break
    def add_patient(self):
            patient_name = askstring("Assign Patient", "Enter Patient Name:", parent=self.root)
            patient_address = askstring("Assign Patient", "Enter Patient Address:",parent=self.root)
            patient_care = askstring("Assign Patient", "Enter time of care in minutes:",parent=self.root)
            if patient_name:
                patient = Patient(patient_name, patient_address, patient_care)
                self.patients.append(patient)

                #Places patient with the lowest time nurse
                smallestEndTime = 1000000000000000000
                for employee in self.employees:
                        if employee.endTime < smallestEndTime:
                             chosenEmp = employee
                             smallestEndTime = employee.endTime
                travelTime = getTravelTime(chosenEmp.address, patient_address)
                chosenEmp.add_patient(patient_name, travelTime+chosenEmp.get_endTime())
                chosenEmp.endTime=chosenEmp.get_endTime()+int(patient_care)*60+travelTime
                chosenEmp.address=patient_address
                self.update_patient_listbox()
                        
    def update_patient_listbox(self):
        self.patient_listbox.delete(0, tk.END)
        format = '%I:%M %p'
        if self.current_employee:
            for employee in self.employees:
                if employee.name == self.current_employee:
                    patients = employee.get_patients()
                    startTimes = employee.get_startTimes()
                    count = 1
                    time = datetime.datetime(100,1,1,8,0,0)
                    for i in range(len(patients)):
                        timeDelta = datetime.timedelta(0, startTimes[i])
                        time2 = time + timeDelta
                        self.patient_listbox.insert(tk.END, str(count) + ". " + patients[i] + " " + str(time2.strftime(format)))
                        count += 1
    
    # A simple version of calculate to not have calls every time                    
    def calculateMock(self):
        data = json.load(open('data.json'))
        employees = []
        patients = []
        for person in data["Employees"]:
                employee = Employee(person["name"], person["address"], person["patients"])
                employees.append(employee)
        for person in data["Patients"]:
                patient = Patient(person["name"], person["address"], person["careTime"])
                patients.append(patient)
        return employees, patients
    
    # The actual calculate function
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
            employees[minJ].address=patients[minI].address
            employees[minJ].endTime=minValue+patients[minI].careTime
            for n in range(rows):
                if arr[n][minJ]!=-1:
                    arr[n][minJ]=minValue+patients[minI].careTime+getTravelTime(patients[minI].address, patients[n].address)
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