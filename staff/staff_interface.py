# =========================== Importing all the necessary modules ============================#
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time as tm
import datetime
from staff.staff_interface_backend import Staffbackend
from doctor.doctor_interface_backend import Doctorbackend

class Staff_interface:
    # =============================== Creating Tkinter Window ================================#
    def __init__(self,staffloggedin):
        self.wn = Tk()
        self.wn.title("Staff Panel")
        self.wn.geometry("1370x735+0+0")
        self.wn.configure(bg="white")
        self.wn.resizable(False, False)
        self.doctor_backend = Doctorbackend()
        self.staff_backend = Staffbackend()
        self.lastuserloggedin=staffloggedin
        self.update_index0=""
        self.update_index1=""

        # =========================== Importing all necessary photo =============================#
        self.title_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\staff_logooo.png")
        self.title_photo_lable = Label(self.wn, image=self.title_photo, bg="white",bd=1,borderwidth=1)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=1, y=0)


        self.title_photo01 = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\staff_board_background.png")
        self.title_photo01_lable = Label(self.wn, image=self.title_photo01,bg="white")
        self.title_photo01_lable.image = self.title_photo01
        self.title_photo01_lable.place(x=280, y=0)

        # ===========================  Necessary Frames =============================#
        self.frame1 = LabelFrame(self.wn, bg="white")
        self.frame1.place(x=1, y=270)
        self.tree_frame = Frame(self.wn, bg="white")
        self.tree_frame.place(x=285, y=0)
        self.navigation_frame = Frame(self.wn, bg="white")
        self.navigation_frame.place(x=285, y=247)
        self.navigation_frame0 = LabelFrame(self.wn, bg="white", bd=2)
        self.navigation_frame0.place(x=1100, y=0)

        # ==================================== Major Heading ====================================#
        self.lb_heading_inital = Label(self.frame1, text="Staff", bg="white", font=('Impact', 34, 'bold', 'underline'),fg='red')
        self.lb_heading_inital.grid(row=20, column=40, padx=15, pady=10)
        self.lb_heading_end = Label(self.frame1, text="Panel", bg="white", font=('Impact', 34, 'bold', 'underline'),fg='blue')
        self.lb_heading_end.grid(row=20, column=80, padx=17, pady=10)

        # =================================== Creating Frame-2 ===================================#
        self.frame2 = LabelFrame(self.wn, bg="white")
        self.frame2.place(x=1, y=350)

        # ============================ Creating Seprator and Buttons ============================#

        # =================================== First Seprator ====================================#
        # self.first_seperator = Canvas(self.frame2, width=270, height=1, bd=0, highlightthickness=0)
        # self.first_seperator.configure(bg="black")
        # self.first_seperator.grid(row=0, column=0)

        # ==================================== First Button ====================================#
        self.patient_button = Button(self.frame2, text="Patients", bg='white', fg="black", activebackground="#73C2FB",activeforeground="indigo", cursor="hand2", font=("Comic Sans MS", 15, "bold"),height=1, width=15,command=self.patientboard, relief=RIDGE, overrelief=RAISED)
        self.patient_button.grid(row=5, column=0, padx=5, pady=20)

        # =================================+ Second Seprator ===================================#
        self.second_seperator = Canvas(self.frame2, width=270, height=1, bd=0, highlightthickness=0)
        self.second_seperator.configure(bg="black")
        self.second_seperator.grid(row=10, column=0)

        # ==================================== Second Button ====================================#
        self.appointments_button = Button(self.frame2, text="Appointments", bd=1, bg='yellow', fg="black",activebackground="#73C2FB", activeforeground="indigo", cursor="hand2",font=("Comic Sans MS", 15, "bold"), height=1, width=15,command=self.appointments,relief=RIDGE, overrelief=RAISED)
        self.appointments_button.grid(row=20, column=0, padx=5, pady=20)

        # ==================================== Third Seprator ====================================#
        self.third_seperator = Canvas(self.frame2, width=270, height=1, bd=0, highlightthickness=0)
        self.third_seperator.configure(bg="black")
        self.third_seperator.grid(row=25, column=0)

        # ==================================== Third Button ====================================#
        self.credentials_button = Button(self.frame2, text="Credentials", bd=1, bg='red', fg="white", activebackground="#73C2FB",activeforeground="indigo",command=self.change_staff_credentials, font=("Comic Sans MS", 15, "bold"), height=1,cursor="hand2", width=15, relief=RIDGE, overrelief=RAISED)
        self.credentials_button.grid(row=40, column=0, padx=5, pady=20)

        # ==================================== Fourth Seprator ====================================#
        self.fourth_seperator = Canvas(self.frame2, width=270, height=1, bd=0, highlightthickness=0)
        self.fourth_seperator.configure(bg="black")
        self.fourth_seperator.grid(row=45, column=0)


        # ==================================== Fifth Button ====================================#
        self.billing_button = Button(self.frame2, text="Billing", bd=1, bg='blue', fg="white",activebackground="#73C2FB", activeforeground="indigo",command=self.bill_of_patients,font=("Comic Sans MS", 15, "bold"), height=1, cursor="hand2", width=15,relief=RIDGE, overrelief=RAISED)
        self.billing_button.grid(row=80, column=0, padx=5, pady=20)

        # ==================================== Fifth Seprator ====================================#
        self.sixth_seperator = Canvas(self.frame2, width=277, height=1, bd=0, highlightthickness=0)
        self.sixth_seperator.configure(bg="black")
        self.sixth_seperator.grid(row=85, column=0)
        self.show_menu()
        self.wn.mainloop()

    # ==================================== Menu Button ====================================#
    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        log_out = Menu(my_menu)
        my_menu.add_cascade(label="Log Out", menu=log_out)
        log_out.add_cascade(label="Log Out", command=self.logout)

    def patientboard(self):
        self.deleteframe()
        self.display_date()
        self.display_time()
        self.endphoto()
        # =================================== FIRST SEPERATOR ===================================#
        self.data0 = 22
        while self.data0 <= 790:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=9)
            self.data0 += 10
        # =================================== SECOND SEPERATOR ===================================#
        self.data = 22
        while self.data <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=70)
            self.data += 10

        #==================================== Patient Logo  ====================================#
        self.patient_photoo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\patientboard.png")
        self.patient_photoo_lable = Label(self.navigation_frame0, image=self.patient_photoo, bg="white")
        self.patient_photoo_lable.image = self.patient_photoo
        self.patient_photoo_lable.grid(row=3, column=0, padx=5)

        # ==================================== FIRST LABEL - NAME ====================================#
        self.patientboard_lb1 = Label(self.navigation_frame, text="Name of the patient", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb1.grid(row=2, column=1, padx=10, pady=10)

        # ==================================== SCEOND LABEL - AGE ====================================#
        self.patientboard_lb2 = Label(self.navigation_frame, text="Age of the patient", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb2.grid(row=3, column=1, padx=10, pady=10)

        # ==================================== THIRD LABEL - GENDER ====================================#
        self.patientboard_lb3 = Label(self.navigation_frame, text="Gender of the patient", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb3.grid(row=4, column=1, padx=10, pady=10)

        # ==================================== FOURTH LABEL - Weight ====================================#
        self.patientboard_lb4 = Label(self.navigation_frame, text="Weight of the patient", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb4.grid(row=5, column=1, padx=10, pady=10)

        # ==================================== FIFTH LABEL - Height ====================================#
        self.patientboard_lb5 = Label(self.navigation_frame, text="Height of the patient", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb5.grid(row=6, column=1, padx=10, pady=10)

        # ==================================== SIXTH LABEL - Address ====================================#
        self.patientboard_lb6 = Label(self.navigation_frame, text="Address of the patient", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb6.grid(row=7, column=1, padx=10, pady=10)

        # ==================================== Seventh LABEL - Contact ====================================#
        self.patientboard_lb8 = Label(self.navigation_frame, text="Contact number of the patient", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb8.grid(row=8, column=1, padx=10, pady=10)


        # ==================================== FIRST ENTRY - NAME ====================================#
        self.patientboard_entbx1 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx1.grid(row=2, column=2, padx=10, pady=10)

        # ==================================== SCEOND ENTRY - AGE ====================================#
        self.patientboard_entbx2 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx2.grid(row=3, column=2, padx=10, pady=10)

        # ==================================== THIRD ENTRY - GENDER ====================================#
        self.patientboard_entbx3 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx3.grid(row=4, column=2, padx=10, pady=10)

        # ==================================== FOURTH ENTRY - WEIGHT ====================================#
        self.patientboard_entbx4 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx4.grid(row=5, column=2, padx=10, pady=10)

        # ==================================== FIFTH ENTRY - HEIGHT ====================================#
        self.patientboard_entbx5 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx5.grid(row=6, column=2, padx=10, pady=10)

        # ==================================== SIXTH ENTRY - ADDERESS ====================================#
        self.patientboard_entbx6 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx6.grid(row=7, column=2, padx=10, pady=10)

        # ==================================== SEVENTH ENTRY - CONTACT NUMBER ====================================#
        self.patientboard_entbx7 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx7.grid(row=8, column=2, padx=10, pady=10)


        # =================================== Patient SEARCH COMBOBOX VALUE ===================================#
        self.patient_search_obj = StringVar()
        self.patientboard_searchbox = ttk.Combobox(self.navigation_frame0,state='readonly',textvariable=self.patient_search_obj,width=27, height=5)
        self.patientboard_searchbox['values'] = ["Patient_Name","Patient_Age","Patient_Gender","Patient_Weight","Patient_Height","Patient_Address","Patient_Contact"]
        self.patientboard_searchbox.grid(row=4, column=0,pady=10,padx=10)

        # =================================== Patient SEARCH VALUE ===================================#
        self.patient_search_value = StringVar()
        self.patientboard_searchbx10 = Entry(self.navigation_frame0,textvariable=self.patient_search_value, bg="white", fg="black", font=("arial", 12, "bold"))
        self.patientboard_searchbx10.grid(row=5, column=0,pady=10,padx=10)

        # =================================== Patient TREE ===================================#
        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.patientboard_tree = ttk.Treeview(self.tree_frame, column=("Name", "Age", "Gender","Weight","Height","Address","Contact Number"),yscrollcommand=self.yscroll.set, height=11)
        self.yscroll.config(command=self.patientboard_tree.yview)
        self.patientboard_tree.pack()
        self.patientboard_tree['show'] = 'headings'

        self.patientboard_tree.column('Name', width=130,anchor="center")
        self.patientboard_tree.column('Age', width=100,anchor="center")
        self.patientboard_tree.column('Gender', width=100,anchor="center")
        self.patientboard_tree.column('Weight', width=100,anchor="center")
        self.patientboard_tree.column('Height', width=100,anchor="center")
        self.patientboard_tree.column('Address', width=130,anchor="center")
        self.patientboard_tree.column('Contact Number', width=133,anchor="center")

        self.patientboard_tree.heading('Name', text="Name")
        self.patientboard_tree.heading('Age', text="Age")
        self.patientboard_tree.heading('Gender', text="Gender")
        self.patientboard_tree.heading('Weight', text="Weight")
        self.patientboard_tree.heading('Height', text="Height")
        self.patientboard_tree.heading('Address', text="Address")
        self.patientboard_tree.heading('Contact Number', text="Contact Number")

        # =================================== ADD Button with picture inserted ===================================#
        self.patient_addbutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\addbutton.png")
        self.patient_addbutton = Button(self.navigation_frame, image=self.patient_addbutton_img, bg="white", fg="black", font=("arial", 15),command=self.addpatients, height=25, width=95)
        self.patient_addbutton.image = self.patient_addbutton_img
        self.patient_addbutton.grid(row=15, column=1, columnspan=2, padx=10, pady=15)

        # =================================== SHOW Button with picture inserted ===================================#
        self.patientboard_showbutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\showbutton.png")
        self.patientboard_showbutton = Button(self.navigation_frame, image=self.patientboard_showbutton_img, bg="white",fg="black", font=("arial", 15),command=self.showitemintree_patientdata, height=40, width=120)
        self.patientboard_showbutton.image = self.patientboard_showbutton_img
        self.patientboard_showbutton.grid(row=1, column=1,columnspan=3, padx=344, pady=15)

        # =================================== UPDATE Button with picture inserted ===================================#
        self.patientboard_updatebutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\updatebutton.png")
        self.patientboard_updatebutton = Button(self.navigation_frame, image=self.patientboard_updatebutton_img, bg="white",fg="black", font=("arial", 15),command=self.patient_updatefrntend, height=25, width=95)
        self.patientboard_updatebutton.image = self.patientboard_updatebutton_img
        self.patientboard_updatebutton.grid(row=15, column=2, padx=10, pady=15)

        # =================================== DELETE Button with picture inserted ===================================#
        self.patientboard_deletebutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\deletebutton.png")
        self.patientboard_deletebutton = Button(self.navigation_frame, image=self.patientboard_deletebutton_img,command=self.deletepatients, bg="white",fg="black", font=("arial", 15), height=25, width=95)
        self.patientboard_deletebutton.image = self.patientboard_deletebutton_img
        self.patientboard_deletebutton.grid(row=15, column=1, padx=10, pady=15)

        # =================================== SEARCH Button with picture inserted ===================================#
        self.patientboard_searchbutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\searchbutton.png")
        self.patientboard_searchbutton = Button(self.navigation_frame0, image=self.patientboard_searchbutton_img,bg="white",fg="black", font=("arial", 15),command=self.patientsearch, height=25, width=95)
        self.patientboard_searchbutton.image = self.patientboard_searchbutton_img
        self.patientboard_searchbutton.grid(row=6, column=0, pady=15,padx=20)

        # =================================== THIRD SEPERATOR ===================================#
        self.data1 = 22
        while self.data1 <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=415)
            self.data1 += 10

    # =================================== ADDING SERVICE ===================================#
    def addpatients(self):
        pat_name = self.patientboard_entbx1.get()
        pat_age = self.patientboard_entbx2.get()
        pat_gender = self.patientboard_entbx3.get()
        pat_weight = self.patientboard_entbx4.get()
        pat_height = self.patientboard_entbx5.get()
        pat_address=self.patientboard_entbx6.get()
        pat_contact=self.patientboard_entbx7.get()
        if len(pat_name) != 0 and len(pat_age) != 0 and len(pat_gender) != 0 and len(pat_weight) != 0 and len(pat_height) != 0 and len(pat_address) != 0 and len(pat_contact) != 0:
            if pat_age.isdigit():
                if pat_weight.isdigit():
                    if pat_contact.isdigit():
                        if self.staff_backend.patient_add(pat_name, pat_age, pat_gender, pat_weight,pat_height,pat_address,pat_contact):
                            messagebox.showinfo('Success', "Patients Added")
                            self.showitemintree_patientdata()
                            self.update_index1 = ""
                        else:
                            messagebox.showerror("Error", "Can't add your patient.")
                    else:
                        messagebox.showerror("Numeric data needed.", "Contract number must be numeric.")
                else:
                    messagebox.showerror("Numeric data needed.", "Weight must be numeric.")
            else:
                messagebox.showerror("Numeric data needed.", "Age must be numeric.")
        else:
            messagebox.showerror("Error", "Can't leave any blank spaces.")

    # =================================== SHOWING CONTENT IN Patient TREE ===================================#
    def showitemintree_patientdata(self):
        self.patientboard_tree.delete(*self.patientboard_tree.get_children())
        reqdata=self.staff_backend.patient_backend_showdata()
        for i in reqdata:
            self.patientboard_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3],i[4], i[5],i[6],i[7]))
        self.patientboard_tree.bind("<Double-1>", self.patient_onitemselect)

    # =================================== SELECTING CONTENT IN TREE ===================================#
    def patient_onitemselect(self, event):
        selected_row0 = self.patientboard_tree.selection()[0]
        selected_item0 = self.patientboard_tree.item(selected_row0, 'values')
        self.update_index0 = self.patientboard_tree.item(selected_row0, 'text')

        self.patientboard_entbx1.delete(0,END)
        self.patientboard_entbx1.insert(0,selected_item0[0])
        self.patientboard_entbx2.delete(0, END)
        self.patientboard_entbx2.insert(0, selected_item0[1])
        self.patientboard_entbx3.delete(0, END)
        self.patientboard_entbx3.insert(0, selected_item0[2])
        self.patientboard_entbx4.delete(0, END)
        self.patientboard_entbx4.insert(0, selected_item0[3])
        self.patientboard_entbx5.delete(0, END)
        self.patientboard_entbx5.insert(0, selected_item0[4])
        self.patientboard_entbx6.delete(0, END)
        self.patientboard_entbx6.insert(0, selected_item0[5])
        self.patientboard_entbx7.delete(0, END)
        self.patientboard_entbx7.insert(0, selected_item0[6])

    # =================================== UPDATING CONTENT IN TREE ===================================#
    def patient_updatefrntend(self):
        if self.update_index0 == "":
            messagebox.showerror("Error", "Please select a row first")
        else:
            pat_name = self.patientboard_entbx1.get()
            pat_age = self.patientboard_entbx2.get()
            pat_gender = self.patientboard_entbx3.get()
            pat_weight = self.patientboard_entbx4.get()
            pat_height = self.patientboard_entbx5.get()
            pat_address = self.patientboard_entbx6.get()
            pat_contact = self.patientboard_entbx7.get()
            if len(pat_name) != 0 and len(pat_age) != 0 and len(pat_gender) != 0 and len(pat_weight) != 0 and len(pat_height) != 0 and len(pat_address) != 0 and len(pat_contact) != 0:
                if pat_age.isdigit():
                    if pat_weight.isdigit():
                        if pat_contact.isdigit():
                            if self.staff_backend.patient_status_update(self.update_index0,pat_name, pat_age, pat_gender, pat_weight, pat_height, pat_address,pat_contact):
                                messagebox.showinfo('Success', "Patients Updated")
                                self.showitemintree_patientdata()
                                self.update_index1 = ""
                            else:
                                messagebox.showerror("Error", "Can't add your patient.")
                        else:
                            messagebox.showerror("Numeric data needed.", "Contract number must be numeric.")
                    else:
                        messagebox.showerror("Numeric data needed.", "Weight must be numeric.")
                else:
                    messagebox.showerror("Numeric data needed.", "Age must be numeric.")
            else:
                messagebox.showerror("Error", "Can't leave any blank spaces.")

    # =================================== SEARCHING CONTENT IN DATABASE ===================================#
    def patientsearch(self):
        if len(self.patient_search_value.get()) != 0 and len(self.patient_search_obj.get()) != 0:
            searcheed_data0 = self.staff_backend.return_patient_search_data(self.patient_search_value.get(),self.patient_search_obj.get())
            if len(searcheed_data0) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
                self.patientboard_tree.delete(*self.patientboard_tree.get_children())
            else:
                self.patientboard_tree.delete(*self.patientboard_tree.get_children())
                for i in searcheed_data0:
                    self.patientboard_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                self.patientboard_tree.bind("<Double-1>", self.patient_onitemselect)
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")

    # ================================== Delete Service =======================================================#
    def deletepatients(self):
        if self.update_index0 == "":
            messagebox.showerror("Can't delete", "Please select a row first.")
        else:
            if self.staff_backend.delete_patients(self.update_index0):
                messagebox.showinfo("Service Deleted", "The service is now deleted.")
                self.showitemintree_patientdata()
            else:
                messagebox.showerror("Can't delete", "Delete Failed")

    # ======================================== APPOINTMENT =========================================#
    def appointments(self):
        self.deleteframe()
        self.display_date()
        self.display_time()
        self.endphoto()
        # =================================== FIRST SEPERATOR ===================================#
        self.data0 = 22
        while self.data0 <= 790:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=9)
            self.data0 += 10
        # =================================== SECOND SEPERATOR ===================================#
        self.data = 22
        while self.data <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=70)
            self.data += 10

        # ==================================== Appointment Logo  ====================================#
        self.appointment_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\schedulelogo.png")
        self.appointment_photo_lable = Label(self.navigation_frame0, image=self.appointment_photo, bg="white")
        self.appointment_photo_lable.image = self.appointment_photo
        self.appointment_photo_lable.grid(row=3, column=0, padx=5)

        self.appointment_photo1 = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\schedule.png")
        self.appointment_photo1_lable = Label(self.navigation_frame, image=self.appointment_photo1, bg="white")
        self.appointment_photo1_lable.image = self.appointment_photo1

        # ==================================== HeEADING LABEL - Appointment ====================================#
        self.appointmentboard_lbhead = Label(self.navigation_frame, text="Appointment", image=self.appointment_photo1,compound=TOP, bg="white", font=('Arial', 18, 'bold', 'underline'), fg='Black')
        self.appointmentboard_lbhead.grid(row=2, column=1, columnspan=3, padx=10, pady=12)

        # ==================================== FIRST LABEL - NAME ====================================#
        self.appointmentboard_lb1 = Label(self.navigation_frame, text="Name of the Patint", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.appointmentboard_lb1.grid(row=3, column=1, padx=10, pady=14)

        # ==================================== SCEOND LABEL - TIME ====================================#
        self.appointmentboard_lb2 = Label(self.navigation_frame, text="Appointed By", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.appointmentboard_lb2.grid(row=4, column=1, padx=10, pady=14)

        # ==================================== THIRD LABEL - DOC StatS ====================================#
        self.appointmentboard_lb3 = Label(self.navigation_frame, text="Appointment Status", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.appointmentboard_lb3.grid(row=5, column=1, padx=10, pady=14)

        # ==================================== FIRST ENTRY - NAME ====================================#
        self.appointmentboard_entbx1_obj = StringVar()
        self.appointmentboard_entbx1 = ttk.Combobox(self.navigation_frame, state='readonly',textvariable=self.appointmentboard_entbx1_obj, width=33, height=5)
        self.appointmentboard_entbx1['values'] = self.staff_backend.return_all_patientname()
        self.appointmentboard_entbx1.grid(row=3, column=2, padx=10, pady=10)

        # ==================================== SCEOND ENTRY - AGE ====================================#
        self.appointmentboard_entbx2_obj = StringVar()
        self.appointmentboard_entbx2 = ttk.Combobox(self.navigation_frame, state='readonly',textvariable=self.appointmentboard_entbx2_obj, width=33, height=5)
        self.appointmentboard_entbx2['values'] =(self.lastuserloggedin)
        self.appointmentboard_entbx2.grid(row=4, column=2, padx=10, pady=10)

        # ==================================== THIRD ENTRY - GENDER ====================================#
        self.appointmentboard_entbx3_obj = StringVar()
        self.appointmentboard_entbx3 = ttk.Combobox(self.navigation_frame, state='readonly',textvariable=self.appointmentboard_entbx3_obj, width=33, height=5)
        self.appointmentboard_entbx3['values'] = ["Pending", "Approved"]
        self.appointmentboard_entbx3.grid(row=5, column=2, padx=10, pady=10)

        # =================================== Appointment SEARCH COMBOBOX VALUE ===================================#
        self.appointment_search_obj = StringVar()
        self.appointmentboard_searchbox = ttk.Combobox(self.navigation_frame0, state='readonly',textvariable=self.appointment_search_obj, width=27, height=5)
        self.appointmentboard_searchbox['values'] = ["Doctor_Name", "Time", "Doctor_Availability","Patient_Name", "Appointment_by", "Booking_status"]
        self.appointmentboard_searchbox.grid(row=4, column=0, pady=10)

        # =================================== Appointment SEARCH VALUE ===================================#
        self.appointment_search_value = StringVar()
        self.appointmentboard_searchbx10 = Entry(self.navigation_frame0, textvariable=self.appointment_search_value,bg="white", fg="black", font=("arial", 12, "bold"))
        self.appointmentboard_searchbx10.grid(row=5, column=0, pady=10)

        # =================================== Appointment TREE ===================================#
        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.appointmentboard_tree = ttk.Treeview(self.tree_frame, column=("Name", "Time", "Availability","Patient_Name","Appointed_by","Booking_status"),yscrollcommand=self.yscroll.set, height=11)
        self.yscroll.config(command=self.appointmentboard_tree.yview)
        self.appointmentboard_tree.pack()
        self.appointmentboard_tree['show'] = 'headings'

        self.appointmentboard_tree.column('Name', width=125, anchor="center")
        self.appointmentboard_tree.column('Time', width=125, anchor="center")
        self.appointmentboard_tree.column('Availability', width=125, anchor="center")
        self.appointmentboard_tree.column('Patient_Name', width=140, anchor="center")
        self.appointmentboard_tree.column('Appointed_by', width=140, anchor="center")
        self.appointmentboard_tree.column('Booking_status', width=140, anchor="center")

        self.appointmentboard_tree.heading('Name', text="Doctor Name")
        self.appointmentboard_tree.heading('Time', text="Time")
        self.appointmentboard_tree.heading('Availability', text="Availability")
        self.appointmentboard_tree.heading('Patient_Name', text="Patient_Name")
        self.appointmentboard_tree.heading('Appointed_by', text="Appointed_by")
        self.appointmentboard_tree.heading('Booking_status', text="Appointment_status")

        # =================================== SHOW Button with picture inserted ===================================#
        self.appointmentboard_showbutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\showbutton.png")
        self.appointmentboard_showbutton = Button(self.navigation_frame, image=self.appointmentboard_showbutton_img,command=self.showitemintree_appointmentdata,bg="white", fg="black",font=("arial", 15), height=40, width=120)
        self.appointmentboard_showbutton.image = self.appointmentboard_showbutton_img
        self.appointmentboard_showbutton.grid(row=0, column=1, columnspan=3, padx=344, pady=15)

        # =================================== UPDATE Button with picture inserted ===================================#
        self.appointmentboard_updatebutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\updatebutton.png")
        self.appointmentboard_updatebutton = Button(self.navigation_frame, image=self.appointmentboard_updatebutton_img,command=self.appointment_updatefrntend, bg="white", fg="black",font=("arial", 15), height=25, width=95)
        self.appointmentboard_updatebutton.image = self.appointmentboard_updatebutton_img
        self.appointmentboard_updatebutton.grid(row=15, column=2, padx=10, pady=22)

        # =================================== DELETE Button with picture inserted ===================================#
        self.appointmentboard_deletebutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\deletebutton.png")
        self.appointmentboard_deletebutton = Button(self.navigation_frame, image=self.appointmentboard_deletebutton_img,command=self.deleteappointment,bg="white", fg="black", font=("arial", 15), height=25, width=95)
        self.appointmentboard_deletebutton.image = self.appointmentboard_deletebutton_img
        self.appointmentboard_deletebutton.grid(row=15, column=1, padx=10, pady=22)

        # =================================== SEARCH Button with picture inserted ===================================#
        self.appointmentboard_searchbutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\searchbutton.png")
        self.appointmentboard_searchbutton = Button(self.navigation_frame0, image=self.appointmentboard_searchbutton_img,command=self.appointmentsearch,bg="white", fg="black",font=("arial", 15), height=25, width=95)
        self.appointmentboard_searchbutton.image = self.appointmentboard_searchbutton_img
        self.appointmentboard_searchbutton.grid(row=6, column=0, pady=10)

        # =================================== THIRD SEPERATOR ===================================#
        self.data1 = 22
        while self.data1 <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=400)
            self.data1 += 10

    # =================================== SHOWING CONTENT IN SERVICE TREE ===================================#
    def showitemintree_appointmentdata(self):
        self.appointmentboard_tree.delete(*self.appointmentboard_tree.get_children())
        reqdata = self.staff_backend.appointment_backend_showdata()
        for i in reqdata:
            self.appointmentboard_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5],i[6]))
        self.appointmentboard_tree.bind("<Double-1>", self.appointment_onitemselect)

    # =================================== SELECTING CONTENT IN TREE ===================================#
    def appointment_onitemselect(self, event):
        selected_row0 = self.appointmentboard_tree.selection()[0]
        selected_item0 = self.appointmentboard_tree.item(selected_row0, 'values')
        self.update_index0 = self.appointmentboard_tree.item(selected_row0, 'text')

        self.appointmentboard_entbx1.delete(0, END)
        self.appointmentboard_entbx1.insert(0, selected_item0[0])
        self.appointmentboard_entbx2.delete(0, END)
        self.appointmentboard_entbx2.insert(0, selected_item0[1])
        self.appointmentboard_entbx3.delete(0, END)
        self.appointmentboard_entbx3.insert(0, selected_item0[2])

    # =================================== UPDATING CONTENT IN TREE ===================================#
    def appointment_updatefrntend(self):
        if self.update_index0 == "":
            messagebox.showerror("Error", "Please select a row first")
        else:
            appointment_pname = self.appointmentboard_entbx1_obj.get()
            appointment_by = self.appointmentboard_entbx2_obj.get()
            appointment_docsapptatus = self.appointmentboard_entbx3_obj.get()
            if len(appointment_pname) != 0 and len(appointment_by) != 0 and len(appointment_docsapptatus) != 0:
                if self.staff_backend.appointment_status_update(self.update_index0, appointment_pname, appointment_by,appointment_docsapptatus):
                    messagebox.showinfo('Item', "Item Updated")
                    self.showitemintree_appointmentdata()
                    self.update_index0 = ""
                else:
                    messagebox.showerror("Error", 'Can not be updated !!!')
            else:
                messagebox.showerror("Error", "Can't leave any blank spaces.")

    # ========================================= Deleting Appointment Data ====================================#
    def deleteappointment(self):
        if self.update_index0 == "":
            messagebox.showerror("Can't delete", "Please select a row first.")
        else:
            if self.staff_backend.delete_appointments(self.update_index0):
                messagebox.showinfo("Appointment Cleared", "The appointment is now cleared.")
                self.showitemintree_appointmentdata()
            else:
                messagebox.showerror("Can't delete", "Delete Failed")

    # =================================== SEARCHING CONTENT IN DATABASE ===================================#
    def appointmentsearch(self):
        if len(self.appointment_search_value.get()) != 0 and len(self.appointment_search_obj.get()) != 0:
            searcheed_data0 = self.staff_backend.return_appointment_search_data(self.appointment_search_value.get(),self.appointment_search_obj.get())
            if len(searcheed_data0) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
                self.appointmentboard_tree.delete(*self.appointmentboard_tree.get_children())
            else:
                self.appointmentboard_tree.delete(*self.appointmentboard_tree.get_children())
                for i in searcheed_data0:
                    self.appointmentboard_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5],i[6]))
                self.appointmentboard_tree.bind("<Double-1>", self.appointment_onitemselect)
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")
    #=================================== Changing Credentials ==========================================#
    def change_staff_credentials(self):
        self.deleteframe()

        # ==================================== Chng Credential Logo  ====================================#
        self.change_credential_pic = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\change_credentials.png")
        self.change_credential_pic_lable = Label(self.tree_frame, image=self.change_credential_pic, bg="white")
        self.change_credential_pic_lable.image = self.change_credential_pic

        # ==================================== First Seperator ====================================#
        self.data0 = 22
        while self.data0 <= 800:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=0)
            self.data0 += 10
        # ==================================== Second Seperator ====================================#
        self.data = 22
        while self.data <= 800:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=230)
            self.data += 10
        # ==================================== Third Seprator ====================================#
        self.data1 = 22
        while self.data1 <= 800:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=300)
            self.data1 += 10

        # ==================================== First label - Major heading  ====================================#
        self.changeboard_lbhead = Label(self.tree_frame, text="Change Credentials", image=self.change_credential_pic,compound=TOP, bg="white", font=('Arial', 18, 'bold', 'underline'),fg='Black')
        self.changeboard_lbhead.grid(row=2, column=1, columnspan=2, padx=115, pady=13)

        # ==================================== FIRST LABEL - NAME ====================================#
        self.changeboard_lb1 = Label(self.navigation_frame, text="Username", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.changeboard_lb1.grid(row=3, column=1, padx=10, pady=15)

        # ==================================== Second LABEL - OLd Password ====================================#
        self.changeboard_lb2 = Label(self.navigation_frame, text="Old Password", bg="white", font=('Arial', 12, 'bold'),fg='Black')
        self.changeboard_lb2.grid(row=4, column=1, padx=10, pady=14)

        # ==================================== Third LABEL - New password ====================================#
        self.changeboard_lb3 = Label(self.navigation_frame, text="New Password", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.changeboard_lb3.grid(row=5, column=1, padx=10, pady=14)

        # ====================================== First Entry - Name ======================================#
        self.changeboard_entbx1 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.changeboard_entbx1.grid(row=3, column=2, padx=12, pady=15)

        # ====================================== Second Entry - old PAssowrd ======================================#
        self.changeboard_entbx2 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.changeboard_entbx2.grid(row=4, column=2, padx=12, pady=15)

        # ====================================== Third Entry - New password ======================================#
        self.changeboard_entbx3 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.changeboard_entbx3.grid(row=5, column=2, padx=14, pady=15)

        # ====================================== Fourth Entry - resenter password ======================================#
        self.changeboard_entbx4 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.changeboard_entbx4.grid(row=6, column=2, padx=13, pady=15)

        # ==================================== Fourth LABEL - Reenter pasword ====================================#
        self.changeboard_lb4 = Label(self.navigation_frame, text="Re-enter New Password", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.changeboard_lb4.grid(row=6, column=1, padx=10, pady=14)

        #====================================== Required Buttons ========================================#
        self.changeboard_btn1_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\updatebutton.png")
        self.changeboard_btn1 = Button(self.navigation_frame, image=self.changeboard_btn1_img,command=self.updating_credentials,bg="white", fg="black",font=("arial", 15), height=25, width=95)
        self.changeboard_btn1.image = self.changeboard_btn1_img
        self.changeboard_btn1.grid(row=7, column=1,columnspan=2,padx=10, pady=22)

        # ==================================== Fifth LABEL -Instruction to follow ====================================#
        self.changeboard_lb5 = Label(self.navigation_frame, text="Please follow the following Instruction.", bg="white",font=('Arial', 12, 'bold',"underline"), fg='Black')
        self.changeboard_lb5.grid(row=8, column=1,columnspan=2, padx=10, pady=14)

        self.changeboard_lb6 = Label(self.navigation_frame, text="Ensure your password are 8 character long.\n\n"
                                                                 "Please don't use your birthdates, phone numbers for passwords.\n\n"
                                                                 "Passwords mustn't be shared with anyone.", bg="white",font=('Arial', 10, 'bold'), fg='Black')
        self.changeboard_lb6.grid(row=9, column=1,columnspan=2, pady=14)


    def updating_credentials(self):
        username=self.changeboard_entbx1.get()
        oldpassword=self.changeboard_entbx2.get()
        newpassword=self.changeboard_entbx3.get()
        retype_newpassword=self.changeboard_entbx4.get()
        if len(username)!=0 and len(oldpassword)!=0 and len(newpassword)!=0 and len(retype_newpassword)!=0:
            if username==self.lastuserloggedin.lower():
                if self.staff_backend.return_staff_search_data(username)[0][0]==oldpassword:
                    if len(newpassword)>=8:
                        if newpassword==retype_newpassword:
                            self.staff_backend.update_staff_login_data(retype_newpassword,username)
                            messagebox.showinfo("Success","Credentials changed.")
                        else:
                            messagebox.showerror("Password didn't matched", "The password you provided in \n  both column are not identical.")
                    else:
                        messagebox.showerror("Password too Short.", "The password must be 8 character long.")
                else:
                    messagebox.showerror("Wrong Password", "The password you provided didn't matched.")
            else:
                messagebox.showerror("Unauthenticated user", "You can't change other people credentials.")
        else:
            messagebox.showerror("Empty Input", "You can't leave any boxes empty.")

    # =================================== Billings =======================================================#
    def bill_of_patients(self):
        self.deleteframe()
        self.display_date()
        self.display_time()
        self.endphoto()
        # ==================================== First Seperator ====================================#
        self.data0 = 22
        while self.data0 <= 790:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=4)
            self.data0 += 10

        # ==================================== SCEOND Seperator ====================================#
        self.data = 22
        while self.data <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=55)
            self.data += 10

        # ==================================== THIRD Seperator ====================================#
        self.data1 = 22
        while self.data1 <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=300)
            self.data1 += 10

        # ==================================== FOURTH Seperator ====================================#
        self.data4 = 22
        while self.data4 <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data4, y=355)
            self.data4 += 10

        # ============================= Priscription Tree =======================#
        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.patient_billing_tree = ttk.Treeview(self.tree_frame, column=("Patient_name", "Service_name", "Servive_type", "Service_price", "Medicine_name", "Medicine_type","Medicine_price", "Quantity"), yscrollcommand=self.yscroll.set, height=11)
        self.yscroll.config(command=self.patient_billing_tree.yview)
        self.patient_billing_tree.pack()

        self.patient_billing_tree['show'] = 'headings'
        self.patient_billing_tree.column('Patient_name', width=100, anchor='center')
        self.patient_billing_tree.column('Service_name', width=100, anchor='center')
        self.patient_billing_tree.column('Servive_type', width=100, anchor='center')
        self.patient_billing_tree.column('Service_price', width=100, anchor='center')
        self.patient_billing_tree.column('Medicine_name', width=100, anchor='center')
        self.patient_billing_tree.column('Medicine_type', width=100, anchor='center')
        self.patient_billing_tree.column('Medicine_price', width=100, anchor='center')
        self.patient_billing_tree.column('Quantity', width=95, anchor='center')

        self.patient_billing_tree.heading('Patient_name', text='Patient_name')
        self.patient_billing_tree.heading('Service_name', text='Service_name')
        self.patient_billing_tree.heading('Servive_type', text='Servive_type')
        self.patient_billing_tree.heading('Service_price', text='Service_price')
        self.patient_billing_tree.heading('Medicine_name', text='Medicine_name')
        self.patient_billing_tree.heading('Medicine_type', text='Medicine_type')
        self.patient_billing_tree.heading('Medicine_price', text='Medicine_price')
        self.patient_billing_tree.heading('Quantity', text='Med_quantity')

        # ==================================== Change Credential Logo  ====================================#
        self.patient_billing_pic = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\bill.png")
        self.patient_billing_pic_lable = Label(self.navigation_frame0, image=self.patient_billing_pic, bg="white")
        self.patient_billing_pic_lable.image = self.patient_billing_pic
        self.patient_billing_pic_lable.grid(row=3, column=0, padx=20)

        # ==================================== First Lable ================================================#
        self.patient_billing_lb1 = Label(self.navigation_frame0, text="BILLING ", bg="white",font=('Arial', 15, 'bold', 'underline'), fg='Black')
        self.patient_billing_lb1.grid(row=4, column=0, padx=15, pady=20)

        # ==================================== Prescribed Patient List ===================================#
        self.patient_billing_entbx1 = ttk.Combobox(self.navigation_frame0, state='readonly', width=33, height=5)
        self.patient_billing_entbx1['values'] = self.doctor_backend.return_all_prescribed_patient()
        self.patient_billing_entbx1.grid(row=5, column=0, padx=20, pady=20)

        # =================================== SEARCH Button with picture inserted ===================================#
        self.scheduleboard_searchbutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\searchbutton.png")
        self.scheduleboard_searchbutton = Button(self.navigation_frame0, image=self.scheduleboard_searchbutton_img,command=self.search_history_prescription_bill, bg="white", fg="black",font=("arial", 15), height=25, width=95)
        self.scheduleboard_searchbutton.image = self.scheduleboard_searchbutton_img
        self.scheduleboard_searchbutton.grid(row=6, column=0, pady=10)

        #=================================== Extra Lables ========================================================#
        self.patient_billing_lb11 = Label(self.navigation_frame, text="Softwarica Clinic Bill", bg="white",font=('Arial', 20, 'bold',"underline"), fg='Blue')
        self.patient_billing_lb11.grid(row=8, column=1,columnspan=5, padx=310, pady=8)

        # =================================== BILL NUMBER ========================================================#
        self.patient_billing_lb12 = Label(self.navigation_frame, text="Bill no:", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.patient_billing_lb12.grid(row=9, column=1,columnspan=2, padx=5, pady=8)

        # =================================== PATIENT NAME ========================================================#
        self.patient_billing_lb13 = Label(self.navigation_frame, text="Patient Name:", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.patient_billing_lb13.grid(row=10, column=1,columnspan=2, padx=5, pady=8)

        # =================================== DATEs ========================================================#
        self.patient_billing_lb114 = Label(self.navigation_frame, text="Date:", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.patient_billing_lb114.grid(row=11, column=1,columnspan=2, padx=5, pady=8)

        # =================================== BILLED BY ========================================================#
        self.patient_billing_lb115 = Label(self.navigation_frame, text="Billed by:", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.patient_billing_lb115.grid(row=12, column=1,columnspan=2, padx=5, pady=8)

        # =================================== SERVICE CHARGES ========================================================#
        self.patient_billing_lb14 = Label(self.navigation_frame, text="Service Charges:", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.patient_billing_lb14.grid(row=13, column=1, columnspan=2, padx=5, pady=8)

        # =================================== MEDICINES CHARGES ========================================================#
        self.patient_billing_lb15 = Label(self.navigation_frame, text="Medicine Charges:", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.patient_billing_lb15.grid(row=14, column=1, columnspan=2, padx=5, pady=8)

        # =================================== TOTAL AMOUNT ========================================================#
        self.patient_billing_lb155 = Label(self.navigation_frame, text="Total Amount:", bg="white",font=('Arial', 15, 'bold'), fg='Black')
        self.patient_billing_lb155.grid(row=15, column=1,columnspan=3, padx=5, pady=15)

        # ------------------------------------ Values -----------------------------------------------------------#
        # =================================== BILL NUMBER ========================================================#
        self.patient_billing_lb12val = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
        self.patient_billing_lb12val.grid(row=9, column=3, columnspan=2, padx=5, pady=8)

        # =================================== PATIENT NAME ========================================================#
        self.patient_billing_lb13val = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
        self.patient_billing_lb13val.grid(row=10, column=3, columnspan=2, padx=5, pady=8)

        # =================================== DATEs ========================================================#
        self.patient_billing_lb114val = Label(self.navigation_frame, bg="white", font=('Arial', 12, 'bold'),fg='red')
        self.patient_billing_lb114val.grid(row=11, column=3, columnspan=2, padx=5, pady=8)

        # =================================== BILLED BY ========================================================#
        self.patient_billing_lb115val = Label(self.navigation_frame, bg="white", font=('Arial', 12, 'bold'), fg='red')
        self.patient_billing_lb115val.grid(row=12, column=3, columnspan=2, padx=5, pady=8)

        # =================================== SERVICE CHARGES ========================================================#
        self.patient_billing_lb14val = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
        self.patient_billing_lb14val.grid(row=13, column=3, columnspan=2, padx=5, pady=8)

        # =================================== MEDICINES CHARGES ========================================================#
        self.patient_billing_lb15val = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
        self.patient_billing_lb15val.grid(row=14, column=3, columnspan=2, padx=5, pady=8)

        # =================================== TOTAL AMOUNT ========================================================#
        self.patient_billing_lb15v = Label(self.navigation_frame, bg="white",font=('Arial', 15, 'bold'), fg='red')
        self.patient_billing_lb15v.grid(row=15, column=2, columnspan=3, padx=5, pady=15)

        # =================================== REMINDER Lables ========================================================#
        self.patient_billing_lb105 = Label(self.navigation_frame, text="Please Ensure the Following:", bg="white",font=('Arial',14 , 'bold','underline'), fg='Black')
        self.patient_billing_lb105.grid(row=16, column=1, columnspan=5, padx=5, pady=5)

        self.patient_billing_lb105 = Label(self.navigation_frame, text="1.) Once sold medicines wont be returned. \n ""2.) Clinic shalln't refund money invested \n for any of the services.", bg="white",font=('Arial', 12), fg='Black')
        self.patient_billing_lb105.grid(row=17, column=1, columnspan=5, padx=5, pady=5)

    # ======================================== Generate Bill ===========================================#
    def generate_bill(self):
        orders = self.patient_billing_tree.get_children()
        total=0
        servicetotal = 0
        medicinetotal =0
        for i in orders:
            order=self.patient_billing_tree.item(i,'values')
            if order[3] == "--/--":
                serviceamt = 0
            else:
                serviceamt = float(order[3])
            medicineamt=float(order[6])*float(order[7])
            servicetotal += serviceamt
            medicinetotal += medicineamt
            total= servicetotal + medicinetotal

        # ------------------------------------ Values -----------------------------------------------------------#
        # =================================== BILL NUMBER ========================================================#
        billid_data=self.staff_backend.return_patient_search_data(self.patient_billing_entbx1.get(),"Patient_Name")
        billid=billid_data[0][0]
        self.patient_billing_lb12val.destroy()
        self.patient_billing_lb12val = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
        self.patient_billing_lb12val.configure(text=billid)
        self.patient_billing_lb12val.grid(row=9, column=3, columnspan=2, padx=5, pady=8)

        # =================================== PATIENT NAME ========================================================#
        self.patient_billing_lb13val.destroy()
        self.patient_billing_lb13val = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
        self.patient_billing_lb13val.configure(text=self.patient_billing_entbx1.get())
        self.patient_billing_lb13val.grid(row=10, column=3, columnspan=2, padx=5, pady=8)

        # =================================== DATEs ========================================================#
        self.patient_billing_lb114val.destroy()
        self.patient_billing_lb114val = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
        myfate = datetime.datetime.now()
        reqdate = myfate.strftime('%D')
        self.patient_billing_lb114val.configure(text=reqdate)
        self.patient_billing_lb114val.grid(row=11, column=3, columnspan=2, padx=5, pady=8)

        # =================================== BILLED BY ========================================================#
        self.patient_billing_lb115val.destroy()
        self.patient_billing_lb115val = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
        username=self.lastuserloggedin
        self.patient_billing_lb115val.configure(text=username)
        self.patient_billing_lb115val.grid(row=12, column=3, columnspan=2, padx=5, pady=8)

        # =================================== SERVICE CHARGES ========================================================#
        self.patient_billing_lb14val.destroy()
        self.patient_billing_lb14val = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
        self.patient_billing_lb14val.configure(text=servicetotal)
        self.patient_billing_lb14val.grid(row=13, column=3, columnspan=2, padx=5, pady=8)

        # =================================== MEDICINES CHARGES ========================================================#
        self.patient_billing_lb15val.destroy()
        self.patient_billing_lb15val = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
        self.patient_billing_lb15val.configure(text=medicinetotal)
        self.patient_billing_lb15val.grid(row=14, column=3, columnspan=2, padx=5, pady=8)

        # =================================== TOTAL AMOUNT ========================================================#
        self.patient_billing_lb15v.destroy()
        self.patient_billing_lb15v = Label(self.navigation_frame, bg="white",font=('Arial', 15, 'bold'), fg='red')
        self.patient_billing_lb15v.configure(text=total)
        self.patient_billing_lb15v.grid(row=15, column=2, columnspan=3, padx=5, pady=15)


    # ================================ Search data ============================================#
    def search_history_prescription_bill(self):
        if len(self.patient_billing_entbx1.get()) != 0:
            self.patient_billing_tree.delete(*self.patient_billing_tree.get_children())
            data = self.doctor_backend.return_specified_prescribed_data_history(self.patient_billing_entbx1.get())
            if len(data) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
            else:
                for i in data:
                    self.patient_billing_tree.insert('', 'end', text='',value=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                self.generate_bill()
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")

    # =================================== DATE AND TIME SELECTED FRAME ===================================#
    def display_time(self):
        current_time = tm.strftime('%I:%M:%S %p ')
        self.wn.after(200, self.display_time)
        clock_label = Label(self.navigation_frame0, text=current_time, font=("Ticking Timebomb BB Regular", 27),bg='white', fg='#000000')
        clock_label.grid(row=0, column=0, padx=14)

    def display_date(self):
        x = datetime.datetime.now()
        self.current_date = x.strftime('%A,%B %d')
        self.req_currentdate=x.strftime('%B %d')
        date_label = Label(self.navigation_frame0, text=self.current_date, font="Ariel 15", bg='white', fg='#2b2b2b')
        date_label.grid(row=1, column=0,padx=15)

    # =================================== DELETE LAST SELECTED FRAME ===================================#
    def deleteframe(self):
        for widget in self.navigation_frame.winfo_children():
            widget.destroy()

        for widget in self.navigation_frame0.winfo_children():
            widget.destroy()

        for widget in self.tree_frame.winfo_children():
            widget.destroy()

    # =================================== Logging out ===================================#
    def logout(self):
        self.wn.destroy()
        from interface.first_window import Firstwindow
        Firstwindow()

    # ================================ END PHOTO =======================================#
    def endphoto(self):
        self.photo00 = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\logo.png")
        self.photo_lable00 = Label(self.navigation_frame0, image=self.photo00, bg="white")
        self.photo_lable00.image = self.photo00
        self.photo_lable00.grid(row=8, column=0, padx=5, pady=43)

# Staff_interface("test")