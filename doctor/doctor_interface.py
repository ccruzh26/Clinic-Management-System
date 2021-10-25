#=========================== Importing all the necessary modules ============================#
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time as tm
import datetime
from doctor.doctor_interface_backend import Doctorbackend
from admin.admin_interface_backend import Adminbackend
from staff.staff_interface_backend import Staffbackend


class Doctor_interface:
    # =============================== Creating Tkinter Window ================================#
    def __init__(self,doctorloggedin,doctorloggedinname):
        self.wn = Tk()
        self.wn.title("Doctor Panel")
        self.wn.geometry("1370x735+0+0")
        self.wn.configure(bg="white")
        self.wn.resizable(False, False)
        self.doctor_backend = Doctorbackend()
        self.admin_backend= Adminbackend()
        self.staff_backend=Staffbackend()
        self.lastuserloggedin = doctorloggedin
        self.lastuserloggedinname =doctorloggedinname

        self.all_services=self.admin_backend.service_backend_showdata()
        self.all_medicines=self.admin_backend.medicine_backend_showdata()
        self.update_index0=""
        # =========================== Importing all necessary photo =============================#
        self.title_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\doctorpanel.png")
        self.title_photo_lable = Label(self.wn, image=self.title_photo, bg="white",bd=1,borderwidth=2)
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=1, y=0)

        self.title_photo01 = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\doctorboardbckground.png")
        self.title_photo01_lable = Label(self.wn, image=self.title_photo01,bg="white")
        self.title_photo01_lable.image = self.title_photo01
        self.title_photo01_lable.place(x=280, y=0)

        # ===========================  Necessary Frames =============================#
        self.frame1 = LabelFrame(self.wn, bg="white")
        self.frame1.place(x=0, y=270)
        self.entry_frame= Frame(self.wn, bg="white")
        self.entry_frame.place(x=300,y=20)
        self.tree_frame = LabelFrame(self.wn, bg="white",bd=2)
        self.tree_frame.place(x=285, y=0)
        self.navigation_frame = LabelFrame(self.wn, bg="white")
        self.navigation_frame.place(x=285, y=247)
        self.navigation_frame0 = LabelFrame(self.wn, bg="white", bd=2)
        self.navigation_frame0.place(x=1100, y=0)

        # ==================================== Major Heading ====================================#
        self.lb_heading_inital = Label(self.frame1, text="Doctor", bg="white", font=('Impact', 34, 'bold', 'underline'),fg='red')
        self.lb_heading_inital.grid(row=20, column=40, padx=8, pady=12)
        self.lb_heading_end = Label(self.frame1, text="Panel", bg="white", font=('Impact', 34, 'bold', 'underline'),fg='blue')
        self.lb_heading_end.grid(row=20, column=80, padx=7, pady=12)

        # =================================== Creating Frame-2 ===================================#
        self.frame2 = LabelFrame(self.wn, bg="white",borderwidth=2)
        self.frame2.place(x=0, y=350)

        # ============================ Creating Seprator and Buttons ============================#

        # ==================================== First Button ====================================#
        self.appointment_button = Button(self.frame2, text="Appointments", bg='green', fg="white",
                                         activebackground="#73C2FB",activeforeground="indigo", cursor="hand2",
                                         command=self.appointments, font=("Comic Sans MS", 15, "bold"),height=1,
                                         width=15, relief=RIDGE, overrelief=RAISED)
        self.appointment_button.grid(row=5, column=0, padx=10, pady=20)

        # =================================+ Second Seprator ===================================#
        self.second_seperator = Canvas(self.frame2, width=270, height=1, bd=0, highlightthickness=0)
        self.second_seperator.configure(bg="black")
        self.second_seperator.grid(row=10, column=0)

        # ==================================== Second Button ====================================#
        self.prescription_button = Button(self.frame2, text="Prescriptions", bg='yellow', fg="black",
                                          activebackground="#73C2FB", activeforeground="indigo", cursor="hand2",
                                          command=self.prescriptions,font=("Comic Sans MS", 15, "bold"), height=1,
                                          width=15,relief=RIDGE, overrelief=RAISED)
        self.prescription_button.grid(row=20, column=0, padx=10, pady=20)

        # ==================================== Third Seprator ====================================#
        self.third_seperator = Canvas(self.frame2, width=270, height=1, bd=0, highlightthickness=0)
        self.third_seperator.configure(bg="black")
        self.third_seperator.grid(row=25, column=0)

        # ==================================== Third Button ====================================#
        self.credentials_button = Button(self.frame2, text="Credentials", bg='red', fg="white",
                                         activebackground="#73C2FB",activeforeground="indigo",
                                         command=self.change_doctor_credentials, font=("Comic Sans MS", 15, "bold"),
                                         height=1,cursor="hand2", width=15, relief=RIDGE, overrelief=RAISED)
        self.credentials_button.grid(row=40, column=0, padx=10, pady=20)

        # ==================================== Fourth Seprator ====================================#
        self.fourth_seperator = Canvas(self.frame2, width=270, height=1, bd=0, highlightthickness=0)
        self.fourth_seperator.configure(bg="black")
        self.fourth_seperator.grid(row=45, column=0)

        # ==================================== Fourth Button ====================================#
        self.patient_history_button = Button(self.frame2, text="Patient History", bg='blue',
                                             fg="white",activebackground="#73C2FB",command=self.pathistory,
                                             activeforeground="indigo",font=("Comic Sans MS", 15, "bold"),
                                             height=1, cursor="hand2", width=15,relief=RIDGE, overrelief=RAISED)
        self.patient_history_button.grid(row=80, column=0, padx=10, pady=20)

        # ==================================== Sixth Seprator ====================================#
        self.sixth_seperator = Canvas(self.frame2, width=281, height=1, bd=0, highlightthickness=0)
        self.sixth_seperator.configure(bg="black")
        self.sixth_seperator.grid(row=85, column=0)

        # ========================== Front lable ========================#
        req_numbers= self.check_appointsmentexisting(self.lastuserloggedinname.lower())
        self.changeboard_lb7=Label(self.entry_frame,text=f"Greetings!! Doctor {self.lastuserloggedinname} \n You have got {req_numbers} appointments.")
        self.changeboard_lb7.pack()
        self.show_menu()
        self.wn.mainloop()

    # ==================================== Menu Button ====================================#
    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        log_out = Menu(my_menu)
        my_menu.add_cascade(label="Log Out", menu=log_out)
        log_out.add_cascade(label="Log Out", command=self.logout)

    # ======================================== APPOINTMENT =======================================#
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
        # =================================== SECOND SEPERATOR ==================================#
        self.data = 22
        while self.data <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=70)
            self.data += 10
        # =================================== Fourth SEPERATOR ===================================#
        self.data11 = 22
        while self.data11 <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data11, y=340)
            self.data11 += 10

        # =================================== Fifth SEPERATOR ===================================#
        self.data01 = 22
        while self.data01 <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data01, y=460)
            self.data01 += 10
        # ==================================== Appointment Logo  ====================================#
        self.appointment_photo = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\schedulelogo.png")
        self.appointment_photo_lable = Label(self.navigation_frame0, image=self.appointment_photo, bg="white")
        self.appointment_photo_lable.image = self.appointment_photo
        self.appointment_photo_lable.grid(row=3, column=0, padx=5)

        self.appointment_photo1 = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\schedule.png")
        self.appointment_photo1_lable = Label(self.navigation_frame, image=self.appointment_photo1, bg="white")
        self.appointment_photo1_lable.image = self.appointment_photo1

        # ==================================== HeEADING LABEL - Appointment ====================================#
        self.appointmentboard_lbhead = Label(self.navigation_frame, text="Appointment",image=self.appointment_photo1,
                                             compound=TOP, bg="white",font=('Arial', 18, 'bold', 'underline'), fg='Black')
        self.appointmentboard_lbhead.grid(row=2, column=1, columnspan=3, padx=10, pady=12)

        # ==================================== FIRST LABEL - NAME ====================================#
        self.appointmentboard_lb1 = Label(self.navigation_frame, text=f"Appointment list of Doctor {self.lastuserloggedinname}",
                                          bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.appointmentboard_lb1.grid(row=3, column=1,columnspan=3, padx=10, pady=14)

        # ==================================== FIRST LABEL - NAME ====================================#
        self.appointmentboard_lb2 = Label(self.navigation_frame,text="Appointment Status", bg="white",font=('Arial', 12, 'bold'), fg='Black')
        self.appointmentboard_lb2.grid(row=5, column=1,columnspan=2, padx=10, pady=14)

        # ==================================== THIRD ENTRY - GENDER ====================================#
        self.appointmentboard_entbx3_obj = StringVar()
        self.appointmentboard_entbx3 = ttk.Combobox(self.navigation_frame, state='readonly',
                                                    textvariable=self.appointmentboard_entbx3_obj, width=33, height=5)
        self.appointmentboard_entbx3['values'] = ["Pending", "Approved"]
        self.appointmentboard_entbx3.grid(row=5, column=2,columnspan=2, padx=10, pady=10)

        # =================================== Appointment SEARCH COMBOBOX VALUE ===================================#
        self.appointment_search_obj = StringVar()
        self.appointmentboard_searchbox = ttk.Combobox(self.navigation_frame0, state='readonly',
                                                       textvariable=self.appointment_search_obj, width=27, height=5)
        self.appointmentboard_searchbox['values'] = ["Time", "Patient_Name","Appointed_by"]
        self.appointmentboard_searchbox.grid(row=4, column=0, pady=10)

        # =================================== Appointment SEARCH VALUE ===================================#
        self.appointment_search_value = StringVar()
        self.appointmentboard_searchbx10 = Entry(self.navigation_frame0, textvariable=self.appointment_search_value,
                                                 bg="white", fg="black", font=("arial", 12, "bold"))
        self.appointmentboard_searchbx10.grid(row=5, column=0, pady=10)

        # =================================== Appointment TREE ===================================#
        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.appointmentboard_tree = ttk.Treeview(self.tree_frame,column=("Name", "Time", "Availability", "Patient_Name", "Appointed_by", "Booking_status"),yscrollcommand=self.yscroll.set, height=11)
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
        self.appointmentboard_showbutton = Button(self.navigation_frame, image=self.appointmentboard_showbutton_img,
                                                  command=self.showitemintree_appointmentdata, bg="white",fg="black",
                                                  font=("arial", 15), height=40, width=120)
        self.appointmentboard_showbutton.image = self.appointmentboard_showbutton_img
        self.appointmentboard_showbutton.grid(row=0, column=1, columnspan=3, padx=344, pady=15)

        # =================================== UPDATE Button with picture inserted ===================================#
        self.appointmentboard_updatebutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\updatebutton.png")
        self.appointmentboard_updatebutton = Button(self.navigation_frame,image=self.appointmentboard_updatebutton_img,
                                                    command=self.appointment_updatefrntend, bg="white", fg="black",
                                                    font=("arial", 15), height=25, width=95)
        self.appointmentboard_updatebutton.image = self.appointmentboard_updatebutton_img
        self.appointmentboard_updatebutton.grid(row=15, column=1,columnspan=3, padx=10, pady=15)

        # =================================== DELETE Button with picture inserted ===================================#
        self.appointmentboard_deletebutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\deletebutton.png")
        self.appointmentboard_deletebutton = Button(self.navigation_frame,image=self.appointmentboard_deletebutton_img,
                                                    command=self.deleteappointment, bg="white",fg="black",
                                                    font=("arial", 15), height=25, width=95)
        self.appointmentboard_deletebutton.image = self.appointmentboard_deletebutton_img
        self.appointmentboard_deletebutton.grid(row=16, column=1,columnspan=3, padx=10, pady=15)

        # =================================== SEARCH Button with picture inserted ===================================#
        self.appointmentboard_searchbutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\searchbutton.png")
        self.appointmentboard_searchbutton = Button(self.navigation_frame0,image=self.appointmentboard_searchbutton_img,
                                                    command=self.appointmentsearch, bg="white", fg="black",
                                                    font=("arial", 15), height=25, width=95)
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
        reqdata = self.doctor_backend.appointment_backend_showdata(self.lastuserloggedinname)
        for i in reqdata:
            self.appointmentboard_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6]))
        self.appointmentboard_tree.bind("<Double-1>", self.appointment_onitemselect)

    # =================================== SELECTING CONTENT IN TREE ===================================#
    def appointment_onitemselect(self, event):
        selected_row0 = self.appointmentboard_tree.selection()[0]
        selected_item0 = self.appointmentboard_tree.item(selected_row0, 'values')
        self.update_index0 = self.appointmentboard_tree.item(selected_row0, 'text')

        self.appointmentboard_entbx3.delete(0, END)
        self.appointmentboard_entbx3.insert(0, selected_item0[2])

    # =================================== UPDATING CONTENT IN TREE ===================================#
    def appointment_updatefrntend(self):
        if self.update_index0 == "":
            messagebox.showerror("Error", "Please select a row first")
        else:
            appointment_docsapptatus = self.appointmentboard_entbx3_obj.get()
            if len(appointment_docsapptatus) != 0:
                if self.doctor_backend.appointment_status_update(self.update_index0, appointment_docsapptatus):
                    messagebox.showinfo('Item', "Item Updated")
                    self.showitemintree_appointmentdata()
                    self.update_index0 = ""
                else:
                    messagebox.showerror("Error", 'Can not be updated !!!')
            else:
                messagebox.showerror("Error", "Can't leave any blank spaces.")

    # =================================== SEARCHING CONTENT IN DATABASE ===================================#
    def appointmentsearch(self):
        if len(self.appointment_search_value.get()) != 0 and len(self.appointment_search_obj.get()) != 0:
            searcheed_data0 = self.doctor_backend.return_appointment_search_data(self.appointment_search_value.get(),
                                                                                 self.appointment_search_obj.get(),self.lastuserloggedinname)
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

    # ========================================= Deleting Appointment Data ====================================#
    def deleteappointment(self):
        if self.update_index0 == "":
            messagebox.showerror("Can't delete", "Please select a row first.")
        else:
            if self.staff_backend.delete_appointments(self.update_index0):
                messagebox.showinfo("Appointment Cleared", "The appointment is now cleared.")
                self.appointmentboard_tree.delete(*self.appointmentboard_tree.get_children())
                self.showitemintree_appointmentdata()
            else:
                messagebox.showerror("Can't delete", "Delete Failed")

    #==================================== Prescription =================================================#
    def prescriptions(self):
        self.deleteframe()
        self.display_date()
        self.display_time()
        self.endphoto()

        # =================================== FIRST SEPERATOR ===================================#
        self.data0 = 22
        while self.data0 <= 790:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=12)
            self.data0 += 10
        # =================================== SECOND SEPERATOR ===================================#
        self.data = 22
        while self.data <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=85)
            self.data += 10

        # =================================== THIRD SEPERATOR ===================================#
        self.data1 = 22
        while self.data1 <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=350)
            self.data1 += 10

        # =================================== Fourth SEPERATOR ===================================#
        self.data11 = 22
        while self.data11 <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data11, y=410)
            self.data11 += 10

        # =================================== Fifth SEPERATOR ===================================#
        self.data01 = 22
        while self.data01 <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data01, y=460)
            self.data01 += 10

        # ==================================== Patient Logo  ====================================#
        self.prescription_pic = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\prescription.png")
        self.prescription_pic_lable = Label(self.navigation_frame0, image=self.prescription_pic, bg="white")
        self.prescription_pic_lable.image = self.prescription_pic
        self.prescription_pic_lable.grid(row=3, column=0, padx=5)

        #==============================first label- all appproved patient name=========================#
        self.prescription_lb01=Label(self.navigation_frame,text="Patient_name", bg="white", font=('Arial',12, 'bold', ),fg='black')
        self.prescription_lb01.grid(row=2,column=1,padx=10,pady=20)


        # ==============================Combo Entry - Patients =========================#
        self.prescription_lb1_obj=StringVar()
        self.prescription_lb1=ttk.Combobox(self.navigation_frame,textvariable=self.prescription_lb1_obj,state="readonly", width=33, height=5)
        self.prescription_lb1.grid(row=2,column=2,padx=10, pady=15)
        self.approvedpatientdata()

        # ==============================Lable Service =========================#
        self.prescription_lb02 = Label(self.navigation_frame, text="Services", bg="white",font=('Arial', 12, 'bold',), fg='black')
        self.prescription_lb02.grid(row=3, column=1, padx=10, pady=20)

        # ==============================Combo Entry - Service=========================#
        self.prescription_lb2 = ttk.Combobox(self.navigation_frame, state="readonly", width=33, height=5)
        self.prescription_lb2.grid(row=3, column=2, padx=10, pady=15)
        self.showingservices()

        # ==============================Lable medicine=========================#
        self.prescription_lb03 = Label(self.navigation_frame, text="Mediciness", bg="white", font=('Arial', 12, 'bold',),fg='black')
        self.prescription_lb03.grid(row=4, column=1, padx=10, pady=20)

        # ==============================Combo Entry - Medicine=========================#
        self.prescription_lb3 = ttk.Combobox(self.navigation_frame, state="readonly", width=33, height=5)
        self.prescription_lb3.grid(row=4, column=2, padx=10, pady=15)
        self.showingmedicines()

        # ==============================Lable Quantity=========================#
        self.prescription_lb4= Label(self.navigation_frame, text="Quantity", bg="white",font=('Arial', 12, 'bold',), fg='black')
        self.prescription_lb4.grid(row=5,column=1,padx=10,pady=20)

        #============================== Entry Quantity=========================#
        self.prescription_entry1= Entry(self.navigation_frame,  bg="white", fg="black", font=("arial", 15, "bold"))
        self.prescription_entry1.grid(row=5, column=2, padx=10, pady=15)
        self.prescription_id_list=[]

        # =================================== Patient SEARCH COMBOBOX VALUE ===================================#
        self.prescriptionboard_searchbox = Label(self.navigation_frame0, text="Search Prescription ID", bg="white",
                                                 font=('Arial', 12, 'bold',), fg='black')
        self.prescriptionboard_searchbox.grid(row=4, column=0, pady=5, padx=10)

        # =================================== prescription SEARCH VALUE ===================================#
        self.prescriptionboard_searchbx10 = Entry(self.navigation_frame0, bg="white",fg="black", font=("arial", 12, "bold"))
        self.prescriptionboard_searchbx10.grid(row=5, column=0, pady=5, padx=10)

        #============================= Priscription Tree =======================#
        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.prescription_tree = ttk.Treeview(self.tree_frame, column=("Patient_name", "Service_name", "Servive_type", "Service_price", "Medicine_name", "Medicine_type","Medicine_price", "Quantity"),yscrollcommand=self.yscroll.set,height=11)
        self.yscroll.config(command=self.prescription_tree.yview)
        self.prescription_tree.pack()
        self.prescription_tree['show'] = 'headings'
        self.prescription_tree.column('Patient_name', width=110, anchor='center')
        self.prescription_tree.column('Service_name', width=92, anchor='center')
        self.prescription_tree.column('Servive_type', width=90, anchor='center')
        self.prescription_tree.column('Service_price', width=90, anchor='center')
        self.prescription_tree.column('Medicine_name', width=100, anchor='center')
        self.prescription_tree.column('Medicine_type', width=100, anchor='center')
        self.prescription_tree.column('Medicine_price', width=100, anchor='center')
        self.prescription_tree.column('Quantity', width=110, anchor='center')
        self.prescription_tree.heading('Patient_name', text='Patient_name')
        self.prescription_tree.heading('Service_name', text='Service_name')
        self.prescription_tree.heading('Servive_type', text='Servive_type')
        self.prescription_tree.heading('Service_price', text='Service_price')
        self.prescription_tree.heading('Medicine_name', text='Medicine_name')
        self.prescription_tree.heading('Medicine_type', text='Medicine_type')
        self.prescription_tree.heading('Medicine_price', text='Medicine_price')
        self.prescription_tree.heading('Quantity', text='Medicine_quantity')
        # self.prescription_tree.tag_configure('odd', background='#E8E8E8')
        # self.prescription_tree.tag_configure('even', background='#DFDFDF')

        # =================================== ADD Button with picture inserted ===================================#
        self.service_addbutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\addbutton.png")
        self.service_addbutton = Button(self.navigation_frame, image=self.service_addbutton_img, bg="white",
                                        command=self.adding_prescription, fg="black", font=("arial", 15), height=25, width=95)
        self.service_addbutton.image = self.service_addbutton_img
        self.service_addbutton.grid(row=8, column=1, columnspan=2, padx=10, pady=10)

        # =================================== Show Button with picture inserted ===================================#
        self.prescription_showbutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\showbutton.png")
        self.prescription_showbutton = Button(self.navigation_frame, image=self.prescription_showbutton_img,
                                              command=self.show_data_inprescriptiontree,bg="white",fg="black",
                                              font=("arial", 15), height=37, width=140)
        self.prescription_showbutton.image = self.prescription_showbutton_img
        self.prescription_showbutton.grid(row=1, column=1, columnspan=3, padx=333, pady=25)

        # =================================== Submit Button with picture inserted ===================================#
        self.submit_button_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\submit.png")
        self.submit_button = Button(self.navigation_frame, image=self.submit_button_img,command=self.submit_prescriptions,
                                    bg="white",fg="black", font=("arial", 15), height=25, width=95)
        self.submit_button.image = self.submit_button_img
        self.submit_button.grid(row=9, column=1, columnspan=3, padx=10, pady=15)

        #=================================== Delete Button with picture inserted ===================================#
        self.prescription_deletebutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\deletebutton.png")
        self.prescription_deletebutton = Button(self.navigation_frame, image=self.prescription_deletebutton_img,
                                                command=self.deleteprescription, bg="white",fg="black",
                                                font=("arial", 15), height=25, width=95)
        self.prescription_deletebutton.image = self.prescription_deletebutton_img
        self.prescription_deletebutton.grid(row=8, column=2, padx=10, pady=10)

        # =================================== SEARCH Button with picture inserted ===================================#
        self.prescription_booard_searchbutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\searchbutton.png")
        self.prescription_booard_searchbutton = Button(self.navigation_frame0, image=self.prescription_booard_searchbutton_img,
                                                       command=self.search_prescription,bg="white", fg="black",
                                                       font=("arial", 15),height=25, width=95)
        self.prescription_booard_searchbutton.image = self.prescription_booard_searchbutton_img
        self.prescription_booard_searchbutton.grid(row=6, column=0, pady=5, padx=20)

    #=================================  SHOWING APPROVED PATIENT DATA =====================#
    def approvedpatientdata(self):
        approved_patient= []
        dataretrived=self.doctor_backend.return_approved_patientname(self.lastuserloggedinname)
        for i in dataretrived:
            realdatarequired = self.admin_backend.return_patient_search_data_schedule(i[4])
            approved_patient.append(("ID:",realdatarequired[0][0],":",realdatarequired[0][1]))
        self.prescription_lb1['values']=approved_patient


    #================================ Showing revelant Services ===========================#
    def showingservices(self):
        services_data=[]
        servicesdata=self.admin_backend.service_backend_showdata()
        for i in servicesdata:
            services_data.append((i[1],i[2]))
        self.prescription_lb2['values']=services_data

    # ================================ Showing revelant Medicines ===========================#
    def showingmedicines(self):
        medicine_data = []
        medicinedata = self.admin_backend.medicine_backend_showdata()
        for i in medicinedata:
            medicine_data.append((i[1], i[2]))
        self.prescription_lb3['values'] =medicine_data

    #================================= Adding Prescriptions =================================#
    def adding_prescription(self):
        service_index = self.prescription_lb2.current()
        req_services = self.all_services[service_index]
        medicine_index = self.prescription_lb3.current()
        req_medicines = self.all_medicines[medicine_index]
        qty = self.prescription_entry1.get()
        patientname = self.prescription_lb1_obj.get()
        if len(self.prescription_lb2.get()) != 0 and len(self.prescription_lb3.get()) != 0 and (len(patientname)) != 0 and len(qty) != 0:
            if qty.isdigit():
                patient_index = patientname[4]
                self.prescription_id_list.append((patient_index,req_services[0],req_medicines[0],qty))
                self.prescription_tree.insert('', 'end', text='',value=(patientname,req_services[1],req_services[2],req_services[3],req_medicines[1],req_medicines[2],req_medicines[3], qty))
            else:
                messagebox.showerror("Numeric data needed.", "Quantity must be numeric.")
        else:
            messagebox.showerror("EMPTY BOXES","You can't leave any boxes empty.")

    #================================= Show all data =======================================#
    def show_data_inprescriptiontree(self):
        self.prescription_tree.delete(*self.prescription_tree.get_children())
        data=self.doctor_backend.return_all_prescribed_data()
        for i in data:
            self.prescription_tree.insert('', 'end', text=i[0], value=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
        self.prescription_tree.bind("<Double-1>", self.prescription_onitemselect)

    # =================================== SELECTING Appointment Index IN TREE ===================================#
    def prescription_onitemselect(self, event):
        selected_row0 = self.prescription_tree.selection()[0]
        self.update_index0 = self.prescription_tree.item(selected_row0, 'text')
        print(self.update_index0)

    #=================================Submitting the prescriptions ==============================#
    def submit_prescriptions(self):
        if self.doctor_backend.add_prescription(self.prescription_id_list):
            messagebox.showinfo("Prescription Added","The desired prescription is added.")
            self.prescription_tree.delete(*self.prescription_tree.get_children())
        else:
            messagebox.showerror("Error", "can't add your prescription")

    #================================ Search data ============================================#
    def search_prescription(self):
        if len(self.prescriptionboard_searchbx10.get()) != 0:
            self.prescription_tree.delete(*self.prescription_tree.get_children())
            data=self.doctor_backend.return_specified_prescribed_data(self.prescriptionboard_searchbx10.get())
            if len(data) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
            else:
                for i in data:
                    self.prescription_tree.insert('', 'end', text=i[0], value=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")

    # ========================================= Deleting Prescriptions Data ====================================#
    def deleteprescription(self):
        if self.update_index0 == "":
            messagebox.showerror("Can't delete", "Please select a row first.")
        else:
            if self.doctor_backend.delete_prescription(self.update_index0):
                messagebox.showinfo("Prescription Cleared", "The prescription is now cleared.")
                self.show_data_inprescriptiontree()
            else:
                messagebox.showerror("Can't delete", "Delete Failed")

    # =================================== Changing Credentials ==========================================#
    def change_doctor_credentials(self):
        self.deleteframe()
        # ==================================== Change Credential Logo  ====================================#
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
        self.changeboard_lbhead = Label(self.tree_frame, text="Change Credentials",image=self.change_credential_pic,
                                        compound=TOP, bg="white",font=('Arial', 18, 'bold', 'underline'), fg='Black')
        self.changeboard_lbhead.grid(row=2, column=1, columnspan=2, padx=115, pady=13)

        # ==================================== FIRST LABEL - NAME ====================================#
        self.changeboard_lb1 = Label(self.navigation_frame, text="Username", bg="white", font=('Arial', 12, 'bold'),fg='Black')
        self.changeboard_lb1.grid(row=3, column=1, padx=10, pady=15)

        # ==================================== Second LABEL - OLd Password ====================================#
        self.changeboard_lb2 = Label(self.navigation_frame, text="Old Password", bg="white",font=('Arial', 12, 'bold'), fg='Black')
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

        # ====================================== Required Buttons ========================================#
        self.changeboard_btn1_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\updatebutton.png")
        self.changeboard_btn1 = Button(self.navigation_frame, image=self.changeboard_btn1_img,command=self.updating_credentials,
                                       bg="white", fg="black",font=("arial", 15), height=25, width=95)
        self.changeboard_btn1.image = self.changeboard_btn1_img
        self.changeboard_btn1.grid(row=7, column=1, columnspan=2, padx=10, pady=22)

        # ==================================== Fifth LABEL -Instruction to follow ====================================#
        self.changeboard_lb5 = Label(self.navigation_frame, text="Please follow the following Instruction.",bg="white",
                                     font=('Arial', 12, 'bold', "underline"), fg='Black')
        self.changeboard_lb5.grid(row=8, column=1, columnspan=2, padx=10, pady=14)

        self.changeboard_lb6 = Label(self.navigation_frame, text="Ensure your password are 8 character long.\n\n"
                                                                 "Please don't use your birthdates, phone numbers for passwords.\n\n"
                                                                 "Passwords mustn't be shared with anyone.",bg="white",
                                     font=('Arial', 10, 'bold'), fg='Black')
        self.changeboard_lb6.grid(row=9, column=1, columnspan=2, pady=14)

        # ===================================== removing date frame=======================================#
        # self.rm_dateframe = Label(self.navigation_frame0, text="")
        # self.rm_dateframe.pack()

    def updating_credentials(self):
        username = self.changeboard_entbx1.get()
        oldpassword = self.changeboard_entbx2.get()
        newpassword = self.changeboard_entbx3.get()
        retype_newpassword = self.changeboard_entbx4.get()
        if len(username) != 0 and len(oldpassword) != 0 and len(newpassword) != 0 and len(retype_newpassword) != 0:
            if username == self.lastuserloggedin.lower():
                if self.doctor_backend.return_doctor_search_data(username)[0][0] == oldpassword:
                    if len(newpassword) >= 8:
                        if newpassword == retype_newpassword:
                            self.doctor_backend.update_doctor_login_data(retype_newpassword, username)
                            messagebox.showinfo("Success", "Credentials changed.")
                        else:
                            messagebox.showerror("Password didn't matched",
                                                 "The password you provided in \n  both column are not identical.")
                    else:
                        messagebox.showerror("Password too Short.", "The password must be 8 character long.")
                else:
                    messagebox.showerror("Wrong Password", "The password you provided didn't matched.")
            else:
                messagebox.showerror("Unauthenticated user", "You can't change other people credentials.")
        else:
            messagebox.showerror("Empty Input", "You can't leave any boxes empty.")

    # =================================== Check existing Appointments ===================================#
    def check_appointsmentexisting(self,value):
        return self.doctor_backend.check_existing_appoitments(value)

    #====================================Patient  history ===============================================#
    def pathistory(self):
        self.deleteframe()
        # ==================================== First Seperator ====================================#
        self.data0 = 22
        while self.data0 <= 720:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=300)
            self.data0 += 10
        # ==================================== SCEOND Seperator ====================================#
        self.data = 22
        while self.data <= 720:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=420)
            self.data += 10
        # ============================= Priscription Tree =======================#
        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.patient_history_tree = ttk.Treeview(self.tree_frame, column=("Patient_name", "Service_name", "Servive_type", "Service_price", "Medicine_name", "Medicine_type","Medicine_price", "Quantity"),yscrollcommand=self.yscroll.set, height=11)
        self.yscroll.config(command=self.patient_history_tree.yview)
        self.patient_history_tree.pack()
        self.patient_history_tree['show'] = 'headings'
        self.patient_history_tree.column('Patient_name', width=90, anchor='center')
        self.patient_history_tree.column('Service_name', width=90, anchor='center')
        self.patient_history_tree.column('Servive_type', width=90, anchor='center')
        self.patient_history_tree.column('Service_price', width=90, anchor='center')
        self.patient_history_tree.column('Medicine_name', width=90, anchor='center')
        self.patient_history_tree.column('Medicine_type', width=90, anchor='center')
        self.patient_history_tree.column('Medicine_price', width=90, anchor='center')
        self.patient_history_tree.column('Quantity', width=90, anchor='center')
        self.patient_history_tree.heading('Patient_name', text='Patient_name')
        self.patient_history_tree.heading('Service_name', text='Service_name')
        self.patient_history_tree.heading('Servive_type', text='Servive_type')
        self.patient_history_tree.heading('Service_price', text='Service_price')
        self.patient_history_tree.heading('Medicine_name', text='Medicine_name')
        self.patient_history_tree.heading('Medicine_type', text='Medicine_type')
        self.patient_history_tree.heading('Medicine_price', text='Medicine_price')
        self.patient_history_tree.heading('Quantity', text='Med_quantity')


        # ==================================== Change Credential Logo  ====================================#
        self.patient_history_pic = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\patienthistory.png")
        self.patient_history_pic_lable = Label(self.tree_frame, image=self.patient_history_pic, bg="white")
        self.patient_history_pic_lable.image = self.patient_history_pic

        #==================================== First Lable ================================================#
        self.patient_history_lb1 = Label(self.navigation_frame, text="LOOK UP PATIENT HISTORY",image=self.patient_history_pic,
                                         compound=TOP, bg="white", font=('Arial', 15, 'bold','underline'),fg='Black')
        self.patient_history_lb1.grid(row=3, column=1,columnspan=4,padx=230, pady=10)

        #==================================== Prescribed Patient List ===================================#
        self.patient_history_entbx1 = ttk.Combobox(self.navigation_frame, state='readonly', width=33, height=5)
        self.patient_history_entbx1['values'] = self.doctor_backend.return_all_prescribed_patient()
        self.patient_history_entbx1.grid(row=6, column=1,columnspan=4, padx=10, pady=10)

        # =================================== SEARCH Button with picture inserted ===================================#
        self.scheduleboard_searchbutton_img = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\searchbutton.png")
        self.scheduleboard_searchbutton = Button(self.navigation_frame, image=self.scheduleboard_searchbutton_img,
                                                 command=self.search_history_prescription, bg="white", fg="black",
                                                 font=("arial", 15), height=25, width=95)
        self.scheduleboard_searchbutton.image = self.scheduleboard_searchbutton_img
        self.scheduleboard_searchbutton.grid(row=7, column=1,columnspan=4, pady=10)

        # ==================================== FIRST LABEL - NAME ====================================#
        self.patientboard_lb1 = Label(self.navigation_frame, text="Name of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb1.grid(row=8, column=1, padx=10, pady=9)

        # ==================================== SCEOND LABEL - AGE ====================================#
        self.patientboard_lb2 = Label(self.navigation_frame, text="Age of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb2.grid(row=9, column=1, padx=10, pady=9)

        # ==================================== THIRD LABEL - GENDER ====================================#
        self.patientboard_lb3 = Label(self.navigation_frame, text="Gender of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb3.grid(row=10, column=1, padx=10, pady=9)

        # ==================================== FOURTH LABEL - Weight ====================================#
        self.patientboard_lb4 = Label(self.navigation_frame, text="Weight of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb4.grid(row=10, column=3, padx=10, pady=9)

        # ==================================== FIFTH LABEL - Height ====================================#
        self.patientboard_lb5 = Label(self.navigation_frame, text="Height of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb5.grid(row=8, column=3, padx=10, pady=9)

        # ==================================== SIXTH LABEL - Address ====================================#
        self.patientboard_lb6 = Label(self.navigation_frame, text="Address of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb6.grid(row=9, column=3, padx=10, pady=9)

        # ==================================== Seventh LABEL - Contact ====================================#
        self.patientboard_lb8 = Label(self.navigation_frame, text="Contact number of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb8.grid(row=11, column=2,padx=10, pady=8)

        #  ==================================== FIRST LABEL - NAME ====================================#
        self.patientboardsrch_lb1 = Label(self.navigation_frame, bg="white", font=('Arial', 12, 'bold'), fg='red')
        self.patientboardsrch_lb1.grid(row=8, column=2, padx=10, pady=9)

        # ==================================== SCEOND LABEL - AGE ====================================#
        self.patientboardsrch_lb2 = Label(self.navigation_frame, bg="white", font=('Arial', 12, 'bold'), fg='red')
        self.patientboardsrch_lb2.grid(row=9, column=2, padx=10, pady=9)

        # ==================================== THIRD LABEL - GENDER ====================================#
        self.patientboardsrch_lb3 = Label(self.navigation_frame, bg="white", font=('Arial', 12, 'bold'), fg='red')
        self.patientboardsrch_lb3.grid(row=10, column=2, padx=10, pady=9)

        # ==================================== FOURTH LABEL - Weight ====================================#
        self.patientboardsrch_lb4 = Label(self.navigation_frame, bg="white", font=('Arial', 12, 'bold'), fg='red')
        self.patientboardsrch_lb4.grid(row=10, column=4, padx=10, pady=9)

        # ==================================== FIFTH LABEL - Height ====================================#
        self.patientboardsrch_lb5 = Label(self.navigation_frame, bg="white", font=('Arial', 12, 'bold'), fg='red')
        self.patientboardsrch_lb5.grid(row=8, column=4, padx=10, pady=9)

        # ==================================== SIXTH LABEL - Address ====================================#
        self.patientboardsrch_lb6 = Label(self.navigation_frame, bg="white", font=('Arial', 12, 'bold'), fg='red')
        self.patientboardsrch_lb6.grid(row=9, column=4, padx=10, pady=9)

        # ==================================== Seventh LABEL - Contact ====================================#
        self.patientboardsrch_lb8 = Label(self.navigation_frame, bg="white", font=('Arial', 12, 'bold'), fg='red')
        self.patientboardsrch_lb8.grid(row=11, column=3, padx=10, pady=8)

    # ================================ Search data ============================================#
    def search_history_prescription(self):
        if len(self.patient_history_entbx1.get()) != 0:
            self.patient_history_tree.delete(*self.patient_history_tree.get_children())
            data = self.doctor_backend.return_specified_prescribed_data_history(self.patient_history_entbx1.get())
            if len(data) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
            else:
                for i in data:
                    self.patient_history_tree.insert('','end',text='',value=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                self.givepatient_details()
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")

    #================================ Patient Detail ==========================================#
    def givepatient_details(self):
        reqPatient_data=self.staff_backend.return_patient_search_data(self.patient_history_entbx1.get(),"Patient_Name")
        reqPatient_data_lst=list(reqPatient_data[0])
        for i in range(len(reqPatient_data_lst)):
            name=reqPatient_data_lst[(i-7)]
            age=reqPatient_data_lst[(i-6)]
            gender=reqPatient_data_lst[(i-5)]
            weight=reqPatient_data_lst[(i-4)]
            height=reqPatient_data_lst[(i-3)]
            address=reqPatient_data_lst[(i-2)]
            contact=reqPatient_data_lst[(i-1)]

            #  ==================================== FIRST LABEL - NAME ====================================#
            self.patientboardsrch_lb1.destroy()
            self.patientboardsrch_lb1 = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
            self.patientboardsrch_lb1.configure(text=name)
            self.patientboardsrch_lb1.grid(row=8, column=2, padx=10, pady=9)

            # ==================================== SCEOND LABEL - AGE ====================================#
            self.patientboardsrch_lb2.destroy()
            self.patientboardsrch_lb2 = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
            self.patientboardsrch_lb2.configure(text=age)
            self.patientboardsrch_lb2.grid(row=9, column=2, padx=10, pady=9)

            # ==================================== THIRD LABEL - GENDER ====================================#
            self.patientboardsrch_lb3.destroy()
            self.patientboardsrch_lb3 = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
            self.patientboardsrch_lb3.configure(text=gender)
            self.patientboardsrch_lb3.grid(row=10, column=2, padx=10, pady=9)

            # ==================================== FOURTH LABEL - Weight ====================================#
            self.patientboardsrch_lb4.destroy()
            self.patientboardsrch_lb4 = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
            self.patientboardsrch_lb4.configure(text=weight)
            self.patientboardsrch_lb4.grid(row=10, column=4, padx=10, pady=9)

            # ==================================== FIFTH LABEL - Height ====================================#
            self.patientboardsrch_lb5.destroy()
            self.patientboardsrch_lb5 = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
            self.patientboardsrch_lb5.configure(text=height)
            self.patientboardsrch_lb5.grid(row=8, column=4, padx=10, pady=9)

            # ==================================== SIXTH LABEL - Address ====================================#
            self.patientboardsrch_lb6.destroy()
            self.patientboardsrch_lb6 = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
            self.patientboardsrch_lb6.configure(text=address)
            self.patientboardsrch_lb6.grid(row=9, column=4, padx=10, pady=9)

            # ==================================== Seventh LABEL - Contact ====================================#
            self.patientboardsrch_lb8.destroy()
            self.patientboardsrch_lb8 = Label(self.navigation_frame, bg="white",font=('Arial', 12, 'bold'), fg='red')
            self.patientboardsrch_lb8.configure(text=contact)
            self.patientboardsrch_lb8.grid(row=11, column=3, padx=10, pady=8)
            break

    # =================================== DATE AND TIME SELECTED FRAME ===================================#
    def display_time(self):
        current_time = tm.strftime('%I:%M:%S %p ')
        self.wn.after(200, self.display_time)
        clock_label = Label(self.navigation_frame0, text=current_time, font=("Ticking Timebomb BB Regular", 27),
                            bg='white', fg='#000000')
        clock_label.grid(row=0, column=0, padx=14)

    def display_date(self):
        x = datetime.datetime.now()
        current_date = x.strftime('%A,%B %d')
        date_label = Label(self.navigation_frame0, text=current_date, font="Ariel 15", bg='white', fg='#2b2b2b')
        date_label.grid(row=1, column=0, padx=15)

    # =================================== DELETE LAST SELECTED FRAME ===================================#
    def deleteframe(self):
        for widget in self.entry_frame.winfo_children():
            widget.destroy()

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
        self.photo00 = PhotoImage(file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\doctor_end.png")
        self.photo_lable00 = Label(self.navigation_frame0, image=self.photo00, bg="white")
        self.photo_lable00.image = self.photo00
        self.photo_lable00.grid(row=8, column=0, padx=5, pady=40)

# Doctor_interface("test","test")