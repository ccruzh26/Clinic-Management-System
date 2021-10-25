# =========================== Importing all the necessary modules ============================#
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from admin.admin_login_interface import Adminwindow
from doctor.doctor_login_interface import Doctorwindow
from staff.staff_login_interface import Staffwindow
import winsound

# =============================== Playing Music ================================#
winsound.PlaySound('C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\SmoothJazz.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

class Firstwindow:
    # =============================== Creating Tkinter Window ================================#
    def __init__(self):
        self.wn = Tk()
        self.wn.title("Softwarica Clinic")
        self.wn.geometry("1370x735+0+0")
        self.wn.config(bg="white")
        self.wn.resizable(False, False)

        # =========================== Importing all necessary photo =============================#
        self.title_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\firstwindowbackground.png")
        self.title_photo_lable = Label(self.wn, image=self.title_photo)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=370, y=0)

        self.background_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\main_logo.png")
        self.background_photo_lable = Label(self.wn, image=self.background_photo, bg="white")
        self.background_photo_lable.image = self.background_photo
        self.background_photo_lable.place(x=50, y=5)

        # ========================== Moving Pictures ==============================================#
        # ==================================== Photo - a  ====================================#
        self.a_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\a.png")
        self.a_photo_lable = Label(self.wn, image=self.a_photo, bg="white")
        self.a_photo_lable.image = self.a_photo
        self.a_photo_lable.place(x=1050, y=20)

        # ==================================== Photo - b  ====================================#
        self.b_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\b.png")
        self.b_photo_lable = Label(self.wn, image=self.b_photo, bg="white")
        self.b_photo_lable.image = self.a_photo
        self.b_photo_lable.place(x=1050, y=20)

        # ==================================== Photo - c  ====================================#
        self.c_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\c.png")
        self.c_photo_lable = Label(self.wn, image=self.c_photo, bg="white")
        self.c_photo_lable.image = self.a_photo
        self.c_photo_lable.place(x=1050, y=20)

        # ==================================== Photo - d  ====================================#
        self.d_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\d.png")
        self.d_photo_lable = Label(self.wn, image=self.d_photo, bg="white")
        self.d_photo_lable.image = self.a_photo
        self.d_photo_lable.place(x=1050, y=20)

        # ==================================== Photo - e  ====================================#
        self.e_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\e.png")
        self.e_photo_lable = Label(self.wn, image=self.e_photo, bg="white")
        self.e_photo_lable.image = self.a_photo
        self.e_photo_lable.place(x=1050, y=20)

        # ==================================== Photo - f  ====================================#
        self.f_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\f.png")
        self.f_photo_lable = Label(self.wn, image=self.f_photo, bg="white")
        self.f_photo_lable.image = self.a_photo
        self.f_photo_lable.place(x=1050, y=20)

        # ==================================== Photo - g  ====================================#
        self.g_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\g.png")
        self.g_photo_lable = Label(self.wn, image=self.g_photo, bg="white")
        self.g_photo_lable.image = self.a_photo
        self.g_photo_lable.place(x=1050, y=20)

        # ==================================== Photo - h  ====================================#
        self.h_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\h.png")
        self.h_photo_lable = Label(self.wn, image=self.h_photo, bg="white")
        self.h_photo_lable.image = self.a_photo
        self.h_photo_lable.place(x=1050, y=20)

        # ==================================== Photo - i  ====================================#
        self.i_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\i.png")
        self.i_photo_lable = Label(self.wn, image=self.i_photo, bg="white")
        self.i_photo_lable.image = self.a_photo
        self.i_photo_lable.place(x=1050, y=20)

        # ==================================== Photo - j  ====================================#
        self.j_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\j.png")
        self.j_photo_lable = Label(self.wn, image=self.j_photo, bg="white")
        self.j_photo_lable.image = self.a_photo
        self.j_photo_lable.place(x=650, y=20)
        self.x = 650
        self.slider_func()

        # =================================== HEADINGS ===================================#
        self.lb_heading_inital = Label(self.wn, text="Softwarica", bg="white", font=('Impact', 35, 'bold'), fg='red')
        self.lb_heading_inital.place(x=10, y=280)
        self.lb_heading_end = Label(self.wn, text="Clinic", bg="white", font=('Impact', 35, 'bold'), fg='blue')
        self.lb_heading_end.place(x=232,y=280)

        # =================================== SUB-HEADINGS ===================================#
        self.lb_contact_info = Label(self.wn, text="071-456789 |", bg="white", font=("Arial", 12), fg='black')
        self.lb_contact_info.place(x=50, y=340)
        self.lb_contact_info_end = Label(self.wn, text=" info@softwarica.edu.np", bg="white",font=("Arial", 12, 'underline'), fg='red')
        self.lb_contact_info_end.place(x=145, y=340)

        # =================================== First SEPERATOR ===================================#
        self.data = 10
        while self.data <= 360:
            self.seperator = Canvas(self.wn, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=380)
            self.data += 10

        # =================================== DESCRIPTION ===================================#
        self.lb_decription = Label(self.wn, text="Established in year 1998.\n\n Softwarica clinic by far is one\n  of "
                                                 "those few repuated clinic in the town.\n\nThe clinic was "
                                                 "founded\n by the money collected by the students\n"
                                                 "of Softwarica college of IT and E-Commerce.\n\n "
                                                 "With best Doctors and Sevices \n the clinic is certain to provide\n"
                                                 "the best Clinicity in the town. \n",
                                   font=('Arial', 12), justify="center", fg='black', bg="white")
        self.lb_decription.place(x=24, y=485)

        # =================================== BUTTON - WELCOME ===================================#
        self.welcome_button = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\welcomebutton.png")
        self.welcome_button_button = Button(self.wn, image=self.welcome_button,bd=0,bg='white', fg="#3498eb",
                                            activebackground="white",cursor="hand2", font=("bold", 13), height=100,
                                            width=138,relief=RAISED,command=self.second_window)
        self.welcome_button_button.image = self.welcome_button
        self.welcome_button_button.place(x=120, y=385)

        # =================================== SECOND SEPERATOR ===================================#
        self.data1 = 10
        while self.data1 <= 360:
            self.seperator1 = Canvas(self.wn, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator1.configure(bg="black")
            self.seperator1.place(x=self.data1, y=720)
            self.data1 += 10
        self.wn.mainloop()

    # ============================= Sliding Pictures====================================#
    def slider_func(self):
        self.x += 1
        if self.x == 1050:
            self.x = 650
            # time.sleep(5)
            # ========================= Swapping Function ============================#
            self.new_im = self.b_photo
            self.b_photo = self.c_photo
            self.c_photo = self.a_photo
            self.a_photo = self.d_photo
            self.d_photo = self.e_photo
            self.e_photo = self.f_photo
            self.f_photo = self.g_photo
            self.g_photo = self.h_photo
            self.h_photo = self.i_photo
            self.i_photo = self.new_im

            # ======================= Specifying Picture =============================#
            self.a_photo_lable.config(image=self.a_photo)
            self.b_photo_lable.config(image=self.b_photo)
            self.c_photo_lable.config(image=self.c_photo)
            self.d_photo_lable.config(image=self.d_photo)
            self.e_photo_lable.config(image=self.e_photo)
            self.f_photo_lable.config(image=self.f_photo)
            self.g_photo_lable.config(image=self.g_photo)
            self.h_photo_lable.config(image=self.h_photo)
            self.i_photo_lable.config(image=self.i_photo)
            self.j_photo_lable.config(image=self.j_photo)

        # ============================= Labling Photo============================================#
        self.a_photo_lable.place(x=self.x, y=20)
        self.a_photo_lable.after(2, self.slider_func)

    def second_window(self):
        # =================================== Creating Frames ===================================#
        self.frame2 = Frame(self.wn, bg="white")
        self.frame2.place(x=470, y=450)
        self.frame22 = Frame(self.wn, bg="white")
        self.frame22.place(x=470, y=150)
        self.frame3 = Frame(self.wn, bg="white")
        self.frame3.place(x=770, y=450)
        self.frame33 = Frame(self.wn, bg="white")
        self.frame33.place(x=770, y=150)
        self.frame4 = Frame(self.wn, bg="white")
        self.frame4.place(x=1070, y=450)
        self.frame44 = Frame(self.wn, bg="white")
        self.frame44.place(x=1070, y=150)

        # =========================== Importing OTHER necessary photo =============================#
        self.one_adminphoto = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\one_admin.png")
        self.one_adminphoto_lable = Label(self.wn, image=self.one_adminphoto, bg="white")
        self.one_adminphoto_lable.image = self.one_adminphoto
        self.one_adminphoto_lable.place(x=470, y=200)

        self.one_docphoto = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\one_doc.png")
        self.one_docphoto_lable = Label(self.wn, image=self.one_docphoto, bg="white")
        self.one_docphoto_lable.image = self.one_docphoto
        self.one_docphoto_lable.place(x=770, y=200)

        self.one_staffphoto = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\one_staff.png")
        self.one_staffphoto_lable = Label(self.wn, image=self.one_staffphoto, bg="white")
        self.one_staffphoto_lable.image = self.one_staffphoto
        self.one_staffphoto_lable.place(x=1070, y=200)
        # =========================== LABEL- ADMIN =============================#
        self.lb_login_admin = Label(self.frame22, text="ADMIN", bd=1, fg="black", bg="white",
                                    font=("Comic Sans MS", 18, "bold"), height=1, width=14)
        self.lb_login_admin.grid(row=0, column=0,padx=20)

        # =========================== BUTTON- ADMIN =============================#
        self.butn_login_admin = Button(self.frame2, text="ADMIN LOG IN", bd=1, bg='blue', fg="white",
                                       activebackground="white", activeforeground="indigo",cursor="hand2",
                                       font=("Comic Sans MS", 14, "bold"), height=1, width=15,
                                       command=self.open_admin_loginpage,relief=RIDGE, overrelief=RAISED)
        self.butn_login_admin.grid(row=1, column=0, padx=33, pady=5)

        # =========================== LABEL- DOCTOR =============================#
        self.lb_login_doctor = Label(self.frame33, text="DOCTOR", bd=1, fg="black", bg="white",
                                     font=("Comic Sans MS", 18, "bold"), height=1, width=14)
        self.lb_login_doctor.grid(row=0, column=0,padx=21)

        # =========================== BUTTON- DOCTOR =============================#
        self.butn_login_doctor = Button(self.frame3, text="DOCTOR LOG IN", bd=1, bg='red',fg="white",
                                        activebackground="#73C2FB", activeforeground="indigo",
                                        font=("Comic Sans MS", 14, "bold"), height=1,cursor="hand2",
                                        command=self.open_doctor_loginpage,width=15, relief=RIDGE, overrelief=RAISED)
        self.butn_login_doctor.grid(row=1, column=0, padx=34, pady=5)

        # =========================== LABEL- STAFF =============================#
        self.lb_login_staff = Label(self.frame44, text="STAFF", bd=1, fg="black", bg="white",
                                    font=("Comic Sans MS", 18, "bold"), height=1, width=14)
        self.lb_login_staff.grid(row=0, column=0,padx=20)

        # =========================== BUTTON- STAFF =============================#
        self.butn_login_staff = Button(self.frame4, text="STAFF LOG IN", bd=1, bg='white', fg="#3498eb",
                                       activebackground="#73C2FB", activeforeground="indigo",cursor="hand2",
                                       font=("Comic Sans MS", 14, "bold"), height=1, width=15,
                                       command=self.open_staff_loginpage,relief=RIDGE, overrelief=RAISED)
        self.butn_login_staff.grid(row=1, column=0, padx=33, pady=5)

    # =========================== COMMAND TO OPEN ADMIN LOGIN PAGE =============================#
    def open_admin_loginpage(self):
        self.wn.destroy()
        Adminwindow()

    # =========================== COMMAND TO OPEN DOCTOR LOGIN PAGE =============================#
    def open_doctor_loginpage(self):
        self.wn.destroy()
        Doctorwindow()

    # =========================== COMMAND TO OPEN STAFF LOGIN PAGE =============================#
    def open_staff_loginpage(self):
        self.wn.destroy()
        Staffwindow()

# ================================ Calling That Particular Function ====================#
Firstwindow()
