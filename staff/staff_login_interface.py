# ====================================== Importing Necessary photos ========================================#
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from admin.connection import MyDatabase
from staff.staff_registration import Staffregistrationwindow
from staff.staff_interface import Staff_interface

class Staffwindow:
    # ====================================== Generating Windows ========================================#
    def __init__(self):
        self.wn=Tk()
        self.wn.title("Staff Login")
        self.wn.geometry("1370x735+0+0")
        self.wn.resizable(False,False)
        self.my_db = MyDatabase()

        # ====================================== Necessary Photos ========================================#
        self.title_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\ad.png")
        self.title_photo_lable = Label(self.wn, image=self.title_photo)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=0, y=0)

        self.title01_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\nurse.png")
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
        self.staff_frame=Frame(self.wn,bg="white")
        self.staff_frame.place(x=683, y=256)

        self.staff_frame1 = Frame(self.wn, bg="white")
        self.staff_frame1.place(x=683, y=177)

        self.staff_frame2 = Frame(self.wn, bg="white")
        self.staff_frame2.place(x=824, y=177)

        # ====================================== All Lables ========================================#
        self.lb_heading = Label(self.staff_frame1, text="Staff",font=('Impact',37,'bold','underline'),justify="center", fg='red',bg="white")
        self.lb_heading.grid(row=0, column=0,columnspan=1,padx=40,pady=10)

        self.lb_heading2 = Label(self.staff_frame2, text="Login",font=('Impact',37,'bold','underline'),justify="center", fg='blue',bg="white")
        self.lb_heading2.grid(row=0, column=1,columnspan=1,padx=22,pady=10)

        self.lb_username = Label(self.staff_frame, text="Username:", bg="white",fg="Blue", font=("cambria", 15, 'bold','underline'),image=self.title02_photo,compound=LEFT)
        self.lb_username.grid(row=5, column=0, padx=10, pady=5)

        self.lb_password = Label(self.staff_frame, text="Password:", bg="white", fg="Blue", font=("cambria", 15, 'bold','underline'),image=self.title03_photo,compound=LEFT)
        self.lb_password.grid(row=10, column=0, padx=10, pady=5)

        # ====================================== All Entries ========================================#
        self.ent_username = Entry(self.staff_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.ent_username.grid(row=6, column=0,padx=40, pady=5)

        self.ent_pass = Entry(self.staff_frame, bg="white", fg="black", font=("arial", 15, "bold"), show="*")
        self.ent_pass.grid(row=11, column=0, padx=40, pady=5)

        self.butn_forget = Button(self.staff_frame, text="Forgot your password?", fg="#000080", bg="white",font=("Arial", 10, "underline"),cursor="hand2",command=self.forgotpassword, relief=FLAT)
        self.butn_forget.grid(row=14, columnspan=3, pady=5)

        # ====================================== Buttons Required ========================================#
        self.ch_btn = Checkbutton(self.staff_frame, text="Remember me", bg="white", fg="Black",font=("Arial MT", 10, "bold"),cursor="hand2")
        self.ch_btn.grid(row=18, columnspan=2, padx=5, pady=2)

        self.loginbtn_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\loginbutn.png")
        self.loginbtn_photo_button = Button(self.staff_frame, image=self.loginbtn_photo,bg='white', fg="#3498eb", activebackground="#73C2FB",cursor="hand2",command=self.checking_credentials, font=("bold", 13), height=39, width=120,relief=RAISED)
        self.loginbtn_photo_button.image = self.loginbtn_photo
        self.loginbtn_photo_button.grid(row=20, columnspan=2, padx=0, pady=6)

        self.butn_dont_have_an_account = Button(self.staff_frame, text="Don't have an account? | Sign Up", fg="#000080", bg="white", font=("Arial", 10, "underline"),command=self.open_staffregpage,cursor="hand2", relief=FLAT)
        self.butn_dont_have_an_account.grid(row=22, columnspan=3, pady=5)
        self.show_menu()
        self.wn.mainloop()

    # ====================================== Open Staff Regestritation Page ========================================#
    def open_staffregpage(self):
        self.wn.destroy()
        Staffregistrationwindow()

    # ====================================== Opening Staff Dashboard ========================================#
    def open_staff_dashboard(self,usrlgn):
        self.wn.destroy()
        Staff_interface(usrlgn)

    # ====================================== Checking Credentials ========================================#
    def checking_credentials(self):
        username=self.ent_username.get().lower()
        password=self.ent_pass.get().lower()
        if len(username)==0 or len(password)==0:
            messagebox.showerror("Missing data entry","You can't leave any of the sections empty.")
        else:
            values=self.my_db.fetchingdata_staff()
            username_mylist = []
            for i in values:
                data = (i[0]).lower()
                username_mylist.append(data)
            if username in username_mylist:
                required_index=username_mylist.index(username)
                name_logged_in_user=values[required_index][0]
                if (username == values[required_index][0].lower() and password == values[required_index][1].lower()):
                    if values[required_index][3] == "yes" or values[required_index][3] == "Yes":
                        messagebox.showinfo("Login Successful",f"Welcome Mr {values[required_index][2]}")
                        self.open_staff_dashboard(name_logged_in_user)
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
        messagebox.showinfo("Service Unavailable","The system is in its inital phase."
                                                  "\n Service regarding credintials shall"
                                                  "\n be provided very soon.\n"
                                                  "Please consult admin desk for more info.")