# =========================== Importing all the necessary modules ============================#
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from admin.connection import MyDatabase

class Doctorregistrationwindow:
    # =============================== Creating Tkinter Window ================================#
    def __init__(self):
        self.wn=Tk()
        self.wn.title("Doctor Registration")
        self.wn.geometry("1370x735+0+0")
        self.wn.resizable(False,False)
        self.show_menu()

        # =========================== Importing all necessary photo =============================#
        self.background = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\regestration.png")
        self.background_lable = Label(self.wn, image=self.background,bg="white")
        self.background_lable.image = self.background
        self.background_lable.place(x=0, y=0)

        # =================================== Creating Frames ===================================#
        self.doctor_frame=Frame(self.wn,bg="white")
        self.doctor_frame.place(x=450, y=60)

        self.doctor_frame1 = Frame(self.wn, bg="white")
        self.doctor_frame1.place(x=450, y=10)

        self.doctor_frame2 = Frame(self.wn, bg="white")
        self.doctor_frame2.place(x=620, y=10)

        # ==================================== Major Heading ====================================#
        self.lb_heading = Label(self.doctor_frame1, text="Doctor",font=('Impact',30,'bold',"underline"),justify="right", fg='red',bg="white")
        self.lb_heading.grid(row=0, column=0,columnspan=1,padx=52,pady=1)

        self.lb_heading2 = Label(self.doctor_frame2, text="Registration",font=('Impact',30,'bold',"underline"),justify="left", fg='blue',bg="white")
        self.lb_heading2.grid(row=0, column=1,columnspan=1,padx=38,pady=1)

        # ==================================== Picture With Label ====================================#
        self.title01_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\regtoppic.png")
        self.title01_photo_lable = Label(self.doctor_frame, image=self.title01_photo, bg="white")
        self.title01_photo_lable.image = self.title01_photo

        # ==================================== All Labels ====================================#
        self.lb_doctorname = Label(self.doctor_frame, text="Registration Form", bg="white", fg="Black",font=("cambria", 15, 'bold',"underline"), image=self.title01_photo, compound=TOP,justify="center")
        self.lb_doctorname.grid(row=1, column=0,columnspan=2, padx=7, pady=8)

        self.lb_doctorname = Label(self.doctor_frame, text="Doctor's Name:", bg="white", fg="Blue",font=("cambria", 15, 'bold'),justify="center")
        self.lb_doctorname.grid(row=3, column=0, padx=7, pady=3)

        self.lb_username = Label(self.doctor_frame, text="Username:", bg="white",fg="Blue", font=("cambria", 15, 'bold'),justify="center")
        self.lb_username.grid(row=5, column=0, padx=7, pady=3)

        self.lb_password = Label(self.doctor_frame, text="Password:", bg="white", fg="Blue", font=("cambria", 15, 'bold'),justify="center")
        self.lb_password.grid(row=7, column=0, padx=7, pady=3)

        self.lb_doctorage = Label(self.doctor_frame, text="Doctor's Age:", bg="white", fg="Blue",font=("cambria", 15, 'bold'), justify="center")
        self.lb_doctorage.grid(row=15, column=0, padx=7, pady=3)

        self.lb_doctorgender = Label(self.doctor_frame, text="Doctor's Gender:", bg="white", fg="Blue",font=("cambria", 15, 'bold'), justify="center")
        self.lb_doctorgender.grid(row=20, column=0, padx=7, pady=3)

        self.lb_doctoraddress = Label(self.doctor_frame, text="Doctor's Address:", bg="white", fg="Blue",font=("cambria", 15, 'bold'), justify="center")
        self.lb_doctoraddress.grid(row=25, column=0, padx=7, pady=3)

        self.lb_doctorqualification = Label(self.doctor_frame, text="Doctor's Qualification:", bg="white", fg="Blue",font=("cambria", 15, 'bold'), justify="center")
        self.lb_doctorqualification.grid(row=30, column=0, padx=7, pady=3)

        self.lb_doctorpassedfrom = Label(self.doctor_frame, text="Doctor's University:", bg="white", fg="Blue",font=("cambria", 15, 'bold'), justify="center")
        self.lb_doctorpassedfrom.grid(row=35, column=0, padx=7, pady=3)

        self.lb_doctorspeciality = Label(self.doctor_frame, text="Doctor's Speciality:", bg="white", fg="Blue",font=("cambria", 15, 'bold'), justify="center")
        self.lb_doctorspeciality.grid(row=40, column=0, padx=7, pady=3)

        self.lb_doctoremail = Label(self.doctor_frame, text="Doctor's Email:", bg="white", fg="Blue",font=("cambria", 15, 'bold'), justify="center")
        self.lb_doctoremail.grid(row=45, column=0, padx=7, pady=3)

        # ==================================== All Entries ====================================#
        self.ent_doctorname=Entry(self.doctor_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_doctorname.grid(row=3,column=1,padx=10,pady=3)

        self.ent_username = Entry(self.doctor_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_username.grid(row=5, column=1,padx=10, pady=3)

        self.ent_pass = Entry(self.doctor_frame, bg="white", fg="black", font=("arial", 15, "bold"), show="*",justify="center")
        self.ent_pass.grid(row=7, column=1, padx=10, pady=3)

        self.ent_doctorage=Entry(self.doctor_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_doctorage.grid(row=15, column=1, padx=10, pady=3)

        self.ent_doctorgender=Entry(self.doctor_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_doctorgender.grid(row=20, column=1, padx=10, pady=3)

        self.ent_doctoraddress=Entry(self.doctor_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_doctoraddress.grid(row=25, column=1, padx=10, pady=3)

        self.ent_doctorqualification = Entry(self.doctor_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_doctorqualification.grid(row=30, column=1, padx=10, pady=3)

        self.ent_doctorpasseedfrom=Entry(self.doctor_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_doctorpasseedfrom.grid(row=35, column=1, padx=10, pady=3)

        self.ent_doctorspeciality=Entry(self.doctor_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_doctorspeciality.grid(row=40, column=1, padx=10, pady=3)

        self.ent_email = Entry(self.doctor_frame, bg="white", fg="black", font=("arial", 15, "bold"),justify="center")
        self.ent_email.grid(row=45, column=1, padx=10, pady=3)

        # ==================================== All Buttons ====================================#
        self.create_account_button_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\createaccount.png")
        self.create_account_button_photo_button = Button(self.doctor_frame,image=self.create_account_button_photo, bg='white', fg="#3498eb", activebackground="#73C2FB", cursor="hand2", font=("bold", 13),command=self.registering_doc, height=25, width=138, relief=RAISED)
        self.create_account_button_photo_button.image = self.create_account_button_photo
        self.create_account_button_photo_button.grid(row=50, columnspan=2, padx=7, pady=10)

        self.my_database=MyDatabase()
        self.wn.mainloop()

    # ==================================== Regestring the Doctor ====================================#
    def registering_doc(self):
        name=self.ent_doctorname.get()
        username=self.ent_username.get()
        password=self.ent_pass.get()
        age=self.ent_doctorage.get()
        gender=self.ent_doctorgender.get()
        address=self.ent_doctoraddress.get()
        passedfrom=self.ent_doctorpasseedfrom.get()
        speciality=self.ent_doctorspeciality.get()
        qualification=self.ent_doctorqualification.get()
        email=self.ent_email.get()
        if len(name)!=0 and len(username)!=0 and len(password)!=0 and len(age)!=0 and len(gender)!=0 and len(address)!=0 and len(passedfrom)!=0 and len(speciality)!=0 and len(qualification)!=0 and len(email)!=0:
            if age.isdigit():
                qry="INSERT INTO doctor_credentials (Doctor_Name,username,password,Doctor_Age,Doctor_Gender,Doctor_Address,Doctor_Qualification,Doctor_University,Doctor_Speciality,Doctor_Email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values=(name,username,password,age,gender,address,qualification,passedfrom,speciality,email)
                self.my_database.add_update_delete(qry,values)
                messagebox.showinfo("Regestration Successfull","Please wait until \n admin approval for login")
            else:
                messagebox.showerror("Numeric Data Needed.","Age can't be a string value")
        else:
            messagebox.showerror("Blank Space Detected","You can't leave any entry boxes empty.")

    # =================================== MENU Button ===================================#
    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        log_out = Menu(my_menu)
        my_menu.add_cascade(label="<-- Back", menu=log_out)
        log_out.add_cascade(label="<-- Back", command=self.logout)

    # =================================== Logging out ===================================#
    def logout(self):
        self.wn.destroy()
        from doctor.doctor_login_interface import Doctorwindow
        Doctorwindow()
