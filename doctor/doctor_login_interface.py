# ====================================== Importing Necessary photos ========================================#
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from admin.connection import MyDatabase
from doctor.doctor_registration import Doctorregistrationwindow
from doctor.doctor_interface import Doctor_interface

class Doctorwindow:
    # ====================================== Generating Windows ========================================#
    def __init__(self):
        self.wn=Tk()
        self.wn.title("Doctor Login")
        self.wn.geometry("1370x735+0+0")
        self.wn.resizable(False,False)
        self.my_db = MyDatabase()

        # ====================================== Necessary Photos ========================================#
        self.title_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\ad.png")
        self.title_photo_lable = Label(self.wn, image=self.title_photo)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=0, y=0)

        self.title01_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\doc.png")
        self.title01_photo_lable = Label(self.wn, image=self.title01_photo,bg="white")
        self.title01_photo_lable.image = self.title01_photo
        self.title01_photo_lable.place(x=355, y=177)

        self.title02_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\username_logo.png")
        self.title02_photo_lable = Label(self.wn, image=self.title02_photo)
        self.title02_photo_lable.image = self.title02_photo

        self.title03_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\password.png")
        self.title03_photo_lable = Label(self.wn, image=self.title03_photo)
        self.title03_photo_lable.image = self.title03_photo

        # ====================================== All Frames ========================================#
        self.doctor_frame=Frame(self.wn,bg="white")
        self.doctor_frame.place(x=683, y=256)

        self.doctor_frame1 = Frame(self.wn, bg="white")
        self.doctor_frame1.place(x=683, y=177)

        self.doctor_frame2 = Frame(self.wn, bg="white")
        self.doctor_frame2.place(x=842, y=177)

        # ====================================== All Lables ========================================#
        self.lb_heading = Label(self.doctor_frame1, text="Doctor",font=('Impact',37,'bold','underline'),justify="center", fg='red',bg="white")
        self.lb_heading.grid(row=0, column=0,columnspan=1,padx=13,pady=10)

        self.lb_heading2 = Label(self.doctor_frame2, text="Login",font=('Impact',37,'bold','underline'),justify="center", fg='blue',bg="white")
        self.lb_heading2.grid(row=0, column=1,columnspan=1,padx=13,pady=10)

        self.lb_username = Label(self.doctor_frame, text="Username:", bg="white",fg="Blue", font=("cambria", 15, 'bold','underline'),image=self.title02_photo,compound=LEFT)
        self.lb_username.grid(row=5, column=0, padx=10, pady=3)

        self.lb_password = Label(self.doctor_frame, text="Password:", bg="white", fg="Blue", font=("cambria", 15, 'bold','underline'),image=self.title03_photo,compound=LEFT)
        self.lb_password.grid(row=10, column=0, padx=10, pady=3)

        # ====================================== All Entries ========================================#
        self.ent_username = Entry(self.doctor_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.ent_username.grid(row=6, column=0,padx=40, pady=3)

        self.ent_pass = Entry(self.doctor_frame, bg="white", fg="black", font=("arial", 15, "bold"), show="*")
        self.ent_pass.grid(row=11, column=0, padx=40, pady=3)

        self.butn_forget = Button(self.doctor_frame, text="Forgot your password?", fg="#000080", bg="white",font=("Arial", 10, "underline"),command=self.forgotpassword,cursor="hand2", relief=FLAT)
        self.butn_forget.grid(row=14, columnspan=3, pady=3)

        # ====================================== Buttons Required ========================================#
        self.ch_btn = Checkbutton(self.doctor_frame, text="Remember me", bg="white", fg="Black",font=("Arial MT", 10, "bold"),cursor="hand2")
        self.ch_btn.grid(row=18, columnspan=2, padx=5, pady=2)

        self.loginbtn_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\loginbutn.png")
        self.loginbtn_photo_button = Button(self.doctor_frame, image=self.loginbtn_photo,bg='white', fg="#3498eb", activebackground="#73C2FB", cursor="hand2",command=self.checking_credentials, font=("bold", 13), height=39, width=120,relief=RAISED)
        self.loginbtn_photo_button.image = self.loginbtn_photo
        self.loginbtn_photo_button.grid(row=20, columnspan=2, padx=0, pady=6)

        self.butn_dont_have_an_account = Button(self.doctor_frame, text="Don't have an account? | Sign Up", fg="#000080",cursor="hand2",bg="white", font=("Arial", 10, "underline"),command=self.open_docregpage, relief=FLAT)
        self.butn_dont_have_an_account.grid(row=22, columnspan=3, pady=7)

        self.show_menu()
        self.wn.mainloop()

    # ====================================== Open Doctor Regestritation Page ========================================#
    def open_docregpage(self):
        self.wn.destroy()
        Doctorregistrationwindow()

    # ====================================== Opening Doctor Dashboard ========================================#
    def open_doctor_dashboard(self,userlogin,userloginname):
        self.wn.destroy()
        Doctor_interface(userlogin,userloginname)

    # ====================================== Checking Credentials ========================================#
    def checking_credentials(self):
        username=self.ent_username.get().lower()
        password=self.ent_pass.get().lower()
        if len(username)==0 or len(password)==0:
            messagebox.showerror("Missing data entry","You can't leave any of the sections empty.")
        else:
            values=self.my_db.fetchingdata_doctor()
            username_mylist=[]
            for i in values:
                data = (i[0]).lower()
                username_mylist.append(data)
            if username in username_mylist:
                required_index=username_mylist.index(username)
                usrname_logged_in_user = values[required_index][0]
                name_logged_in_user=values[required_index][2]
                if (username == values[required_index][0].lower() and password == values[required_index][1].lower()):
                    if values[required_index][3] == "yes" or values[required_index][3] == "Yes":
                        messagebox.showinfo("Login Successful", f"Welcome Doctor {values[required_index][2]}")
                        self.open_doctor_dashboard(usrname_logged_in_user,name_logged_in_user)
                    else:
                        messagebox.showerror("User not authenticated","Your registration hasn't been\n approved by the admin yet.")
                else:
                    messagebox.showerror("Login Credintials didn't matched","The given username and password didn't matched")
            else:
                messagebox.showerror("User Doesn't Exist","Sorry you aren't registered yet")

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
        from interface.first_window import Firstwindow
        Firstwindow()

    # =================================== Forgot Password ==============================#
    def forgotpassword(self):
        messagebox.showinfo("Service Unavailable", "The system is in its inital phase."
                                                   "\n Service regarding credintials shall"
                                                   "\n be provided very soon.\n"
                                                   "Please consult admin desk for more info.")