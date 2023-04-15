from map import getTravelTime
import json
from app import Employee, Patient

data = json.load(open('data.json'))
employees = []
patients = []
for person in data["Employees"]:
        employee = Employee(person["name"], person["address"], person["patients"])
        employees.append(employee)
for person in data["Patients"]:
        patient = Patient(person["name"], person["address"], person["careTime"])
        patients.append(patient)

closestNurse = 0
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
    employees[minJ].add_patient(patients[minI])
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
                    
print(arr)