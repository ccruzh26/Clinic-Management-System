import mysql.connector

class MyDatabase:
    def __init__(self):
        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306, database='clinic_management_system')  # to access databse
        self.my_cursor = self.my_connection.cursor()
        self.fetchingdata_login()

    # =========================== FETCHING DATA FOR ADMIN LOGIN PAGE =============================#
    def fetchingdata_login(self):
        qry = "SELECT admin_credentials.admin_username, admin_credentials.admin_password FROM admin_credentials"
        self.my_cursor.execute(qry)
        data = self.my_cursor.fetchall()
        return data

    # =========================== FETCHING DATA FOR STAFF LOGIN PAGE =============================#
    def fetchingdata_staff(self):
        qry = "SELECT staff_credentials.username, staff_credentials.password, staff_credentials.Staff_name, staff_credentials.Admin_Approval FROM staff_credentials"
        self.my_cursor.execute(qry)
        data = self.my_cursor.fetchall()
        return data

    # =========================== FETCHING DATA FOR DOCTOR LOGIN PAGE =============================#
    def fetchingdata_doctor(self):
        qry = "SELECT doctor_credentials.username, doctor_credentials.password, doctor_credentials.Doctor_name, doctor_credentials.Admin_Approval FROM doctor_credentials"
        self.my_cursor.execute(qry)
        data = self.my_cursor.fetchall()
        return data

    # =========================== QUERY FOR (ADDING,UPDATING & DELETING DATA) =============================#
    def add_update_delete(self,qry,value):
        self.my_cursor.execute(qry,value)
        self.my_connection.commit()

    # ======================== QUERY FOR RETURNING DATA FROM RESPECTIVE DATABASE ==========================#
    def return_data_frmdatabase(self, qry):
        self.my_cursor.execute(qry)
        data=self.my_cursor.fetchall()
        return data

    # ===================== QUERY FOR RETURNING SPECIFIC DATA FROM RESPECTIVE DATABASE ======================#
    def return_data_frmdatabase_wthreturn(self, qry,value):
        self.my_cursor.execute(qry,value)
        data=self.my_cursor.fetchall()
        return data
