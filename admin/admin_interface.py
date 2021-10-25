# ================================ Importing all the necessary modules ============================#
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
from PIL import Image, ImageTk
import time as tm
import datetime
from admin.admin_interface_backend import Adminbackend


class Addservice:
    def __init__(self):
        # =============================== Creating Tkinter Window ================================#
        self.wn = Tk()
        self.wn.title("Admin Panel")
        self.wn.geometry("1370x735+0+0")
        self.wn.configure(bg="white")
        self.wn.resizable(False, False)

        # ============================= making update index global ===============================#
        self.admin_backend = Adminbackend()
        self.update_index0 = ""
        self.update_index00 = ""
        self.update_index = ""

        # =========================== Importing all necessary photo ==============================#
        self.title_photo = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\admin_top.png")
        self.title_photo_lable = Label(self.wn, image=self.title_photo, bg="white")
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=0, y=0)

        self.title_photo01 = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\adminservice.png")
        self.title_photo01_lable = Label(self.wn, image=self.title_photo01)
        self.title_photo01_lable.image = self.title_photo01
        self.title_photo01_lable.place(x=310, y=0)

        # ==================================== Creating Frames ===================================#
        # ======================================= Main Frame  ====================================#
        self.frame1 = Frame(self.wn, bg="white")
        self.frame1.place(x=0, y=260)
        # ======================================= Tree Frame  ====================================#
        self.tree_frame = Frame(self.wn, bg="white")
        self.tree_frame.place(x=312, y=0)
        # =================================== Navigation Frame  ==================================#
        self.navigation_frame = Frame(self.wn, bg="white")
        self.navigation_frame.place(x=312, y=247)
        # =================================== NAvigation0 Frame  =================================#
        self.navigation_frame0 = LabelFrame(self.wn, bg="white", bd=2)
        self.navigation_frame0.place(x=1125, y=0)

        # ==================================== Major Heading =====================================#
        self.lb_heading_inital = Label(self.frame1, text="Admin", bg="white", font=('Impact', 35, 'bold', 'underline'),fg='red')
        self.lb_heading_inital.grid(row=20, column=40, padx=16, pady=10)
        self.lb_heading_end = Label(self.frame1, text="Panel", bg="white", font=('Impact', 35, 'bold', 'underline'),fg='blue')
        self.lb_heading_end.grid(row=20, column=80, padx=13, pady=10)

        # =================================== Creating Frame-2 ===================================#
        self.frame2 = Frame(self.wn, bg="white")
        self.frame2.place(x=1, y=350)

        # ============================ Creating Seprator and Buttons =============================#

        # =================================== First Seprator =====================================#
        self.first_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.first_seperator.configure(bg="black")
        self.first_seperator.grid(row=0, column=0)

        # ==================================== First Button ======================================#
        self.service_button = Button(self.frame2, text="Services", bg='white', fg="black", activebackground="#73C2FB",
                                     activeforeground="indigo", cursor="hand2", font=("Comic Sans MS", 14, "bold"),
                                     height=1, command=self.services, width=15, relief=FLAT, overrelief=RIDGE)
        self.service_button.grid(row=5, column=0, padx=58, pady=7)

        # =================================+ Second Seprator ====================================#
        self.second_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.second_seperator.configure(bg="black")
        self.second_seperator.grid(row=10, column=0)

        # ==================================== Second Button ====================================#
        self.medicine_button = Button(self.frame2, text="Medicines", bd=1, bg='yellow', fg="black",
                                      activebackground="#73C2FB", activeforeground="indigo", cursor="hand2",
                                      font=("Comic Sans MS", 14, "bold"), height=1, command=self.medicine, width=15,
                                      relief=RIDGE, overrelief=RAISED)
        self.medicine_button.grid(row=20, column=0, padx=58, pady=7)

        # ==================================== Third Seprator ===================================#
        self.third_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.third_seperator.configure(bg="black")
        self.third_seperator.grid(row=25, column=0)

        # ==================================== Third Button =====================================#
        self.doctor_button = Button(self.frame2, text="Doctors", bd=1, bg='red', fg="white", activebackground="#73C2FB",
                                    activeforeground="indigo", font=("Comic Sans MS", 14, "bold"), height=1,
                                    cursor="hand2", command=self.doctorboard, width=15, relief=RIDGE, overrelief=RAISED)
        self.doctor_button.grid(row=40, column=0, padx=30, pady=7)

        # ==================================== Fourth Seprator ==================================#
        self.fourth_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.fourth_seperator.configure(bg="black")
        self.fourth_seperator.grid(row=45, column=0)

        # ==================================== Fourth Button ====================================#
        self.staff_button = Button(self.frame2, text="Staff", bd=1, bg='red', fg="white", activebackground="#73C2FB",
                                   activeforeground="indigo", font=("Comic Sans MS", 14, "bold"), height=1,
                                   cursor="hand2", command=self.staffboard, width=15, relief=RIDGE, overrelief=RAISED)
        self.staff_button.grid(row=60, column=0, padx=30, pady=7)

        # ==================================== Fifth Seprator ===================================#
        self.fifth_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.fifth_seperator.configure(bg="black")
        self.fifth_seperator.grid(row=65, column=0)

        # ==================================== Fifth Button =====================================#
        self.patient_button = Button(self.frame2, text="Patient", bd=1, bg='blue', fg="white",
                                     activebackground="#73C2FB", activeforeground="indigo",
                                     font=("Comic Sans MS", 14, "bold"), command=self.patientboard, height=1,
                                     cursor="hand2", width=15, relief=RIDGE, overrelief=RAISED)
        self.patient_button.grid(row=80, column=0, padx=30, pady=7)

        # ==================================== Sixth Seprator ===================================#
        self.sixth_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.sixth_seperator.configure(bg="black")
        self.sixth_seperator.grid(row=85, column=0)

        # ==================================== Sixth Button =====================================#
        self.schedule_button = Button(self.frame2, text="Schedule", bd=1, bg='green', fg="white",
                                      activebackground="#73C2FB", activeforeground="indigo",
                                      font=("Comic Sans MS", 14, "bold"), command=self.scheduleboard, height=1,
                                      cursor="hand2", width=15, relief=RIDGE, overrelief=RAISED)
        self.schedule_button.grid(row=100, column=0, padx=30, pady=7)

        # ==================================== Seventh Seprator =================================#
        self.seventh_seperator = Canvas(self.frame2, width=300, height=1, bd=0, highlightthickness=0)
        self.seventh_seperator.configure(bg="black")
        self.seventh_seperator.grid(row=105, column=0)

        self.show_menu()
        self.wn.mainloop()

    # ========================================== Menu Button =====================================#
    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        log_out = Menu(my_menu)
        my_menu.add_cascade(label="Log Out", menu=log_out)
        log_out.add_cascade(label="Log Out", command=self.logout)

    # ==================================== Window for Service Button==============================#
    def services(self):
        self.deleteframe()
        self.endphoto()
        self.display_date()
        self.display_time()
        # ==================================== First Seperator ===================================#
        self.data0 = 22
        while self.data0 <= 800:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=7)
            self.data0 += 10
        # ==================================== Second Seperator =================================#
        self.data = 22
        while self.data <= 800:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=70)
            self.data += 10
        # ==================================== Service Logo  ====================================#
        self.service_photo = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\service_logo.png")
        self.service_photo_lable = Label(self.navigation_frame0, image=self.service_photo, bg="white")
        self.service_photo_lable.image = self.service_photo
        self.service_photo_lable.grid(row=3, column=0, padx=5)

        # ==================================== First label - Name ===============================#
        self.service_lb1 = Label(self.navigation_frame, text="Name of the Service", bg="white",
                                 font=('Arial', 12, 'bold'), fg='Black')
        self.service_lb1.grid(row=2, column=1, padx=40, pady=20)

        # ==================================== Second label - Type ==============================#
        self.service_lb2 = Label(self.navigation_frame, text="Type of the Service", bg="white",
                                 font=('Arial', 12, 'bold'), fg='Black')
        self.service_lb2.grid(row=3, column=1, padx=13, pady=20)

        # ==================================== Third label - Price ==============================#
        self.service_lb3 = Label(self.navigation_frame, text="Price of the Service", bg="white",
                                 font=('Arial', 12, 'bold'), fg='Black')
        self.service_lb3.grid(row=4, column=1, padx=13, pady=20)

        # ==================================== Fourth label - Availablity =======================#
        self.service_lb4 = Label(self.navigation_frame, text="Available time of the Service", bg="white",
                                 font=('Arial', 12, 'bold'), fg='Black')
        self.service_lb4.grid(row=5, column=1, padx=13, pady=20)

        # ==================================== Fifth label - Prescription =======================#
        self.service_lb5 = Label(self.navigation_frame, text="Prescription for the Service", bg="white",
                                 font=('Arial', 12, 'bold'), fg='Black')
        self.service_lb5.grid(row=6, column=1, padx=13, pady=20)

        # ==================================== Third Seprator ===================================#
        self.data1 = 22
        while self.data1 <= 800:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=400)
            self.data1 += 10

        # ====================================== First Entry - Name =============================#
        self.service_entbx1 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.service_entbx1.grid(row=2, column=2, padx=12, pady=15)

        # ====================================== Second Entry - Type ============================#
        self.service_entbx2 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.service_entbx2.grid(row=3, column=2, padx=12, pady=15)

        # ====================================== Third Entry - Price ============================#
        self.service_entbx3 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.service_entbx3.grid(row=4, column=2, padx=12, pady=15)

        # ====================================== Fourth Entry - Availablity =====================#
        self.service_entbx4 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.service_entbx4.grid(row=5, column=2, padx=12, pady=15)

        # ====================================== Fifth Entry - Prescription ======================#
        self.service_entbx5 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.service_entbx5.grid(row=6, column=2, padx=12, pady=15)

        # ========================================= Combobox for Search ==========================#
        self.service_search_obj = StringVar()
        self.serviceboard_searchbox = ttk.Combobox(self.navigation_frame0, state='readonly',
                                                   textvariable=self.service_search_obj, width=27, height=5)
        self.serviceboard_searchbox['values'] = ["Service_name", "Service_type", "Service_price",
                                                 "Service_availability", "Service_prescription"]
        self.serviceboard_searchbox.grid(row=4, column=0, pady=10)

        # ========================================= EntryBox for Search ==========================#
        self.service_search_value = StringVar()
        self.serviceboard_searchbx10 = Entry(self.navigation_frame0, textvariable=self.service_search_value, bg="white",
                                             fg="black", font=("arial", 12, "bold"))
        self.serviceboard_searchbx10.grid(row=5, column=0, padx=15, pady=10)

        # =================================== ADD Button with picture inserted ====================#
        self.service_addbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\addbutton.png")
        self.service_addbutton = Button(self.navigation_frame, image=self.service_addbutton_img, bg="white", fg="black",
                                        command=self.addservices, font=("arial", 15), height=25, width=95)
        self.service_addbutton.image = self.service_addbutton_img
        self.service_addbutton.grid(row=8, column=1, columnspan=2, padx=10, pady=22)

        # =================================== Show Button with picture inserted ===================#
        self.service_showbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\showbutton.png")
        self.service_showbutton = Button(self.navigation_frame, image=self.service_showbutton_img, bg="white",
                                         fg="black", font=("arial", 15), command=self.showitemintree_servicedata,
                                         height=37, width=140)
        self.service_showbutton.image = self.service_showbutton_img
        self.service_showbutton.grid(row=1, column=1, columnspan=3, padx=334, pady=15)

        # =================================== Update Button with picture inserted =================#
        self.service_updatebutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\updatebutton.png")
        self.service_updatebutton = Button(self.navigation_frame, image=self.service_updatebutton_img, bg="white",
                                           fg="black", font=("arial", 15), command=self.service_updatefrntend,
                                           height=25, width=95)
        self.service_updatebutton.image = self.service_updatebutton_img
        self.service_updatebutton.grid(row=8, column=1, padx=10, pady=22)

        # =================================== Delete Button with picture inserted =================#
        self.service_deletebutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\deletebutton.png")
        self.service_deletebutton = Button(self.navigation_frame, image=self.service_deletebutton_img, bg="white",
                                           fg="black", font=("arial", 15), command=self.deleteservice, height=25,
                                           width=95)
        self.service_deletebutton.image = self.service_deletebutton_img
        self.service_deletebutton.grid(row=8, column=2, padx=10, pady=22)

        # =================================== Search Button with picture inserted =================#
        self.service_searchbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\searchbutton.png")
        self.service_searchbutton = Button(self.navigation_frame0, image=self.service_searchbutton_img,
                                           command=self.servicesearch, bg="white", fg="black", font=("arial", 15),
                                           height=25, width=95)
        self.service_searchbutton.image = self.service_searchbutton_img
        self.service_searchbutton.grid(row=6, column=0, padx=10, pady=10)

        # ====================================== SERVICE TREE =====================================#
        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.service_tree = ttk.Treeview(self.tree_frame, column=("Name", "Type", "Price", "Time", "Prescription"),
                                         yscrollcommand=self.yscroll.set, height=11)
        self.yscroll.config(command=self.service_tree.yview)
        self.service_tree.pack()

        self.service_tree['show'] = 'headings'
        self.service_tree.column('Name', width=155)
        self.service_tree.column('Type', width=158)
        self.service_tree.column('Price', width=160)
        self.service_tree.column('Time', width=160)
        self.service_tree.column('Prescription', width=160)

        self.service_tree.heading('Name', text="Name")
        self.service_tree.heading('Type', text="Type")
        self.service_tree.heading('Price', text="Rate")
        self.service_tree.heading('Time', text="Available Time")
        self.service_tree.heading('Prescription', text="Prescription")

    # ========================================= ADDING SERVICE ===================================#
    def addservices(self):
        ser_name = self.service_entbx1.get()
        ser_type = self.service_entbx2.get()
        ser_price = self.service_entbx3.get()
        ser_availability = self.service_entbx4.get()
        ser_prescription = self.service_entbx5.get()
        if len(ser_name) != 0 and len(ser_type) != 0 and len(ser_price) != 0 and len(ser_availability) != 0 and len(
                ser_prescription) != 0:
            if ser_price.isdigit():
                if self.admin_backend.service_add(ser_name, ser_type, ser_price, ser_availability, ser_prescription):
                    messagebox.showinfo('Success', "Services Added")
                    self.showitemintree_servicedata()
                    self.update_index1 = ""
                else:
                    messagebox.showerror("Error", "Can't add your service.")
            else:
                messagebox.showerror("Error", "Price must be an integer.")
        else:
            messagebox.showerror("Error", "Can't leave any blank spaces.")

    # =================================== SHOWING CONTENT IN SERVICE TREE ========================#
    def showitemintree_servicedata(self):
        self.service_tree.delete(*self.service_tree.get_children())
        reqdata = self.admin_backend.service_backend_showdata()
        for i in reqdata:
            self.service_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
        self.service_tree.bind("<Double-1>", self.service_onitemselect)

    # =================================== SELECTING CONTENT IN TREE ==============================#
    def service_onitemselect(self, event):
        selected_row0 = self.service_tree.selection()[0]
        selected_item0 = self.service_tree.item(selected_row0, 'values')
        self.update_index0 = self.service_tree.item(selected_row0, 'text')

        self.service_entbx1.delete(0, END)
        self.service_entbx1.insert(0, selected_item0[0])
        self.service_entbx2.delete(0, END)
        self.service_entbx2.insert(0, selected_item0[1])
        self.service_entbx3.delete(0, END)
        self.service_entbx3.insert(0, selected_item0[2])
        self.service_entbx4.delete(0, END)
        self.service_entbx4.insert(0, selected_item0[3])
        self.service_entbx5.delete(0, END)
        self.service_entbx5.insert(0, selected_item0[4])

    # =================================== UPDATING CONTENT IN TREE ===============================#
    def service_updatefrntend(self):
        if self.update_index0 == "":
            messagebox.showerror("Error", "Please select a row first")
        else:
            ser_name = self.service_entbx1.get()
            ser_type = self.service_entbx2.get()
            ser_price = self.service_entbx3.get()
            ser_availability = self.service_entbx4.get()
            ser_prescription = self.service_entbx5.get()
            if len(ser_name) != 0 and len(ser_type) != 0 and len(ser_price) != 0 and len(ser_availability) != 0 and len(
                    ser_prescription) != 0:
                if ser_price.isdigit():
                    if self.admin_backend.service_status_update(self.update_index0, ser_name, ser_type, ser_price,
                                                                ser_availability, ser_prescription):
                        messagebox.showinfo('Item', "Item Updated")
                        self.showitemintree_servicedata()
                        self.update_index1 = ""
                    else:
                        messagebox.showerror("Error", 'Can not be updated !!!')
                else:
                    messagebox.showerror("Error", "Price must be an integer.")
            else:
                messagebox.showerror("Error", "Can't leave any blank spaces.")

    # =================================== SEARCHING CONTENT IN DATABASE =========================#
    def servicesearch(self):
        if len(self.service_search_value.get()) != 0 and len(self.service_search_obj.get()) != 0:
            searcheed_data0 = self.admin_backend.return_service_search_data(self.service_search_value.get(),
                                                                            self.service_search_obj.get())
            if len(searcheed_data0) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
                self.service_tree.delete(*self.service_tree.get_children())
            else:
                self.service_tree.delete(*self.service_tree.get_children())
                for i in searcheed_data0:
                    self.service_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
                self.service_tree.bind("<Double-1>", self.service_onitemselect)
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")

    # ================================== Delete Service =========================================#
    def deleteservice(self):
        if self.update_index0 == "":
            messagebox.showerror("Can't delete", "Please select a row first.")
        else:
            if self.admin_backend.delete_services(self.update_index0):
                messagebox.showinfo("Service Deleted", "The service is now deleted.")
                self.showitemintree_servicedata()
            else:
                messagebox.showerror("Can't delete", "Delete Failed")

    # ==================================== Window for MEDICINE Button===========================#
    def medicine(self):
        self.deleteframe()
        self.endphoto()
        self.display_date()
        self.display_time()
        # ==================================== First Seperator =================================#
        self.data0 = 22
        while self.data0 <= 790:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=5)
            self.data0 += 10

        # ==================================== SCEOND Seperator ================================#
        self.data = 22
        while self.data <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=65)
            self.data += 10

        # ==================================== Medicine Logo  ==================================#
        self.medicine_photo = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\medicine_logo.png")
        self.medicine_photo_lable = Label(self.navigation_frame0, image=self.medicine_photo, bg="white")
        self.medicine_photo_lable.image = self.medicine_photo
        self.medicine_photo_lable.grid(row=3, column=0, padx=5)

        # ==================================== FIRST label - NAME ==============================#
        self.medicine_lb1 = Label(self.navigation_frame, text="Name of the Medicine", bg="white",
                                  font=('Arial', 12, 'bold'), fg='Black')
        self.medicine_lb1.grid(row=2, column=1, padx=5, pady=16)

        # ==================================== SECEOND label - TYPE ============================#
        self.medicine_lb2 = Label(self.navigation_frame, text="Type of the Medicine", bg="white",
                                  font=('Arial', 12, 'bold'), fg='Black')
        self.medicine_lb2.grid(row=3, column=1, padx=5, pady=16)

        # ==================================== THIRD label - PRICE ============================#
        self.medicine_lb3 = Label(self.navigation_frame, text="Price of the Medicine", bg="white",
                                  font=('Arial', 12, 'bold'), fg='Black')
        self.medicine_lb3.grid(row=4, column=1, padx=5, pady=16)

        # ==================================== FOURTH label - DOSE ============================#
        self.medicine_lb4 = Label(self.navigation_frame, text="Dose of the Medicine", bg="white",
                                  font=('Arial', 12, 'bold'), fg='Black')
        self.medicine_lb4.grid(row=5, column=1, padx=5, pady=16)

        # ==================================== FIFTH label - COMPANY ==========================#
        self.medicine_lb5 = Label(self.navigation_frame, text="Company of the Medicine", bg="white",
                                  font=('Arial', 12, 'bold'), fg='Black')
        self.medicine_lb5.grid(row=6, column=1, padx=5, pady=16)

        # ==================================== SIXTH label - EXPIRY ===========================#
        self.medicine_lb6 = Label(self.navigation_frame, text="Expiry of the Medicine", bg="white",
                                  font=('Arial', 12, 'bold'), fg='Black')
        self.medicine_lb6.grid(row=7, column=1, padx=5, pady=16)

        # ====================================== FIRST ENTRY - NAME ===========================#
        self.medicine_entbx1 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.medicine_entbx1.grid(row=2, column=2, padx=12, pady=10)

        # ==================================== SCEOND ENTRY - TYPE ============================#
        self.medicine_entbx2 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.medicine_entbx2.grid(row=3, column=2, padx=13, pady=10)

        # ==================================== THIRD ENTRY - PRICE ============================#
        self.medicine_entbx3 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.medicine_entbx3.grid(row=4, column=2, padx=13, pady=10)

        # ==================================== FOURTH ENTRY - DOSE ============================#
        self.medicine_entbx4 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.medicine_entbx4.grid(row=5, column=2, padx=13, pady=10)

        # ==================================== FIFTH ENTRY - COMPANY ===========================#
        self.medicine_entbx5 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.medicine_entbx5.grid(row=6, column=2, padx=13, pady=10)

        # ==================================== SIXTH ENTRY - EXPIRY ============================#
        self.medicine_entbx6 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.medicine_entbx6.grid(row=7, column=2, padx=13, pady=10)

        # ==================================== MEDICINE TREE====================================#
        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.medicine_tree = ttk.Treeview(self.tree_frame,
                                          column=("Name", "Type", "Price", "Dose", "Company", "Expiry Date"),
                                          yscrollcommand=self.yscroll.set, height=11)
        self.yscroll.config(command=self.medicine_tree.yview)
        self.medicine_tree.pack()

        self.medicine_tree['show'] = 'headings'

        self.medicine_tree.column('Name', width=135)
        self.medicine_tree.column('Type', width=135)
        self.medicine_tree.column('Price', width=130)
        self.medicine_tree.column('Dose', width=130)
        self.medicine_tree.column('Company', width=130)
        self.medicine_tree.column('Expiry Date', width=133)

        self.medicine_tree.heading('Name', text="Name")
        self.medicine_tree.heading('Type', text="Type")
        self.medicine_tree.heading('Price', text="Rate")
        self.medicine_tree.heading('Dose', text="Dose")
        self.medicine_tree.heading('Company', text="Company")
        self.medicine_tree.heading('Expiry Date', text="Expiry Date")

        # =================================== ADD Button with picture inserted =================#
        self.medicine_addbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\addbutton.png")
        self.medicine_addbutton = Button(self.navigation_frame, image=self.medicine_addbutton_img,
                                         command=self.addmedicine, bg="white", fg="black", font=("arial", 15),
                                         height=25, width=95)
        self.medicine_addbutton.image = self.medicine_addbutton_img
        self.medicine_addbutton.grid(row=15, column=2, padx=10, pady=14)

        # =================================== SHOW Button with picture inserted ================#
        self.medicine_showbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\showbutton.png")
        self.medicine_showbutton = Button(self.navigation_frame, image=self.medicine_showbutton_img,
                                          command=self.showitemintree_medicinedata, bg="white", fg="black",
                                          font=("arial", 15), height=37, width=145)
        self.medicine_showbutton.image = self.medicine_showbutton_img
        self.medicine_showbutton.grid(row=1, column=1, columnspan=3, padx=331, pady=14)

        # =================================== UPDATE Button with picture inserted ==============#
        self.medicine_updatebutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\updatebutton.png")
        self.medicine_updatebutton = Button(self.navigation_frame, image=self.medicine_updatebutton_img,
                                            command=self.medicine_updatefrntend, bg="white", fg="black",
                                            font=("arial", 15), height=25, width=95)
        self.medicine_updatebutton.image = self.medicine_updatebutton_img
        self.medicine_updatebutton.grid(row=15, column=1, padx=10, pady=14)

        # =================================== DELETE Button with picture inserted ==============#
        self.medicine_deletebutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\deletebutton.png")
        self.medicine_deletebutton = Button(self.navigation_frame, image=self.medicine_deletebutton_img,
                                            command=self.deletemedicine, bg="white", fg="black", font=("arial", 15),
                                            height=25, width=95)
        self.medicine_deletebutton.image = self.medicine_deletebutton_img
        self.medicine_deletebutton.grid(row=15, column=1, columnspan=2, padx=10, pady=14)

        # =================================== SEARCH Button with picture inserted ==============#
        self.medicine_searchbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\searchbutton.png")
        self.medicine_searchbutton = Button(self.navigation_frame0, image=self.medicine_searchbutton_img,
                                            command=self.medicinesearch, bg="white", fg="black", font=("arial", 15),
                                            height=25, width=95)
        self.medicine_searchbutton.image = self.medicine_searchbutton_img
        self.medicine_searchbutton.grid(row=6, column=0, padx=10, pady=10)

        # =================================== SEARCH COMBOBOX VALUE ============================#
        self.medicine_search_obj = StringVar()
        self.medicineboard_searchbox = ttk.Combobox(self.navigation_frame0, state='readonly',
                                                    textvariable=self.medicine_search_obj, width=27, height=5)
        self.medicineboard_searchbox['values'] = ["Medicine_name", "Medicine_type", "Medicine_price", "Medicine_dose",
                                                  "Medicine_company", "Medicine_expiry"]
        self.medicineboard_searchbox.grid(row=4, column=0, pady=10)

        # =================================== SEARCH ENTRYBOX VALUE ============================#
        self.medicine_search_value = StringVar()
        self.medicineboard_searchbx10 = Entry(self.navigation_frame0, textvariable=self.medicine_search_value,
                                              bg="white", fg="black", font=("arial", 12, "bold"))
        self.medicineboard_searchbx10.grid(row=5, column=0, padx=15, pady=10)

        # =================================== THIRD SEPRATOR ===================================#
        self.data1 = 22
        while self.data1 <= 800:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=412)
            self.data1 += 10

    # ====================================== ADDING MEDICINES ==================================#
    def addmedicine(self):
        med_name = self.medicine_entbx1.get()
        med_type = self.medicine_entbx2.get()
        med_price = self.medicine_entbx3.get()
        med_dose = self.medicine_entbx4.get()
        med_company = self.medicine_entbx5.get()
        med_expiry = self.medicine_entbx6.get()
        if len(med_name) != 0 and len(med_type) != 0 and len(med_price) != 0 and len(med_dose) != 0 and len(
                med_company) != 0 and len(med_expiry) != 0:
            if med_price.isdigit():
                if self.admin_backend.medicine_add(med_name, med_type, med_price, med_dose, med_company, med_expiry):
                    messagebox.showinfo('Success', "Medicine Added")
                    self.showitemintree_medicinedata()
                    self.update_index1 = ""
                else:
                    messagebox.showerror("Error", "Can't add your medicine.")
            else:
                messagebox.showerror("Error", "Price must be an integer.")
        else:
            messagebox.showerror("Error", "Can't leave any blank spaces.")

    # =================================== SHOWING DATA IN MEDICINE_TREE =========================#
    def showitemintree_medicinedata(self):
        self.medicine_tree.delete(*self.medicine_tree.get_children())
        reqdata = self.admin_backend.medicine_backend_showdata()
        for i in reqdata:
            self.medicine_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6]))
        self.medicine_tree.bind("<Double-1>", self.medicine_onitemselect)

    # =================================== SELECTING DATA FROM MEDICINE TREE =====================#
    def medicine_onitemselect(self, event):
        selected_row00 = self.medicine_tree.selection()[0]
        selected_item00 = self.medicine_tree.item(selected_row00, 'values')
        self.update_index00 = self.medicine_tree.item(selected_row00, 'text')

        self.medicine_entbx1.delete(0, END)
        self.medicine_entbx1.insert(0, selected_item00[0])
        self.medicine_entbx2.delete(0, END)
        self.medicine_entbx2.insert(0, selected_item00[1])
        self.medicine_entbx3.delete(0, END)
        self.medicine_entbx3.insert(0, selected_item00[2])
        self.medicine_entbx4.delete(0, END)
        self.medicine_entbx4.insert(0, selected_item00[3])
        self.medicine_entbx5.delete(0, END)
        self.medicine_entbx5.insert(0, selected_item00[4])
        self.medicine_entbx6.delete(0, END)
        self.medicine_entbx6.insert(0, selected_item00[5])

    # ========================================== UPDATING MEDICINE DATA =========================#
    def medicine_updatefrntend(self):
        if self.update_index00 == "":
            messagebox.showerror("Error", "Please select a row first")
        else:
            med_name = self.medicine_entbx1.get()
            med_type = self.medicine_entbx2.get()
            med_price = self.medicine_entbx3.get()
            med_dose = self.medicine_entbx4.get()
            med_company = self.medicine_entbx5.get()
            med_expiry = self.medicine_entbx6.get()
            if len(med_name) != 0 and len(med_type) != 0 and len(med_price) != 0 and len(med_dose) != 0 and len(
                    med_company) != 0 and len(med_expiry) != 0:
                if med_price.isdigit():
                    if self.admin_backend.medicine_status_update(self.update_index00, med_name, med_type, med_price,
                                                                 med_dose, med_company, med_expiry):
                        messagebox.showinfo('Item', "Item Updated")
                        self.showitemintree_medicinedata()
                        self.update_index00 = ""
                    else:
                        messagebox.showerror("Error", 'Can not be updated !!!')
                else:
                    messagebox.showerror("Error", "Price must be an integer.")
            else:
                messagebox.showerror("Error", "Can't leave any blank spaces.")

    # ======================================== SEARCHING MEDICINE DATA ==========================#
    def medicinesearch(self):
        if len(self.medicine_search_value.get()) != 0 and len(self.medicine_search_obj.get()) != 0:
            searcheed_data00 = self.admin_backend.return_medicine_search_data(self.medicine_search_value.get(),
                                                                              self.medicine_search_obj.get())
            if len(searcheed_data00) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
                self.medicine_tree.delete(*self.medicine_tree.get_children())
            else:
                self.medicine_tree.delete(*self.medicine_tree.get_children())
                for i in searcheed_data00:
                    self.medicine_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6]))
                self.medicine_tree.bind("<Double-1>", self.medicine_onitemselect)
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")

    # ================================== Delete Medicine ========================================#
    def deletemedicine(self):
        if self.update_index00 == "":
            messagebox.showerror("Can't delete", "Please select a row first.")
        else:
            if self.admin_backend.delete_medicines(self.update_index00):
                messagebox.showinfo("Medicine Deleted", "The medicine is now deleted.")
                self.showitemintree_medicinedata()
            else:
                messagebox.showerror("Can't delete", "Delete Failed")

    # ======================================== DOCTOR BOARD =====================================#
    def doctorboard(self):
        self.deleteframe()
        self.endphoto()
        self.display_date()
        self.display_time()
        # =================================== FIRST SEPERATOR ===================================#
        self.data0 = 22
        while self.data0 <= 790:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=2)
            self.data0 += 10
        # =================================== SECOND SEPERATOR =================================#
        self.data = 22
        while self.data <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=55)
            self.data += 10

        # ==================================== Doctor Logo  ====================================#
        self.doctor_photoo = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\doctor_logoo.png")
        self.doctor_photoo_lable = Label(self.navigation_frame0, image=self.doctor_photoo, bg="white")
        self.doctor_photoo_lable.image = self.doctor_photoo
        self.doctor_photoo_lable.grid(row=3, column=0, padx=5)

        # ==================================== FIRST LABEL - NAME ==============================#
        self.doctorboard_lb1 = Label(self.navigation_frame, text="Name of the doctor", bg="white",
                                     font=('Arial', 12, 'bold'), fg='Black')
        self.doctorboard_lb1.grid(row=2, column=1, padx=10, pady=8)

        # ==================================== SCEOND LABEL - AGE ==============================#
        self.doctorboard_lb2 = Label(self.navigation_frame, text="Age of the doctor", bg="white",
                                     font=('Arial', 12, 'bold'), fg='Black')
        self.doctorboard_lb2.grid(row=3, column=1, padx=10, pady=8)

        # ==================================== THIRD LABEL - GENDER ============================#
        self.doctorboard_lb3 = Label(self.navigation_frame, text="Gender of the doctor", bg="white",
                                     font=('Arial', 12, 'bold'), fg='Black')
        self.doctorboard_lb3.grid(row=4, column=1, padx=10, pady=8)

        # ==================================== FOURTH LABEL - ADDRESS ==========================#
        self.doctorboard_lb4 = Label(self.navigation_frame, text="Address of the doctor", bg="white",
                                     font=('Arial', 12, 'bold'), fg='Black')
        self.doctorboard_lb4.grid(row=5, column=1, padx=10, pady=8)

        # ==================================== FIFTH LABEL - QUALIFICATION =====================#
        self.doctorboard_lb5 = Label(self.navigation_frame, text="Qualification of the doctor", bg="white",
                                     font=('Arial', 12, 'bold'), fg='Black')
        self.doctorboard_lb5.grid(row=6, column=1, padx=10, pady=6)

        # ==================================== SIXTH LABEL - UNIVERSITY ========================#
        self.doctorboard_lb6 = Label(self.navigation_frame, text="University of the doctor", bg="white",
                                     font=('Arial', 12, 'bold'), fg='Black')
        self.doctorboard_lb6.grid(row=7, column=1, padx=10, pady=8)

        # ==================================== SEVENTH LABEL - SPECIALITY ======================#
        self.doctorboard_lb7 = Label(self.navigation_frame, text="Speciality of the doctor", bg="white",
                                     font=('Arial', 12, 'bold'), fg='Black')
        self.doctorboard_lb7.grid(row=8, column=1, padx=10, pady=8)

        # ==================================== EIGHTH LABEL - EMAIL ============================#
        self.doctorboard_lb8 = Label(self.navigation_frame, text="Email of the doctor", bg="white",
                                     font=('Arial', 12, 'bold'), fg='Black')
        self.doctorboard_lb8.grid(row=9, column=1, padx=10, pady=5)

        # ==================================== NINTH LABEL - ADMIN APPROVAL ====================#
        self.doctorboard_lb9 = Label(self.navigation_frame, text="Admin Approval", bg="white",
                                     font=('Arial', 12, 'bold'), fg='Black')
        self.doctorboard_lb9.grid(row=10, column=1, padx=10, pady=6)

        # ==================================== FIRST ENTRY - NAME ==============================#
        self.doctorboard_entbx1 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.doctorboard_entbx1.grid(row=2, column=2, padx=10, pady=5)

        # ==================================== SCEOND ENTRY - AGE ==============================#
        self.doctorboard_entbx2 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.doctorboard_entbx2.grid(row=3, column=2, padx=10, pady=5)

        # ==================================== THIRD ENTRY - GENDER ============================#
        self.doctorboard_entbx3 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.doctorboard_entbx3.grid(row=4, column=2, padx=10, pady=5)

        # ==================================== FOURTH ENTRY - ADDRESS ==========================#
        self.doctorboard_entbx4 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.doctorboard_entbx4.grid(row=5, column=2, padx=10, pady=5)

        # ==================================== FIFTH ENTRY - QUALIFICATION =====================#
        self.doctorboard_entbx5 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.doctorboard_entbx5.grid(row=6, column=2, padx=10, pady=5)

        # ==================================== SIXTH ENTRY - UNIVERSITY ========================#
        self.doctorboard_entbx6 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.doctorboard_entbx6.grid(row=7, column=2, padx=10, pady=5)

        # ==================================== SEVENTH ENTRY - SPECIALITY ======================#
        self.doctorboard_entbx7 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.doctorboard_entbx7.grid(row=8, column=2, padx=10, pady=5)

        # ==================================== EIGHTH ENTRY - EMAIL ============================#
        self.doctorboard_entbx8 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.doctorboard_entbx8.grid(row=9, column=2, padx=10, pady=5)

        # ==================================== ADMIN APPROVAL_COMBOBOX =========================#
        self.doctorboard_entbx9 = ttk.Combobox(self.navigation_frame, width=33, height=2)
        self.doctorboard_entbx9.grid(row=10, column=2)
        self.doctorboard_entbx9['values'] = ["Yes", "No"]

        # =================================== DOCTOR SEARCH COMBOBOX VALUE =====================#
        self.doctor_search_obj = StringVar()
        self.doctorboard_searchbox = ttk.Combobox(self.navigation_frame0, state='readonly',
                                                  textvariable=self.doctor_search_obj, width=27, height=5)
        self.doctorboard_searchbox['values'] = ["Doctor_Name", "Doctor_Age", "Doctor_Gender", "Doctor_Address",
                                                "Doctor_Qualification", "Doctor_University", "Doctor_Speciality",
                                                "Doctor_Email", "Admin_Approval"]
        self.doctorboard_searchbox.grid(row=4, column=0, pady=10)

        # =================================== DOCTOR SEARCH VALUE =============================#
        self.doctor_search_value = StringVar()
        self.doctorboard_searchbx10 = Entry(self.navigation_frame0, textvariable=self.doctor_search_value, bg="white",
                                            fg="black", font=("arial", 12, "bold"))
        self.doctorboard_searchbx10.grid(row=5, column=0, pady=10)

        # =================================== DOCTOR TREE ====================================#
        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.doctorboard_tree = ttk.Treeview(self.tree_frame, column=(
        "Name", "Age", "Gender", "Address", "Qualification", "University", "Speciality", "Email", "Admin Approval"),
                                             yscrollcommand=self.yscroll.set, height=11)
        self.yscroll.config(command=self.doctorboard_tree.yview)
        self.doctorboard_tree.pack()
        self.doctorboard_tree['show'] = 'headings'

        self.doctorboard_tree.column('Name', width=120)
        self.doctorboard_tree.column('Age', width=55)
        self.doctorboard_tree.column('Gender', width=50)
        self.doctorboard_tree.column('Address', width=70)
        self.doctorboard_tree.column('Qualification', width=90)
        self.doctorboard_tree.column('University', width=90)
        self.doctorboard_tree.column('Speciality', width=90)
        self.doctorboard_tree.column('Email', width=120)
        self.doctorboard_tree.column('Admin Approval', width=110)

        self.doctorboard_tree.heading('Name', text="Name")
        self.doctorboard_tree.heading('Age', text="Age")
        self.doctorboard_tree.heading('Address', text="Address")
        self.doctorboard_tree.heading('Gender', text="Gender")
        self.doctorboard_tree.heading('Qualification', text="Qualification")
        self.doctorboard_tree.heading('University', text="University")
        self.doctorboard_tree.heading('Speciality', text="Speciality")
        self.doctorboard_tree.heading('Email', text="Email")
        self.doctorboard_tree.heading('Admin Approval', text="Admin Approval")

        # =================================== SHOW Button with picture inserted ======================================#
        self.doctorboard_showbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\showbutton.png")
        self.doctorboard_showbutton = Button(self.navigation_frame, image=self.doctorboard_showbutton_img,
                                             command=self.showitemintree_doctordata, bg="white", fg="black",
                                             font=("arial", 15), height=40, width=120)
        self.doctorboard_showbutton.image = self.doctorboard_showbutton_img
        self.doctorboard_showbutton.grid(row=1, column=1, columnspan=3, padx=344, pady=5)

        # =================================== UPDATE Button with picture inserted ====================================#
        self.doctorboard_updatebutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\updatebutton.png")
        self.doctorboard_updatebutton = Button(self.navigation_frame, image=self.doctorboard_updatebutton_img,
                                               command=self.doctor_status_updatefrntend, bg="white", fg="black",
                                               font=("arial", 15), height=25, width=95)
        self.doctorboard_updatebutton.image = self.doctorboard_updatebutton_img
        self.doctorboard_updatebutton.grid(row=15, column=2, padx=10, pady=12)

        # =================================== DELETE Button with picture inserted ====================================#
        self.doctorboard_deletebutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\deletebutton.png")
        self.doctorboard_deletebutton = Button(self.navigation_frame, image=self.doctorboard_deletebutton_img,
                                               command=self.deletedoctors, bg="white", fg="black", font=("arial", 15),
                                               height=25, width=95)
        self.doctorboard_deletebutton.image = self.doctorboard_deletebutton_img
        self.doctorboard_deletebutton.grid(row=15, column=1, padx=10, pady=12)

        # =================================== SEARCH Button with picture inserted ====================================#
        self.doctorboard_searchbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\searchbutton.png")
        self.doctorboard_searchbutton = Button(self.navigation_frame0, image=self.doctorboard_searchbutton_img,
                                               command=self.doctorsearch, bg="white", fg="black", font=("arial", 15),
                                               height=25, width=95)
        self.doctorboard_searchbutton.image = self.doctorboard_searchbutton_img
        self.doctorboard_searchbutton.grid(row=6, column=0, pady=10)

        # =================================== THIRD SEPERATOR ============================================#
        self.data1 = 22
        while self.data1 <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=420)
            self.data1 += 10

    # =================================== SHOWING DOCTOR DATA IN TREE ===================================#
    def showitemintree_doctordata(self):
        self.doctorboard_tree.delete(*self.doctorboard_tree.get_children())
        reqdata = self.admin_backend.doctor_backend_showdata()
        for i in reqdata:
            self.doctorboard_tree.insert("", "end", text=i[0],
                                         value=(i[1], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]))
        self.doctorboard_tree.bind("<Double-1>", self.doctordata_onitemselect)

    # =================================== SELECTING VALUE IN DOCTOR TREE ================================#
    def doctordata_onitemselect(self, event):
        selected_row = self.doctorboard_tree.selection()[0]
        selected_item = self.doctorboard_tree.item(selected_row, 'values')
        self.update_index = self.doctorboard_tree.item(selected_row, 'text')

        self.doctorboard_entbx1.delete(0, END)
        self.doctorboard_entbx1.insert(0, selected_item[0])
        self.doctorboard_entbx2.delete(0, END)
        self.doctorboard_entbx2.insert(0, selected_item[1])
        self.doctorboard_entbx3.delete(0, END)
        self.doctorboard_entbx3.insert(0, selected_item[2])
        self.doctorboard_entbx4.delete(0, END)
        self.doctorboard_entbx4.insert(0, selected_item[3])
        self.doctorboard_entbx5.delete(0, END)
        self.doctorboard_entbx5.insert(0, selected_item[4])
        self.doctorboard_entbx6.delete(0, END)
        self.doctorboard_entbx6.insert(0, selected_item[5])
        self.doctorboard_entbx7.delete(0, END)
        self.doctorboard_entbx7.insert(0, selected_item[6])
        self.doctorboard_entbx8.delete(0, END)
        self.doctorboard_entbx8.insert(0, selected_item[7])

    # =================================== UPDATING DOCTOR DATA ==========================================#
    def doctor_status_updatefrntend(self):
        if self.update_index == "":
            messagebox.showerror("Error", "Please select a row first")
        else:
            name = self.doctorboard_entbx1.get()
            age = self.doctorboard_entbx2.get()
            gender = self.doctorboard_entbx3.get()
            address = self.doctorboard_entbx4.get()
            passedfrom = self.doctorboard_entbx5.get()
            speciality = self.doctorboard_entbx6.get()
            qualification = self.doctorboard_entbx7.get()
            email = self.doctorboard_entbx8.get()
            admin_approval = self.doctorboard_entbx9.get()

            if len(name) != 0 and len(age) != 0 and len(gender) != 0 and len(address) != 0 and len(
                    passedfrom) != 0 and len(speciality) != 0 and len(qualification) != 0 and len(email) != 0 and len(
                    admin_approval) != 0:
                if age.isdigit():
                    if self.admin_backend.doctor_status_update(self.update_index, name, age, gender, address,
                                                               passedfrom, speciality, qualification, email,
                                                               admin_approval):
                        messagebox.showinfo('Item', "Item Updated")
                        self.showitemintree_doctordata()
                        self.update_index = ""
                    else:
                        messagebox.showerror("Error", 'Can not be updated !!!')
                else:
                    messagebox.showerror("Error", "Age must be an integer.")
            else:
                messagebox.showerror("Error", "You can't leave any blank spaces")

    # =================================== SEARCH DOCTOR DATA ============================================#
    def doctorsearch(self):
        if len(self.doctor_search_value.get()) != 0 and len(self.doctor_search_obj.get()) != 0:
            searcheed_data = self.admin_backend.return_doctor_search_data(self.doctor_search_value.get(),
                                                                          self.doctor_search_obj.get())
            if len(searcheed_data) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
                self.doctorboard_tree.delete(*self.doctorboard_tree.get_children())
            else:
                self.doctorboard_tree.delete(*self.doctorboard_tree.get_children())
                for i in searcheed_data:
                    self.doctorboard_tree.insert("", "end", text=i[0],
                                                 value=(i[1], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]))
                self.doctorboard_tree.bind("<Double-1>", self.doctordata_onitemselect)
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")

    # ======================================= Delete Doctors ============================================#
    def deletedoctors(self):
        if self.update_index == "":
            messagebox.showerror("Can't delete", "Please select a row first.")
        else:
            if self.admin_backend.delete_doctors(self.update_index):
                messagebox.showinfo("Doctor Data Deleted", "The desired data is now deleted.")
                self.showitemintree_doctordata()
            else:
                messagebox.showerror("Can't delete", "Delete Failed")

    # ======================================== STAFF BOARD ======================================#
    def staffboard(self):
        self.deleteframe()
        self.endphoto()
        self.display_date()
        self.display_time()
        # =================================== FIRST SEPERATOR ===================================#
        self.data0 = 22
        while self.data0 <= 790:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=5)
            self.data0 += 10
        # =================================== SECOND SEPERATOR ==================================#
        self.data = 22
        while self.data <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=65)
            self.data += 10

        # ==================================== StaffLogo  ======================================#
        self.staff_photo = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\staff_logoo.png")
        self.staff_photo_lable = Label(self.navigation_frame0, image=self.staff_photo, bg="white")
        self.staff_photo_lable.image = self.staff_photo
        self.staff_photo_lable.grid(row=3, column=0, padx=5)
        # ==================================== FIRST LABEL - NAME ==============================#
        self.staffboard_lb1 = Label(self.navigation_frame, text="Name of the staff", bg="white",
                                    font=('Arial', 12, 'bold'), fg='Black')
        self.staffboard_lb1.grid(row=2, column=1, padx=10, pady=9)

        # ==================================== SCEOND LABEL - AGE =============================#
        self.staffboard_lb2 = Label(self.navigation_frame, text="Age of the staff", bg="white",
                                    font=('Arial', 12, 'bold'), fg='Black')
        self.staffboard_lb2.grid(row=3, column=1, padx=10, pady=9)

        # ==================================== THIRD LABEL - GENDER ===========================#
        self.staffboard_lb3 = Label(self.navigation_frame, text="Gender of the staff", bg="white",
                                    font=('Arial', 12, 'bold'), fg='Black')
        self.staffboard_lb3.grid(row=4, column=1, padx=10, pady=9)

        # ==================================== FOURTH LABEL - ADDRESS =========================#
        self.staffboard_lb4 = Label(self.navigation_frame, text="Address of the staff", bg="white",
                                    font=('Arial', 12, 'bold'), fg='Black')
        self.staffboard_lb4.grid(row=5, column=1, padx=10, pady=9)

        # ==================================== FIFTH LABEL - QUALIFICATION ====================#
        self.staffboard_lb5 = Label(self.navigation_frame, text="Qualification of the staff", bg="white",
                                    font=('Arial', 12, 'bold'), fg='Black')
        self.staffboard_lb5.grid(row=6, column=1, padx=10, pady=9)

        # ==================================== SIXTH LABEL - UNIVERSITY =======================#
        self.staffboard_lb6 = Label(self.navigation_frame, text="University of the staff", bg="white",
                                    font=('Arial', 12, 'bold'), fg='Black')
        self.staffboard_lb6.grid(row=7, column=1, padx=10, pady=9)

        # ==================================== SEVENTH LABEL - EMAIL ==========================#
        self.staffboard_lb7 = Label(self.navigation_frame, text="Email of the staff", bg="white",
                                    font=('Arial', 12, 'bold'), fg='Black')
        self.staffboard_lb7.grid(row=8, column=1, padx=10, pady=9)

        # ==================================== EIGHTH LABEL - ADMIN ===========================#
        self.staffboard_lb8 = Label(self.navigation_frame, text="Admin Approval", bg="white",
                                    font=('Arial', 12, 'bold'), fg='Black')
        self.staffboard_lb8.grid(row=9, column=1, padx=10, pady=9)

        # ==================================== FIRST ENTRY - NAME =============================#
        self.staffboard_entbx1 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.staffboard_entbx1.grid(row=2, column=2, padx=10, pady=5)

        # ==================================== SECEOND ENTRY - AGE ============================#
        self.staffboard_entbx2 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.staffboard_entbx2.grid(row=3, column=2, padx=10, pady=5)

        # ==================================== THIRD ENTRY - GENDER ===========================#
        self.staffboard_entbx3 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.staffboard_entbx3.grid(row=4, column=2, padx=10, pady=5)

        # ==================================== FOURTH ENTRY - ADDRESS =========================#
        self.staffboard_entbx4 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.staffboard_entbx4.grid(row=5, column=2, padx=10, pady=5)

        # ==================================== FIFTH ENTRY - QUALIFICATION ====================#
        self.staffboard_entbx5 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.staffboard_entbx5.grid(row=6, column=2, padx=10, pady=5)

        # ==================================== SIXTH ENTRY - UNIVERSITY =======================#
        self.staffboard_entbx6 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.staffboard_entbx6.grid(row=7, column=2, padx=10, pady=5)

        # ==================================== SEVENTH ENTRY - EMAIL ==========================#
        self.staffboard_entbx7 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.staffboard_entbx7.grid(row=8, column=2, padx=10, pady=5)

        # ==================================== EIGHTH ENTRY - ADMIN ===========================#
        self.staffboard_entbx8 = ttk.Combobox(self.navigation_frame, width=33, height=2)
        self.staffboard_entbx8.grid(row=9, column=2)
        self.staffboard_entbx8['values'] = ["Yes", "No"]

        # =================================== STAFF TREE VIEW =================================#

        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.staffboard_tree = ttk.Treeview(self.tree_frame, column=(
        "Name", "Age", "Gender", "Address", "Qualification", "University", "Email", "Admin Approval"),
                                            yscrollcommand=self.yscroll.set, height=11)
        self.yscroll.config(command=self.staffboard_tree.yview)
        self.staffboard_tree.pack()
        self.staffboard_tree['show'] = 'headings'

        self.staffboard_tree.column('Name', width=120)
        self.staffboard_tree.column('Age', width=70)
        self.staffboard_tree.column('Gender', width=70)
        self.staffboard_tree.column('Address', width=100)
        self.staffboard_tree.column('Qualification', width=100)
        self.staffboard_tree.column('University', width=100)
        self.staffboard_tree.column('Email', width=123)
        self.staffboard_tree.column('Admin Approval', width=110)

        self.staffboard_tree.heading('Name', text="Name")
        self.staffboard_tree.heading('Age', text="Age")
        self.staffboard_tree.heading('Address', text="Address")
        self.staffboard_tree.heading('Gender', text="Gender")
        self.staffboard_tree.heading('Qualification', text="Qualification")
        self.staffboard_tree.heading('University', text="University")
        self.staffboard_tree.heading('Email', text="Email")
        self.staffboard_tree.heading('Admin Approval', text="Admin Approval")

        # =================================== SHOW Button with picture inserted =====================================#
        self.staffboard_showbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\showbutton.png")
        self.staffboard_showbutton = Button(self.navigation_frame, image=self.staffboard_showbutton_img,
                                            command=self.showitemintree_staffdata, bg="white", fg="black",
                                            font=("arial", 15), height=40, width=120)
        self.staffboard_showbutton.image = self.staffboard_showbutton_img
        self.staffboard_showbutton.grid(row=1, column=1, columnspan=3, padx=344, pady=10)

        # =================================== UPDATE Button with picture inserted ===================================#
        self.staffboard_updatebutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\updatebutton.png")
        self.staffboard_updatebutton = Button(self.navigation_frame, image=self.staffboard_updatebutton_img,
                                              command=self.staff_status_updatefrntend, bg="white", fg="black",
                                              font=("arial", 15), height=25, width=95)
        self.staffboard_updatebutton.image = self.staffboard_updatebutton_img
        self.staffboard_updatebutton.grid(row=15, column=2, padx=10, pady=15)

        # =================================== DELETE Button with picture inserted ===================================#
        self.staffboard_deletebutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\deletebutton.png")
        self.staffboard_deletebutton = Button(self.navigation_frame, image=self.staffboard_deletebutton_img,
                                              command=self.deletestaffs, bg="white", fg="black", font=("arial", 15),
                                              height=25, width=95)
        self.staffboard_deletebutton.image = self.staffboard_deletebutton_img
        self.staffboard_deletebutton.grid(row=15, column=1, padx=10, pady=15)

        # =================================== SEARCH Button with picture inserted ===================================#
        self.staffboard_searchbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\searchbutton.png")
        self.staffboard_searchbutton = Button(self.navigation_frame0, image=self.staffboard_searchbutton_img,
                                              command=self.staffsearch, bg="white", fg="black", font=("arial", 15),
                                              height=25, width=95)
        self.staffboard_searchbutton.image = self.staffboard_searchbutton_img
        self.staffboard_searchbutton.grid(row=6, column=0, padx=10, pady=10)

        # =================================== STAFF SEARCH COMBOBOX VALUE ===================================#
        self.staff_search_obj = StringVar()
        self.staffboard_searchbox = ttk.Combobox(self.navigation_frame0, state='readonly',
                                                 textvariable=self.staff_search_obj, width=27, height=5)
        self.staffboard_searchbox['values'] = ["Staff_Name", "Staff_Age", "Staff_Gender", "Staff_Address",
                                               "Staff_Qualification", "Staff_University", "Staff_Email",
                                               "Admin_approval"]
        self.staffboard_searchbox.grid(row=4, column=0, pady=10)

        # =================================== STAFF SEARCH VALUE ===========================================#
        self.staff_search_value = StringVar()
        self.staffboard_searchbx10 = Entry(self.navigation_frame0, textvariable=self.staff_search_value, bg="white",
                                           fg="black", font=("arial", 12, "bold"))
        self.staffboard_searchbx10.grid(row=5, column=0, padx=15, pady=10)

        # =================================== THIRD SEPERATOR ===============================================#
        self.data1 = 22
        while self.data1 <= 800:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=410)
            self.data1 += 10

    # =================================== SHOWING STAFF DATA IN TREE =======================================#
    def showitemintree_staffdata(self):
        self.staffboard_tree.delete(*self.staffboard_tree.get_children())
        reqdata = self.admin_backend.staff_backend_showdata()
        for i in reqdata:
            self.staffboard_tree.insert("", "end", text=i[0], value=(i[1], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
        self.staffboard_tree.bind("<Double-1>", self.staffdata_onitemselect)

    # =================================== SELECTING STAFF DATA IN TREE =====================================#
    def staffdata_onitemselect(self, event):
        selected_row1 = self.staffboard_tree.selection()[0]
        selected_item1 = self.staffboard_tree.item(selected_row1, 'values')
        self.update_index0 = self.staffboard_tree.item(selected_row1, 'text')

        self.staffboard_entbx1.delete(0, END)
        self.staffboard_entbx1.insert(0, selected_item1[0])
        self.staffboard_entbx2.delete(0, END)
        self.staffboard_entbx2.insert(0, selected_item1[1])
        self.staffboard_entbx3.delete(0, END)
        self.staffboard_entbx3.insert(0, selected_item1[2])
        self.staffboard_entbx4.delete(0, END)
        self.staffboard_entbx4.insert(0, selected_item1[3])
        self.staffboard_entbx5.delete(0, END)
        self.staffboard_entbx5.insert(0, selected_item1[4])
        self.staffboard_entbx6.delete(0, END)
        self.staffboard_entbx6.insert(0, selected_item1[5])
        self.staffboard_entbx7.delete(0, END)
        self.staffboard_entbx7.insert(0, selected_item1[6])

    # =============================================== UPDATING STAFF DATA IN TREE ===================================#
    def staff_status_updatefrntend(self):
        if self.update_index0 == "":
            messagebox.showerror("Error", "Please select a row first")
        else:
            name = self.staffboard_entbx1.get()
            age = self.staffboard_entbx2.get()
            gender = self.staffboard_entbx3.get()
            address = self.staffboard_entbx4.get()
            passedfrom = self.staffboard_entbx5.get()
            qualification = self.staffboard_entbx6.get()
            email = self.staffboard_entbx7.get()
            admin_approval = self.staffboard_entbx8.get()

            if len(name) != 0 and len(age) != 0 and len(gender) != 0 and len(address) != 0 and len(
                    passedfrom) != 0 and len(qualification) != 0 and len(email) != 0 and len(admin_approval) != 0:
                if age.isdigit():
                    if self.admin_backend.staff_status_update(self.update_index0, name, age, gender, address,
                                                              passedfrom, qualification, email, admin_approval):
                        messagebox.showinfo('Item', "Item Updated")
                        self.showitemintree_staffdata()
                        self.update_index0 = ""
                    else:
                        messagebox.showerror("Error", 'Can not be updated !!!')
                else:
                    messagebox.showerror("Error", "Age must be an integer.")
            else:
                messagebox.showerror("Error", "Can't leave any blank spaces.")

    # =========================================== SEARCHING STAFF DATA IN TREE ======================================#
    def staffsearch(self):
        if len(self.staff_search_value.get()) != 0 and len(self.staff_search_obj.get()) != 0:
            searcheed_data02 = self.admin_backend.return_staff_search_data(self.staff_search_value.get(),
                                                                           self.staff_search_obj.get())
            if len(searcheed_data02) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
                self.staffboard_tree.delete(*self.staffboard_tree.get_children())
            else:
                self.staffboard_tree.delete(*self.staffboard_tree.get_children())
                for i in searcheed_data02:
                    self.staffboard_tree.insert("", "end", text=i[0],
                                                value=(i[1], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
                self.staffboard_tree.bind("<Double-1>", self.staffdata_onitemselect)
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")

    # ================================================ Delete Staffs ================================================#
    def deletestaffs(self):
        if self.update_index0 == "":
            messagebox.showerror("Can't delete", "Please select a row first.")
        else:
            if self.admin_backend.delete_staffs(self.update_index0):
                messagebox.showinfo("Staff Data Deleted", "The desired data is now deleted.")
                self.showitemintree_staffdata()
            else:
                messagebox.showerror("Can't delete", "Delete Failed")

    # ==================================================== PATIENT ==================================================#
    def patientboard(self):
        self.deleteframe()
        self.endphoto()
        self.display_date()
        self.display_time()
        # ============================================= FIRST SEPERATOR =============================================#
        self.data0 = 22
        while self.data0 <= 790:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=9)
            self.data0 += 10
        # ============================================= SECOND SEPERATOR ============================================#
        self.data = 22
        while self.data <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=70)
            self.data += 10

        # ================================================ Patient Logo  ============================================#
        self.patient_photoo = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\patientboard.png")
        self.patient_photoo_lable = Label(self.navigation_frame0, image=self.patient_photoo, bg="white")
        self.patient_photoo_lable.image = self.patient_photoo
        self.patient_photoo_lable.grid(row=3, column=0, padx=5)

        # ========================================== FIRST LABEL - NAME =============================================#
        self.patientboard_lb1 = Label(self.navigation_frame, text="Name of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb1.grid(row=2, column=1, padx=10, pady=10)

        # ========================================== SCEOND LABEL - AGE =============================================#
        self.patientboard_lb2 = Label(self.navigation_frame, text="Age of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb2.grid(row=3, column=1, padx=10, pady=10)

        # ========================================== THIRD LABEL - GENDER ===========================================#
        self.patientboard_lb3 = Label(self.navigation_frame, text="Gender of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb3.grid(row=4, column=1, padx=10, pady=10)

        # ========================================== FOURTH LABEL - Weight ==========================================#
        self.patientboard_lb4 = Label(self.navigation_frame, text="Weight of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb4.grid(row=5, column=1, padx=10, pady=10)

        # ========================================== FIFTH LABEL - Height ===========================================#
        self.patientboard_lb5 = Label(self.navigation_frame, text="Height of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb5.grid(row=6, column=1, padx=10, pady=10)

        # ========================================== SIXTH LABEL - Address ==========================================#
        self.patientboard_lb6 = Label(self.navigation_frame, text="Address of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb6.grid(row=7, column=1, padx=10, pady=10)

        # ========================================== Seventh LABEL - Contact ========================================#
        self.patientboard_lb8 = Label(self.navigation_frame, text="Contact number of the patient", bg="white",
                                      font=('Arial', 12, 'bold'), fg='Black')
        self.patientboard_lb8.grid(row=8, column=1, padx=10, pady=10)

        # ========================================== FIRST ENTRY - NAME =============================================#
        self.patientboard_entbx1 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx1.grid(row=2, column=2, padx=10, pady=10)

        # ========================================== SCEOND ENTRY - AGE =============================================#
        self.patientboard_entbx2 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx2.grid(row=3, column=2, padx=10, pady=10)

        # ========================================== THIRD ENTRY - GENDER ===========================================#
        self.patientboard_entbx3 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx3.grid(row=4, column=2, padx=10, pady=10)

        # ========================================== FOURTH ENTRY - WEIGHT ==========================================#
        self.patientboard_entbx4 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx4.grid(row=5, column=2, padx=10, pady=10)

        # ========================================= FIFTH ENTRY - HEIGHT ============================================#
        self.patientboard_entbx5 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx5.grid(row=6, column=2, padx=10, pady=10)

        # ========================================== SIXTH ENTRY - ADDERESS =========================================#
        self.patientboard_entbx6 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx6.grid(row=7, column=2, padx=10, pady=10)

        # ====================================== SEVENTH ENTRY - CONTACT NUMBER =====================================#
        self.patientboard_entbx7 = Entry(self.navigation_frame, bg="white", fg="black", font=("arial", 15, "bold"))
        self.patientboard_entbx7.grid(row=8, column=2, padx=10, pady=10)

        # ========================================= Patient SEARCH COMBOBOX VALUE ===================================#
        self.patient_search_obj = StringVar()
        self.patientboard_searchbox = ttk.Combobox(self.navigation_frame0, state='readonly',
                                                   textvariable=self.patient_search_obj, width=27, height=5)
        self.patientboard_searchbox['values'] = ["Patient_Name", "Patient_Age", "Patient_Gender", "Patient_Weight",
                                                 "Patient_Height", "Patient_Address", "Patient_Contact"]
        self.patientboard_searchbox.grid(row=4, column=0, pady=10)

        # ========================================= Patient SEARCH VALUE ============================================#
        self.patient_search_value = StringVar()
        self.patientboard_searchbx10 = Entry(self.navigation_frame0, textvariable=self.patient_search_value, bg="white",
                                             fg="black", font=("arial", 12, "bold"))
        self.patientboard_searchbx10.grid(row=5, column=0, pady=10)

        # ============================================= Patient TREE ================================================#
        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.patientboard_tree = ttk.Treeview(self.tree_frame, column=(
        "Name", "Age", "Gender", "Weight", "Height", "Address", "Contact Number"), yscrollcommand=self.yscroll.set,
                                              height=11)
        self.yscroll.config(command=self.patientboard_tree.yview)
        self.patientboard_tree.pack()
        self.patientboard_tree['show'] = 'headings'

        self.patientboard_tree.column('Name', width=130, anchor="center")
        self.patientboard_tree.column('Age', width=100, anchor="center")
        self.patientboard_tree.column('Gender', width=100, anchor="center")
        self.patientboard_tree.column('Weight', width=100, anchor="center")
        self.patientboard_tree.column('Height', width=100, anchor="center")
        self.patientboard_tree.column('Address', width=130, anchor="center")
        self.patientboard_tree.column('Contact Number', width=133, anchor="center")

        self.patientboard_tree.heading('Name', text="Name")
        self.patientboard_tree.heading('Age', text="Age")
        self.patientboard_tree.heading('Gender', text="Gender")
        self.patientboard_tree.heading('Weight', text="Weight")
        self.patientboard_tree.heading('Height', text="Height")
        self.patientboard_tree.heading('Address', text="Address")
        self.patientboard_tree.heading('Contact Number', text="Contact Number")

        # ==================================== SHOW Button with picture inserted ====================================#
        self.patientboard_showbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\showbutton.png")
        self.patientboard_showbutton = Button(self.navigation_frame, image=self.patientboard_showbutton_img, bg="white",
                                              fg="black", font=("arial", 15), command=self.showitemintree_patientdata,
                                              height=40, width=120)
        self.patientboard_showbutton.image = self.patientboard_showbutton_img
        self.patientboard_showbutton.grid(row=1, column=1, columnspan=3, padx=344, pady=15)

        # =================================== UPDATE Button with picture inserted ===================================#
        self.patientboard_updatebutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\updatebutton.png")
        self.patientboard_updatebutton = Button(self.navigation_frame, image=self.patientboard_updatebutton_img,
                                                bg="white", fg="black", font=("arial", 15),
                                                command=self.patient_updatefrntend, height=25, width=95)
        self.patientboard_updatebutton.image = self.patientboard_updatebutton_img
        self.patientboard_updatebutton.grid(row=15, column=2, padx=10, pady=15)

        # =================================== DELETE Button with picture inserted ===================================#
        self.patientboard_deletebutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\deletebutton.png")
        self.patientboard_deletebutton = Button(self.navigation_frame, image=self.patientboard_deletebutton_img,
                                                command=self.deletepatients, bg="white", fg="black", font=("arial", 15),
                                                height=25, width=95)
        self.patientboard_deletebutton.image = self.patientboard_deletebutton_img
        self.patientboard_deletebutton.grid(row=15, column=1, padx=10, pady=15)

        # =================================== SEARCH Button with picture inserted ===================================#
        self.patientboard_searchbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\searchbutton.png")
        self.patientboard_searchbutton = Button(self.navigation_frame0, image=self.patientboard_searchbutton_img,
                                                bg="white", fg="black", font=("arial", 15), command=self.patientsearch,
                                                height=25, width=95)
        self.patientboard_searchbutton.image = self.patientboard_searchbutton_img
        self.patientboard_searchbutton.grid(row=6, column=0, pady=15)

        # ============================================== THIRD SEPERATOR ============================================#
        self.data1 = 22
        while self.data1 <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=415)
            self.data1 += 10

    # ======================================== SHOWING CONTENT IN Patient TREE ======================================#
    def showitemintree_patientdata(self):
        self.patientboard_tree.delete(*self.patientboard_tree.get_children())
        reqdata = self.admin_backend.patient_backend_showdata()
        for i in reqdata:
            self.patientboard_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
        self.patientboard_tree.bind("<Double-1>", self.patient_onitemselect)

    # ========================================= SELECTING CONTENT IN TREE ========================================#
    def patient_onitemselect(self, event):
        selected_row0 = self.patientboard_tree.selection()[0]
        selected_item0 = self.patientboard_tree.item(selected_row0, 'values')
        self.update_index0 = self.patientboard_tree.item(selected_row0, 'text')

        self.patientboard_entbx1.delete(0, END)
        self.patientboard_entbx1.insert(0, selected_item0[0])
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

    # ========================================== UPDATING CONTENT IN TREE ===================================#
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
            if len(pat_name) != 0 and len(pat_age) != 0 and len(pat_gender) != 0 and len(pat_weight) != 0 and len(
                    pat_height) != 0 and len(pat_address) != 0 and len(pat_contact) != 0:
                if pat_age.isdigit():
                    if pat_weight.isdigit():
                        if pat_contact.isdigit():
                            if self.admin_backend.patient_status_update(self.update_index0, pat_name, pat_age,
                                                                        pat_gender, pat_weight, pat_height, pat_address,
                                                                        pat_contact):
                                messagebox.showinfo('Success', "Patients Updated")
                                self.showitemintree_patientdata()
                                self.update_index0 = ""
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

    # ===================================== SEARCHING CONTENT IN DATABASE ===================================#
    def patientsearch(self):
        if len(self.patient_search_value.get()) != 0 and len(self.patient_search_obj.get()) != 0:
            searcheed_data0 = self.admin_backend.return_patient_search_data(self.patient_search_value.get(),
                                                                            self.patient_search_obj.get())
            if len(searcheed_data0) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
                self.patientboard_tree.delete(*self.patientboard_tree.get_children())
            else:
                self.patientboard_tree.delete(*self.patientboard_tree.get_children())
                for i in searcheed_data0:
                    self.patientboard_tree.insert("", "end", text=i[0],
                                                  value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                self.patientboard_tree.bind("<Double-1>", self.patient_onitemselect)
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")

    # ============================================== Delete Patient=========================================#
    def deletepatients(self):
        if self.update_index0 == "":
            messagebox.showerror("Can't delete", "Please select a row first.")
        else:
            if self.admin_backend.delete_patients(self.update_index0):
                messagebox.showinfo("Patient Data Deleted", "The desired data is now deleted.")
                self.showitemintree_patientdata()
            else:
                messagebox.showerror("Can't delete", "Delete Failed")

    # ==================================================== SCHEDULE ================================================#
    def scheduleboard(self):
        self.deleteframe()
        self.endphoto()
        self.display_date()
        self.display_time()
        # ============================================= FIRST SEPERATOR ============================================#
        self.data0 = 22
        while self.data0 <= 790:
            self.seperator0 = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator0.configure(bg="black")
            self.seperator0.place(x=self.data0, y=9)
            self.data0 += 10
        # ============================================= SECOND SEPERATOR ===========================================#
        self.data = 22
        while self.data <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data, y=70)
            self.data += 10

        # ============================================== Schedule Logo ==============================================#
        self.schedule_photo = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\schedulelogo.png")
        self.schedule_photo_lable = Label(self.navigation_frame0, image=self.schedule_photo, bg="white")
        self.schedule_photo_lable.image = self.schedule_photo
        self.schedule_photo_lable.grid(row=3, column=0, padx=5)

        self.schedule_photo1 = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\schedule.png")
        self.schedule_photo1_lable = Label(self.navigation_frame, image=self.schedule_photo1, bg="white")
        self.schedule_photo1_lable.image = self.schedule_photo1

        # ========================================== HEADING LABEL - SCHEDULE ======================================#
        self.scheduleboard_lbhead = Label(self.navigation_frame, text="SCHEDULES", image=self.schedule_photo1,
                                          compound=TOP, bg="white", font=('Arial', 18, 'bold', 'underline'), fg='Black')
        self.scheduleboard_lbhead.grid(row=2, column=1, columnspan=3, padx=10, pady=12)

        # ============================================ FIRST LABEL - NAME ==========================================#
        self.scheduleboard_lb1 = Label(self.navigation_frame, text="Name of the Doctor", bg="white",
                                       font=('Arial', 12, 'bold'), fg='Black')
        self.scheduleboard_lb1.grid(row=3, column=1, padx=10, pady=14)

        # =========================================== SCEOND LABEL - TIME ===========================================#
        self.scheduleboard_lb2 = Label(self.navigation_frame, text="Time allocated for Doctor", bg="white",
                                       font=('Arial', 12, 'bold'), fg='Black')
        self.scheduleboard_lb2.grid(row=4, column=1, padx=10, pady=14)

        # ======================================== THIRD LABEL - DOC StatS ==========================================#
        self.scheduleboard_lb3 = Label(self.navigation_frame, text="Doctor Status", bg="white",
                                       font=('Arial', 12, 'bold'), fg='Black')
        self.scheduleboard_lb3.grid(row=5, column=1, padx=10, pady=14)

        # ========================================== FIRST ENTRY - NAME =============================================#
        self.scheduleboard_entbx1_obj = StringVar()
        self.scheduleboard_entbx1 = ttk.Combobox(self.navigation_frame, state='readonly',
                                                 textvariable=self.scheduleboard_entbx1_obj, width=33, height=5)
        self.scheduleboard_entbx1['values'] = self.admin_backend.return_all_doctorname()
        self.scheduleboard_entbx1.grid(row=3, column=2, padx=10, pady=10)

        # ========================================= SCEOND ENTRY - AGE ==============================================#
        self.scheduleboard_entbx2_obj = StringVar()
        self.scheduleboard_entbx2 = ttk.Combobox(self.navigation_frame, state='readonly',
                                                 textvariable=self.scheduleboard_entbx2_obj, width=33, height=5)
        self.scheduleboard_entbx2['values'] = ["7 A.M", "8 A.M", "9 A.M", "11 A.M", "2 A.M", "3 A.M"]
        self.scheduleboard_entbx2.grid(row=4, column=2, padx=10, pady=10)

        # ======================================== THIRD ENTRY - GENDER =============================================#
        self.scheduleboard_entbx3_obj = StringVar()
        self.scheduleboard_entbx3 = ttk.Combobox(self.navigation_frame, state='readonly',
                                                 textvariable=self.scheduleboard_entbx3_obj, width=33, height=5)
        self.scheduleboard_entbx3['values'] = ["Available", "Occupied"]
        self.scheduleboard_entbx3.grid(row=5, column=2, padx=10, pady=10)

        # ================================== Schedule SEARCH COMBOBOX VALUE =========================================#
        self.schedule_search_obj = StringVar()
        self.scheduleboard_searchbox = ttk.Combobox(self.navigation_frame0, state='readonly',
                                                    textvariable=self.schedule_search_obj, width=27, height=5)
        self.scheduleboard_searchbox['values'] = ["Doctor_Name", "Time", "Doctor_Availability"]
        self.scheduleboard_searchbox.grid(row=4, column=0, pady=10)

        # ======================================= Schedule SEARCH VALUE =============================================#
        self.schedule_search_value = StringVar()
        self.scheduleboard_searchbx10 = Entry(self.navigation_frame0, textvariable=self.schedule_search_value,
                                              bg="white", fg="black", font=("arial", 12, "bold"))
        self.scheduleboard_searchbx10.grid(row=5, column=0, pady=10)

        # ============================================ Schedule TREE =================================================#
        self.yscroll = Scrollbar(self.tree_frame, orient=VERTICAL)
        self.yscroll.pack(side=RIGHT, fill=Y)
        self.scheduleboard_tree = ttk.Treeview(self.tree_frame, column=("Name", "Time", "Availability"),
                                               yscrollcommand=self.yscroll.set, height=11)
        self.yscroll.config(command=self.scheduleboard_tree.yview)
        self.scheduleboard_tree.pack()
        self.scheduleboard_tree['show'] = 'headings'

        self.scheduleboard_tree.column('Name', width=290, anchor="center")
        self.scheduleboard_tree.column('Time', width=250, anchor="center")
        self.scheduleboard_tree.column('Availability', width=255, anchor="center")
        self.scheduleboard_tree.heading('Name', text="Name")
        self.scheduleboard_tree.heading('Time', text="Time")
        self.scheduleboard_tree.heading('Availability', text="Availability")

        # ==================================== ADD Button with picture inserted =====================================#
        self.schedule_addbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\addbutton.png")
        self.schedule_addbutton = Button(self.navigation_frame, image=self.schedule_addbutton_img,
                                         command=self.addschedule, bg="white", fg="black", font=("arial", 15),
                                         height=25, width=95)
        self.schedule_addbutton.image = self.schedule_addbutton_img
        self.schedule_addbutton.grid(row=15, column=1, columnspan=2, padx=10, pady=22)

        # =================================== SHOW Button with picture inserted =====================================#
        self.scheduleboard_showbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\showbutton.png")
        self.scheduleboard_showbutton = Button(self.navigation_frame, image=self.scheduleboard_showbutton_img,
                                               bg="white", command=self.showitemintree_scheduledata, fg="black",
                                               font=("arial", 15), height=40, width=120)
        self.scheduleboard_showbutton.image = self.scheduleboard_showbutton_img
        self.scheduleboard_showbutton.grid(row=0, column=1, columnspan=3, padx=344, pady=15)

        # =================================== UPDATE Button with picture inserted ====================================#
        self.scheduleboard_updatebutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\updatebutton.png")
        self.scheduleboard_updatebutton = Button(self.navigation_frame, image=self.scheduleboard_updatebutton_img,
                                                 bg="white", command=self.schedule_updatefrntend, fg="black",
                                                 font=("arial", 15), height=25, width=95)
        self.scheduleboard_updatebutton.image = self.scheduleboard_updatebutton_img
        self.scheduleboard_updatebutton.grid(row=15, column=2, padx=10, pady=22)

        # =================================== DELETE Button with picture inserted ====================================#
        self.scheduleboard_deletebutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\deletebutton.png")
        self.scheduleboard_deletebutton = Button(self.navigation_frame, image=self.scheduleboard_deletebutton_img,
                                                 command=self.deleteschedules, bg="white", fg="black",
                                                 font=("arial", 15), height=25, width=95)
        self.scheduleboard_deletebutton.image = self.scheduleboard_deletebutton_img
        self.scheduleboard_deletebutton.grid(row=15, column=1, padx=10, pady=22)

        # =================================== SEARCH Button with picture inserted ====================================#
        self.scheduleboard_searchbutton_img = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\searchbutton.png")
        self.scheduleboard_searchbutton = Button(self.navigation_frame0, image=self.scheduleboard_searchbutton_img,
                                                 command=self.schedulesearch, bg="white", fg="black",
                                                 font=("arial", 15), height=25, width=95)
        self.scheduleboard_searchbutton.image = self.scheduleboard_searchbutton_img
        self.scheduleboard_searchbutton.grid(row=6, column=0, pady=10)

        # ============================================ THIRD SEPERATOR ===============================================#
        self.data1 = 22
        while self.data1 <= 790:
            self.seperator = Canvas(self.navigation_frame, width=5, height=1, bd=0, highlightthickness=0)
            self.seperator.configure(bg="black")
            self.seperator.place(x=self.data1, y=400)
            self.data1 += 10

    # ============================== ADDING SERVICE ==============================#
    def addschedule(self):
        global count
        sedule_name = self.scheduleboard_entbx1_obj.get()
        sedule_time = self.scheduleboard_entbx2_obj.get()
        sedule_docstatus = self.scheduleboard_entbx3_obj.get()
        if len(sedule_name) != 0 and len(sedule_time) != 0 and len(sedule_docstatus) != 0:
            if self.check_existing_schedule() != 1:
                if self.admin_backend.schedule_add(sedule_name, sedule_time, sedule_docstatus):
                    messagebox.showinfo('Success', "Schedule Added")
                    self.showitemintree_scheduledata()
                    self.update_index0 = ""
                else:
                    messagebox.showerror("Error", "Can't add your service.")
            else:
                messagebox.showerror("Error", "Can't add existing service.")
        else:
            messagebox.showerror("Error", "Can't leave any blank spaces.")

    # ================== SHOWING CONTENT IN SERVICE TREE ==========================#
    def showitemintree_scheduledata(self):
        self.scheduleboard_tree.delete(*self.scheduleboard_tree.get_children())
        reqdata = self.admin_backend.schedule_backend_showdata()
        for i in reqdata:
            self.scheduleboard_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3]))
        self.scheduleboard_tree.bind("<Double-1>", self.schedule_onitemselect)

    # ======================== SELECTING CONTENT IN TREE ==========================#
    def schedule_onitemselect(self, event):
        selected_row0 = self.scheduleboard_tree.selection()[0]
        selected_item0 = self.scheduleboard_tree.item(selected_row0, 'values')
        self.update_index0 = self.scheduleboard_tree.item(selected_row0, 'text')

        self.scheduleboard_entbx1.delete(0, END)
        self.scheduleboard_entbx1.insert(0, selected_item0[0])
        self.scheduleboard_entbx2.delete(0, END)
        self.scheduleboard_entbx2.insert(0, selected_item0[1])
        self.scheduleboard_entbx3.delete(0, END)
        self.scheduleboard_entbx3.insert(0, selected_item0[2])

    # ======================== UPDATING CONTENT IN TREE ============================#
    def schedule_updatefrntend(self):
        if self.update_index0 == "":
            messagebox.showerror("Error", "Please select a row first")
        else:
            sedule_name = self.scheduleboard_entbx1_obj.get()
            sedule_time = self.scheduleboard_entbx2_obj.get()
            sedule_docstatus = self.scheduleboard_entbx3_obj.get()
            if len(sedule_name) != 0 and len(sedule_time) != 0 and len(sedule_docstatus) != 0:
                if self.admin_backend.schedule_status_update(self.update_index0, sedule_name, sedule_time,
                                                             sedule_docstatus):
                    messagebox.showinfo('Item', "Item Updated")
                    self.showitemintree_scheduledata()
                    self.update_index0 = ""
                else:
                    messagebox.showerror("Error", 'Can not be updated !!!')
            else:
                messagebox.showerror("Error", "Can't leave any blank spaces.")

    # ======================= SEARCHING CONTENT IN DATABASE ========================#
    def schedulesearch(self):
        if len(self.schedule_search_value.get()) != 0 and len(self.schedule_search_obj.get()) != 0:
            searcheed_data0 = self.admin_backend.return_schedule_search_data(self.schedule_search_value.get(),
                                                                             self.schedule_search_obj.get())
            if len(searcheed_data0) == 0:
                messagebox.showinfo("Data Unavailable", "No such data exist.")
                self.scheduleboard_tree.delete(*self.scheduleboard_tree.get_children())
            else:
                self.scheduleboard_tree.delete(*self.scheduleboard_tree.get_children())
                for i in searcheed_data0:
                    self.scheduleboard_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
                self.scheduleboard_tree.bind("<Double-1>", self.schedule_onitemselect)
        else:
            messagebox.showerror("Empty Data to conduct search", "Search not accomplised with empty data.")

    # ================================= Delete Patient================================#
    def deleteschedules(self):
        if self.update_index0 == "":
            messagebox.showerror("Can't delete", "Please select a row first.")
        else:
            if self.admin_backend.delete_schedules(self.update_index0):
                messagebox.showinfo("Schedule Deleted", "The desired data is now deleted.")
                self.showitemintree_scheduledata()
            else:
                messagebox.showerror("Can't delete", "Delete Failed")

    # =========================== SEARCHING CONTENT IN DATABASE =======================#
    def check_existing_schedule(self):
        sedule_name = self.scheduleboard_entbx1_obj.get()
        sedule_time = self.scheduleboard_entbx2_obj.get()
        for i in range(len(self.admin_backend.return_all_scheduledetail())):
            if self.admin_backend.return_all_scheduledetail()[i][0] == sedule_name and \
                    self.admin_backend.return_all_scheduledetail()[i][1] == sedule_time:
                return 1

    # =========================== DATE AND TIME SELECTED FRAME ========================#
    def display_time(self):
        current_time = tm.strftime('%I:%M:%S %p ')
        self.wn.after(200, self.display_time)
        clock_label = Label(self.navigation_frame0, text=current_time, font=("Ticking Timebomb BB Regular", 27),
                            bg='white', fg='#000000')
        clock_label.grid(row=0, column=0, padx=12, pady=2)

    def display_date(self):
        x = datetime.datetime.now()
        current_date = x.strftime('%A,%B %d')
        date_label = Label(self.navigation_frame0, text=current_date, font="Ariel 15", bg='white', fg='#2b2b2b')
        date_label.grid(row=1, column=0, pady=2)

    # ============================ DELETE LAST SELECTED FRAME =========================#
    def deleteframe(self):
        for widget in self.navigation_frame.winfo_children():
            widget.destroy()
        for widget in self.navigation_frame0.winfo_children():
            widget.destroy()
        for widget in self.tree_frame.winfo_children():
            widget.destroy()

    # =================================== Logging out ==================================#
    def logout(self):
        self.wn.destroy()
        from interface.first_window import Firstwindow
        Firstwindow()

    # ==================================== END PHOTO ===================================#
    def endphoto(self):
        self.photo00 = PhotoImage(
            file="C:\\Users\\Aashrit\\Desktop\\Clinic_management_system\\pictures\\hospendlogo.png")
        self.photo_lable00 = Label(self.navigation_frame0, image=self.photo00, bg="white")
        self.photo_lable00.image = self.photo00
        self.photo_lable00.grid(row=8, column=0, padx=5, pady=43)

