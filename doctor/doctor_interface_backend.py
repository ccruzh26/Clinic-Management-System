# =========================== Importing all the necessary modules ============================#
from admin.connection import MyDatabase

class Doctorbackend:
    def __init__(self):
        self.my_db = MyDatabase()

    # =================================== changing credentials==================#
    def return_doctor_search_data(self, search_value):
        qry = "SELECT doctor_credentials.password FROM doctor_credentials where username =%s"
        value = (search_value,)
        req_data = self.my_db.return_data_frmdatabase_wthreturn(qry, value)
        return req_data

    # =============================== update doctor login credential=============#
    def update_doctor_login_data(self, providedpassword, search_value):
        qry = "UPDATE doctor_credentials SET password=%s where username =%s"
        value = (providedpassword, search_value,)
        self.my_db.add_update_delete(qry, value)
        return True

    # =================================== Check existing Appointments ===================================#
    def check_existing_appoitments(self,providedvalue):
        qry = "SELECT * from schedules where Doctor_Name=%s and Booking_status IS NOT NULL"
        value = (providedvalue,)
        schedule_data = self.my_db.return_data_frmdatabase_wthreturn(qry, value)
        return len(schedule_data)

    # ============================ Appointments ==============================#
    def return_all_patientname(self):
        qry = "SELECT patients.Patient_Name FROM patients"
        data_reqq = self.my_db.return_data_frmdatabase(qry)
        return data_reqq

    def return_approved_patientname(self,reqdata):
        qry = "SELECT * from schedules where Doctor_Name=%s and Booking_status=%s"
        value = (reqdata,"Approved")
        schedule_data = self.my_db.return_data_frmdatabase_wthreturn(qry, value)
        return schedule_data

    def appointment_backend_showdata(self,data):
        schedule_data = []
        qry = "SELECT * from schedules where Doctor_Name=%s and Booking_status IS NOT NUll"
        value=(data,)
        schedule_data = self.my_db.return_data_frmdatabase_wthreturn(qry,value)
        return schedule_data

    def appointment_status_update(self, row, appointment_docsapptatus):
        qry = "UPDATE schedules SET Booking_status=%s where id=%s"
        values = (appointment_docsapptatus, row)
        self.my_db.add_update_delete(qry, values)
        return True

    def return_appointment_search_data(self, search_value, search_by,doctorname):
        qry = "SELECT * from schedules where " + search_by + "=%s and Doctor_Name=%s"
        value = (search_value,doctorname)
        req_data = self.my_db.return_data_frmdatabase_wthreturn(qry, value)
        return req_data

    #==========================Prescription=============================================#
    def add_prescription(self,givenlist):
        for i in range(len(givenlist)):
            qry="INSERT INTO prescription (patient_id,service_id,medicine_id,med_quantity) VALUES (%s,%s,%s,%s)"
            values =(givenlist[i][0],givenlist[i][1],givenlist[i][2],givenlist[i][3])
            self.my_db.add_update_delete(qry,values)
        return True

    def return_all_prescribed_data(self):
        qry="SELECT prescription.id, patients.Patient_Name, services.Service_name, services.Service_type, services.Service_price, medicines.Medicine_name, medicines.Medicine_type,medicines.Medicine_price,prescription.med_quantity FROM prescription JOIN patients ON prescription.patient_id = patients.id JOIN services ON prescription.service_id = services.id JOIN medicines ON prescription.medicine_id = medicines.id"
        prescribed_data=self.my_db.return_data_frmdatabase(qry)
        return prescribed_data

    def return_specified_prescribed_data(self,givendata):
        qry = "SELECT prescription.id, patients.Patient_Name, services.Service_name, services.Service_type, services.Service_price, medicines.Medicine_name, medicines.Medicine_type,medicines.Medicine_price,prescription.med_quantity FROM prescription JOIN patients ON prescription.patient_id = patients.id JOIN services ON prescription.service_id = services.id JOIN medicines ON prescription.medicine_id = medicines.id WHERE prescription.id = %s"
        value=(givendata,)
        specified_data=self.my_db.return_data_frmdatabase_wthreturn(qry,value)
        return specified_data

    def return_specified_prescribed_data_history(self, givendata):
        qry = "SELECT patients.Patient_Name, services.Service_name, services.Service_type, services.Service_price, medicines.Medicine_name, medicines.Medicine_type,medicines.Medicine_price,prescription.med_quantity FROM prescription JOIN patients ON prescription.patient_id = patients.id JOIN services ON prescription.service_id = services.id JOIN medicines ON prescription.medicine_id = medicines.id WHERE patients.Patient_Name = %s"
        value = (givendata,)
        specified_data = self.my_db.return_data_frmdatabase_wthreturn(qry, value)
        return specified_data

    def return_all_prescribed_patient(self):
        qry="SELECT prescription.patient_id FROM prescription"
        patient_index=self.my_db.return_data_frmdatabase(qry)
        patient_indexlst=[]
        for i in patient_index:
            patient_indexlst.append(i[0])
        realpatient_indexlist=list(set(patient_indexlst))
        reqdata =[]
        for i in realpatient_indexlist:
            qry2="SELECT patients.Patient_Name FROM `patients` where patients.id=%s"
            value=(i,)
            reqdata.append(self.my_db.return_data_frmdatabase_wthreturn(qry2,value))
        datain_sortedform=[]
        for i in reqdata:
            datain_sortedform.append(i[0])
        return datain_sortedform

    def delete_prescription(self, row):
        qry = "DELETE FROM prescription WHERE prescription.id=%s"
        value = (row,)
        self.my_db.add_update_delete(qry, value)
        return True
