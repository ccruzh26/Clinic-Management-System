# =========================== Importing all the necessary modules ============================#
from admin.connection import MyDatabase

class Staffbackend:
    def __init__(self):
        self.my_db = MyDatabase()

    # ============================ Patients ==============================#
    def patient_backend_showdata(self):
        patient_data=[]
        qry="SELECT * from patients"
        patient_data=self.my_db.return_data_frmdatabase(qry)
        return patient_data

    def patient_add(self,pat_name, pat_age, pat_gender, pat_weight,pat_height,pat_address,pat_contact):
        qry = "INSERT INTO patients (Patient_Name,Patient_Age,Patient_Gender,Patient_weight,Patient_Height,Patient_Adderess,Patient_Contact) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = (pat_name, pat_age, pat_gender, pat_weight,pat_height,pat_address,pat_contact)
        self.my_db.add_update_delete(qry, values)
        return True

    def patient_status_update(self,row,pat_name, pat_age, pat_gender, pat_weight,pat_height,pat_address,pat_contact):
        qry="UPDATE patients SET Patient_Name=%s,Patient_Age=%s,Patient_Gender=%s,Patient_weight=%s,Patient_Height=%s,Patient_Adderess=%s,Patient_Contact=%s where id=%s"
        values = (pat_name, pat_age, pat_gender, pat_weight,pat_height,pat_address,pat_contact,row)
        self.my_db.add_update_delete(qry, values)
        return True

    def return_patient_search_data(self,search_value,search_by):
        qry="SELECT * from patients where "+search_by+"=%s"
        value=(search_value,)
        req_data=self.my_db.return_data_frmdatabase_wthreturn(qry,value)
        return req_data

    def delete_patients(self, row):
        qry = "DELETE FROM patients WHERE patients.id=%s"
        value = (row,)
        self.my_db.add_update_delete(qry, value)
        return True

    # ============================ Appointments ==============================#
    def return_all_patientname(self):
        qry="SELECT patients.Patient_Name FROM patients"
        data_reqq=self.my_db.return_data_frmdatabase(qry)
        return data_reqq

    def appointment_backend_showdata(self):
        schedule_data=[]
        qry="SELECT * from schedules"
        schedule_data=self.my_db.return_data_frmdatabase(qry)
        return schedule_data

    def appointment_status_update(self,row, appointment_pname, appointment_by,appointment_docsapptatus):
        qry="UPDATE schedules SET Patient_Name=%s,Appointed_by=%s,Booking_status=%s where id=%s"
        values = (appointment_pname, appointment_by,appointment_docsapptatus,row)
        self.my_db.add_update_delete(qry, values)
        return True

    def return_appointment_search_data(self,search_value,search_by):
        qry="SELECT * from schedules where "+search_by+"=%s"
        value=(search_value,)
        req_data=self.my_db.return_data_frmdatabase_wthreturn(qry,value)
        return req_data

    def delete_appointments(self, row):
        qry = "UPDATE schedules SET Patient_name = NULL ,Appointed_by = NULL ,Booking_status = NULL where id=%s"
        value = (row,)
        self.my_db.add_update_delete(qry, value)
        return True

    #=================================== changing credentials==================#
    def return_staff_search_data(self, search_value):
        qry = "SELECT staff_credentials.password FROM staff_credentials where username =%s"
        value = (search_value,)
        req_data = self.my_db.return_data_frmdatabase_wthreturn(qry, value)
        return req_data

    #=============================== update staff login credential=============#
    def update_staff_login_data(self,providedpassword,search_value):
        qry = "UPDATE staff_credentials SET password=%s where username =%s"
        value = (providedpassword,search_value,)
        self.my_db.add_update_delete(qry, value)
        return True
