# =========================== Importing all the necessary modules ============================#
from admin.connection import MyDatabase

class Adminbackend:
    def __init__(self):
        self.my_db = MyDatabase()
    # ============================ Login ================================#
    def check_login(self,username,password):
        if len(username)==0 or len(password)==0:
            return False
        else:
            values=self.my_db.fetchingdata_login()
            if (username==values[0][0] and password==values[0][1]):
                return True
            else:
                return False

    #============================ Services ==============================#

    def service_backend_showdata(self):
        doctor_data=[]
        qry="SELECT * from services"
        service_data=self.my_db.return_data_frmdatabase(qry)
        return service_data

    def service_add(self,ser_name, ser_type, ser_price, ser_availability,ser_prescription):
        if ser_name=="" or ser_type=="" or ser_price=="" or ser_availability=="" or ser_prescription=="":
            return False
        elif not ser_price.isdigit():
            return False
        else:
            qry = "INSERT INTO services (Service_name,Service_type,Service_price,Service_availability,Service_prescription) VALUES (%s,%s,%s,%s,%s)"
            values = (ser_name, ser_type, ser_price, ser_availability,ser_prescription)
            self.my_db.add_update_delete(qry, values)
            return True

    def service_status_update(self,row,ser_name, ser_type, ser_price, ser_availability,ser_prescription):
        qry="UPDATE services SET Service_name=%s, Service_type=%s, Service_price=%s, Service_availability=%s,Service_prescription=%s where id=%s"
        values = (ser_name, ser_type, ser_price, ser_availability,ser_prescription,row)
        self.my_db.add_update_delete(qry, values)
        return True

    def return_service_search_data(self,search_value,search_by):
        qry="SELECT * from services where "+search_by+"=%s"
        value=(search_value,)
        req_data=self.my_db.return_data_frmdatabase_wthreturn(qry,value)
        return req_data

    def delete_services(self,row):
        qry="DELETE FROM services WHERE services.id=%s"
        value=(row,)
        self.my_db.add_update_delete(qry,value)
        return True

    #============================ Medicine ==============================#

    def medicine_backend_showdata(self):
        medicine_data=[]
        qry="SELECT * from medicines"
        medicine_data=self.my_db.return_data_frmdatabase(qry)
        return medicine_data

    def medicine_add(self,med_name, med_type, med_price, med_dose, med_company, med_expiry):
        qry = "INSERT INTO medicines (Medicine_name,Medicine_type,Medicine_price,Medicine_dose,Medicine_company,Medicine_expiry) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (med_name, med_type, med_price, med_dose, med_company, med_expiry)
        self.my_db.add_update_delete(qry, values)
        return True

    def medicine_status_update(self,row,med_name, med_type, med_price, med_dose, med_company, med_expiry):
        qry="UPDATE medicines SET Medicine_name=%s, Medicine_type=%s, Medicine_price=%s, Medicine_dose=%s,Medicine_company=%s,Medicine_expiry=%s where id=%s"
        values = (med_name, med_type, med_price, med_dose, med_company, med_expiry,row)
        self.my_db.add_update_delete(qry, values)
        return True

    def return_medicine_search_data(self, search_value, search_by):
        qry = "SELECT * from medicines where " + search_by + "=%s"
        value = (search_value,)
        req_data = self.my_db.return_data_frmdatabase_wthreturn(qry, value)
        return req_data

    def delete_medicines(self,row):
        qry="DELETE FROM medicines WHERE medicines.id=%s"
        value=(row,)
        self.my_db.add_update_delete(qry,value)
        return True

    #============================ Doctor ==============================#

    def doctor_backend_showdata(self):
        doctor_data=[]
        qry="SELECT * from doctor_credentials"
        doctor_data=self.my_db.return_data_frmdatabase(qry)
        return doctor_data

    def doctor_status_update(self,row,name,age,gender,address,passedfrom,speciality,qualification,email,admin_approval):
        qry="UPDATE doctor_credentials SET Doctor_Name=%s,Doctor_Age=%s,Doctor_Gender=%s,Doctor_Address=%s,Doctor_Qualification=%s,Doctor_University=%s,Doctor_Speciality=%s,Doctor_Email=%s,Admin_Approval=%s where id=%s"
        values = (name,age,gender,address,passedfrom,speciality,qualification,email,admin_approval,row)
        self.my_db.add_update_delete(qry, values)
        return True

    def return_doctor_search_data(self,search_value,search_by):
        qry="SELECT * from doctor_credentials where "+search_by+"=%s"
        value=(search_value,)
        req_data=self.my_db.return_data_frmdatabase_wthreturn(qry,value)
        return req_data

    def delete_doctors(self,row):
        qry="DELETE FROM doctor_credentials WHERE doctor_credentials.id=%s"
        value=(row,)
        self.my_db.add_update_delete(qry,value)
        return True

    #============================ Staff ==============================#

    def staff_backend_showdata(self):
        staff_data=[]
        qry="SELECT * from staff_credentials"
        staff_data=self.my_db.return_data_frmdatabase(qry)
        return staff_data

    def staff_status_update(self, row,name,age,gender,address,passedfrom,qualification,email,admin_approval):
        qry="UPDATE staff_credentials SET Staff_Name=%s,Staff_Age=%s,Staff_Gender=%s,Staff_Address=%s,Staff_Qualification=%s,Staff_University=%s,Staff_Email=%s,Admin_approval=%s where id=%s"
        values = (name,age,gender,address,passedfrom,qualification,email,admin_approval,row)
        self.my_db.add_update_delete(qry, values)
        return True

    def return_staff_search_data(self,search_value,search_by):
        qry="SELECT * from staff_credentials where "+search_by+"=%s"
        value=(search_value,)
        req_data=self.my_db.return_data_frmdatabase_wthreturn(qry,value)
        return req_data

    def delete_staffs(self, row):
        qry = "DELETE FROM staff_credentials WHERE staff_credentials.id=%s"
        value = (row,)
        self.my_db.add_update_delete(qry, value)
        return True

    #============================ Patients ==============================#
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

    def return_patient_search_data_schedule(self,search_value):
        qry = "SELECT * from patients where Patient_Name = %s"
        value = (search_value,)
        req_data = self.my_db.return_data_frmdatabase_wthreturn(qry, value)
        return req_data

    def delete_patients(self, row):
        qry = "DELETE FROM patients WHERE patients.id=%s"
        value = (row,)
        self.my_db.add_update_delete(qry, value)
        return True

    # ============================ SCHEDULES ==============================#

    def return_all_doctorname(self):
        qry="SELECT doctor_credentials.Doctor_Name FROM doctor_credentials"
        data_reqq=self.my_db.return_data_frmdatabase(qry)
        return data_reqq

    def return_all_scheduledetail(self):
        qry="SELECT schedules.Doctor_Name, schedules.Time FROM schedules"
        dataret=self.my_db.return_data_frmdatabase(qry)
        return dataret

    def schedule_backend_showdata(self):
        schedule_data=[]
        qry="SELECT * from schedules"
        schedule_data=self.my_db.return_data_frmdatabase(qry)
        return schedule_data

    def schedule_add(self,sedule_name, sedule_time, sedule_docstatus):
        qry = "INSERT INTO schedules (Doctor_Name,Time,Doctor_availability) VALUES (%s,%s,%s)"
        values = (sedule_name, sedule_time, sedule_docstatus)
        self.my_db.add_update_delete(qry, values)
        return True

    def schedule_status_update(self,row,sedule_name, sedule_time, sedule_docstatus):
        qry="UPDATE schedules SET Doctor_Name=%s,Time=%s,Doctor_availability=%s where id=%s"
        values = (sedule_name, sedule_time, sedule_docstatus,row)
        self.my_db.add_update_delete(qry, values)
        return True

    def return_schedule_search_data(self,search_value,search_by):
        qry="SELECT * from schedules where "+search_by+"=%s"
        value=(search_value,)
        req_data=self.my_db.return_data_frmdatabase_wthreturn(qry,value)
        return req_data

    def delete_schedules(self, row):
        qry = "DELETE FROM schedules WHERE schedules.id=%s"
        value = (row,)
        self.my_db.add_update_delete(qry, value)
        return True