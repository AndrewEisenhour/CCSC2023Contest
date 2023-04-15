from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.config import Config
class Patient:
    def init(self, name, assigned_employee=None):
        self.name = name
        self.assigned_employee = assigned_employee

class Employee:
    def init(self, name):
        self.name = name 
        
class AssignApp(App):
    def init(self, kwargs):
        super(AssignApp, self).init(kwargs)
        self.patients = [Patient("Patient 1"), Patient("Patient 2"), Patient("Patient 3")]
        self.employees = [Employee("Employee 1"), Employee("Employee 2"), Employee("Employee 3")]

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        self.popup = Popup(title='', content=Label(text=''), size_hint=(None, None), size=(400, 200))
        for patient in self.patients:
            patient_layout = BoxLayout(orientation='horizontal', spacing=10)
            patient_label = Label(text=patient.name)
            assigned_employee_label = Label(text=f"Assigned Employee: {patient.assigned_employee}")
            assign_button = Button(text='Assign', on_release=lambda x, patient=patient: self.show_assign_popup(patient))
            patient_layout.add_widget(patient_label)
            patient_layout.add_widget(assigned_employee_label)
            patient_layout.add_widget(assign_button)
            layout.add_widget(patient_layout)
        return layout

    def show_assign_popup(self, patient):
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        employee_label = Label(text='Select Employee:')
        employee_input = TextInput(text='', multiline=False)
        assign_button = Button(text='Assign', on_release=lambda x, employee_input=employee_input, patient=patient: self.assign_employee(patient, employee_input.text))
        content.add_widget(employee_label)
        content.add_widget(employee_input)
        content.add_widget(assign_button)
        self.popup.content = content
        self.popup.title = f'Assign Employee to {patient.name}'
        self.popup.open()
def assign_employee(self, patient, employee_name):
        if not employee_name:
            self.popup.dismiss()
            return
        employee = None
        for emp in self.employees:
            if emp.name.lower() == employee_name.lower():
                employee = emp
                break
        if employee:
            patient.assigned_employee = employee.name
            self.popup.dismiss()
        else:
            self.popup.title = 'Error'
            self.popup.content.text = f'Employee {employee_name} not found!'
Config.set('graphics', 'window_state', 'desktop')
if __name__ == 'main':
    AssignApp().run()