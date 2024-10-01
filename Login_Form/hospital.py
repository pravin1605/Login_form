import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import Label, RIDGE
from PIL import Image, ImageTk
from tkinter import  Frame, LabelFrame,Entry,Text,Button,StringVar,END
from tkinter import Frame,TOP


import random
import time
import datetime
import mysql.connector
     
class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management")
        self.root.geometry("1540x800+0+0")

        # Variables
        self.NameTablet = tk.StringVar()
        self.ref = tk.StringVar()
        self.Dose = tk.StringVar()
        self.NumberTablet = tk.StringVar()
        self.Lot = tk.StringVar()
        self.issueDate = tk.StringVar()
        self.ExpDate = tk.StringVar()
        self.DailyDose = tk.StringVar()
        self.SideEffect = tk.StringVar()
        self.FurtherInformation = tk.StringVar()
        self.BloodPressure = tk.StringVar()
        self.StorageAdvise = tk.StringVar()
        self.HowToUseMedication = tk.StringVar()
        self.PatientID = tk.StringVar()
        self.NHSnumber = tk.StringVar()
        self.DateOfBirth = tk.StringVar()
        self.PatientAddress = tk.StringVar()
        self.PatientName = tk.StringVar()

        # Title
        self.lbltitle = tk.Text(self.root, bd=20, relief=tk.RIDGE, bg="darkblue", height=6)
        self.lbltitle.pack(side=tk.TOP, fill=tk.X)
        self.lbltitle.tag_configure("center", justify='center')
        self.lbltitle.tag_configure("red", foreground="red", font=("times new roman", 60, "bold"))
        self.lbltitle.tag_configure("white", foreground="white", font=("times new roman", 50, "bold"))

        self.lbltitle.insert(tk.END, "+", "red")
        self.lbltitle.insert(tk.END, " Hospital Management System ", "white")
        self.lbltitle.insert(tk.END, "+", "red")
        self.lbltitle.tag_add("center", 1.0, "end")
        self.lbltitle.config(state=tk.DISABLED)

        # Dataframe Frame
        self.Dataframe = tk.Frame(self.root, bd=15, relief=tk.RIDGE, bg="lightgreen")
        self.Dataframe.place(x=0, y=130, width=1530, height=350)

        # Load and set the background image
        self.bg_image = Image.open("pexels-tima-miroshnichenko-6011602.jpg")  # Replace with your image path
        self.bg_image = self.bg_image.resize((1530, 350), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.Dataframe, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)  # Fill the entire frame

        # Dataframe Left Widgets
        self.DataframeLeft = tk.LabelFrame(self.Dataframe, bd=10, relief=tk.RIDGE, padx=10, font=("arial", 12, "bold"), text="Patient Information", bg="lightgreen")
        self.DataframeLeft.place(x=0, y=5, width=900, height=300)

        lblNameTablet = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Name of Tablet", padx=2, pady=4, bg="lightgreen")
        lblNameTablet.grid(row=0, column=0, sticky=tk.W)
        comNameTablet = ttk.Combobox(self.DataframeLeft, textvariable=self.NameTablet, state="readonly", font=("arial", 12, "bold"), width=33)
        comNameTablet["values"] = ("Nice", "corona vaccine", "acetaminophen", "adderall", "amlodipine")
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1)

        lblref = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2, pady=4, bg="lightgreen")
        lblref.grid(row=1, column=0, sticky=tk.W)
        txtref = tk.Entry(self.DataframeLeft, textvariable=self.ref, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1, column=1)

        lblDose = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Dose", padx=2, pady=4, bg="lightgreen")
        lblDose.grid(row=2, column=0, sticky=tk.W)
        txtDose = tk.Entry(self.DataframeLeft, textvariable=self.Dose, font=("arial", 13, "bold"), width=35)
        txtDose.grid(row=2, column=1)

        lblTablet = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="No Of Tablet", padx=2, pady=4, bg="lightgreen")
        lblTablet.grid(row=3, column=0, sticky=tk.W)
        txtTablet = tk.Entry(self.DataframeLeft, textvariable=self.NumberTablet, font=("arial", 13, "bold"), width=35)
        txtTablet.grid(row=3, column=1)

        lblLot = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Lot", padx=2, pady=4, bg="lightgreen")
        lblLot.grid(row=4, column=0, sticky=tk.W)
        txtLot = tk.Entry(self.DataframeLeft, textvariable=self.Lot, font=("arial", 13, "bold"), width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Issue Date", padx=2, pady=4, bg="lightgreen")
        lblissueDate.grid(row=5, column=0, sticky=tk.W)
        txtissueDate = tk.Entry(self.DataframeLeft, textvariable=self.issueDate, font=("arial", 13, "bold"), width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Expiry Date", padx=2, pady=4, bg="lightgreen")
        lblExpDate.grid(row=6, column=0, sticky=tk.W)
        txtExpDate = tk.Entry(self.DataframeLeft, textvariable=self.ExpDate, font=("arial", 13, "bold"), width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Daily Dose", padx=2, pady=4, bg="lightgreen")
        lblDailyDose.grid(row=7, column=0, sticky=tk.W)
        txtDailyDose = tk.Entry(self.DataframeLeft, textvariable=self.DailyDose, font=("arial", 13, "bold"), width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Side Effect", padx=2, pady=4, bg="lightgreen")
        lblSideEffect.grid(row=8, column=0, sticky=tk.W)
        txtSideEffect = tk.Entry(self.DataframeLeft, textvariable=self.SideEffect, font=("arial", 13, "bold"), width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherInformation = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Further Information", padx=2, pady=4, bg="lightgreen")
        lblFurtherInformation.grid(row=0, column=2, sticky=tk.W)
        txtFurtherInformation = tk.Entry(self.DataframeLeft, textvariable=self.FurtherInformation, font=("arial", 13, "bold"), width=35)
        txtFurtherInformation.grid(row=0, column=3)

        lblBloodPressure = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Blood Pressure", padx=2, pady=4, bg="lightgreen")
        lblBloodPressure.grid(row=1, column=2, sticky=tk.W)
        txtBloodPressure = tk.Entry(self.DataframeLeft, textvariable=self.BloodPressure, font=("arial", 13, "bold"), width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Storage", padx=2, pady=4, bg="lightgreen")
        lblStorage.grid(row=2, column=2, sticky=tk.W)
        txtStorage = tk.Entry(self.DataframeLeft, textvariable=self.StorageAdvise, font=("arial", 13, "bold"), width=35)
        txtStorage.grid(row=2, column=3)

        lblMedication = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Medication", padx=2, pady=4, bg="lightgreen")
        lblMedication.grid(row=3, column=2, sticky=tk.W)
        txtMedication = tk.Entry(self.DataframeLeft, textvariable=self.HowToUseMedication, font=("arial", 13, "bold"), width=35)
        txtMedication.grid(row=3, column=3)

        lblPatientId = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Patient ID", padx=2, pady=4, bg="lightgreen")
        lblPatientId.grid(row=4, column=2, sticky=tk.W)
        txtPatientId = tk.Entry(self.DataframeLeft, textvariable=self.PatientID, font=("arial", 13, "bold"), width=35)
        txtPatientId.grid(row=4, column=3)

        lblNHSnumber = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="NHS Number", padx=2, pady=4, bg="lightgreen")
        lblNHSnumber.grid(row=5, column=2, sticky=tk.W)
        txtNHSnumber = tk.Entry(self.DataframeLeft, textvariable=self.NHSnumber, font=("arial", 13, "bold"), width=35)
        txtNHSnumber.grid(row=5, column=3)

        lblDateOfBirth = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Date of Birth", padx=2, pady=4, bg="lightgreen")
        lblDateOfBirth.grid(row=6, column=2, sticky=tk.W)
        txtDateOfBirth = tk.Entry(self.DataframeLeft, textvariable=self.DateOfBirth, font=("arial", 13, "bold"), width=35)
        txtDateOfBirth.grid(row=6, column=3)

        lblPatientAddress = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Patient Address", padx=2, pady=4, bg="lightgreen")
        lblPatientAddress.grid(row=8, column=2, sticky=tk.W)
        txtPatientAddress = tk.Entry(self.DataframeLeft, textvariable=self.PatientAddress, font=("arial", 13, "bold"), width=35)
        txtPatientAddress.grid(row=8, column=3)

        lblPatientName = tk.Label(self.DataframeLeft, font=("arial", 12, "bold"), text="Patient Name", padx=2, pady=4, bg="lightgreen")
        lblPatientName.grid(row=7, column=2, sticky=tk.W)
        txtPatientName = tk.Entry(self.DataframeLeft, textvariable=self.PatientName, font=("arial", 13, "bold"), width=35)
        txtPatientName.grid(row=7, column=3)

        # Dataframe Right Widgets
        DataframeRight = tk.LabelFrame(self.Dataframe, bd=10, relief=tk.RIDGE, padx=10, font=("arial", 12, "bold"), text="Prescription", bg="lightgreen")
        DataframeRight.place(x=910, y=5, width=600, height=300)

        self.textPrescription = tk.Text(DataframeRight, font=("arial", 13, "bold"), width=35, height=13, padx=2, pady=6)
        self.textPrescription.grid(row=0, column=0, padx=5, pady=5)


        # Button Frame
        buttonframe = tk.Frame(self.root, bd=15, relief=tk.RIDGE, bg="lightblue")
        buttonframe.place(x=0, y=450, width=1530, height=50)

        # Details Frame
        Detailsframe = tk.Frame(self.root, bd=15, relief=tk.RIDGE, bg="lightblue")
        Detailsframe.place(x=0, y=500, width=1530, height=150)


        # ==================button Prescription==========================
        btnPrescription = tk.Button(buttonframe,command=self.iPrescription, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=2)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = tk.Button(buttonframe,command=self.iPrescriptionData, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=2)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = tk.Button(buttonframe,command=self.update_data,  text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=1)
        btnUpdate.grid(row=0, column=2)

        btnDelete = tk.Button(buttonframe, command=self.delete_data, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=1)
        btnDelete.grid(row=0, column=3)

        btnClear = tk.Button(buttonframe, command=self.clear_data, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=2)
        btnClear.grid(row=0, column=4)

        btnExit = tk.Button(buttonframe, command=self.exit_app, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=1, padx=2, pady=2)
        btnExit.grid(row=0, column=5)

        # ==================Table==========================
        # Scrollbars
        scroll_x = ttk.Scrollbar(Detailsframe, orient="horizontal")
        scroll_y = ttk.Scrollbar(Detailsframe, orient="vertical")

        # Treeview (hospital_table)
        self.hospital_table = ttk.Treeview(Detailsframe, columns=("NameTablet", "ref", "Dose", "Lot", "issueDate",
                                                                  "ExpDate", "DailyDose", "StorageAdvise", "NHSnumber", "PatientName", "DateOfBirth", "PatientAddress"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        # Packing order
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.hospital_table.pack(fill=tk.BOTH, expand=1)

        # Column Headings
        self.hospital_table.heading("NameTablet", text="Name of Tablet")
        self.hospital_table.heading("ref", text="Reference No")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("Lot", text="Lot")
        self.hospital_table.heading("issueDate", text="Issue Date")
        self.hospital_table.heading("ExpDate", text="Expiry Date")
        self.hospital_table.heading("DailyDose", text="Daily Dose")
        self.hospital_table.heading("StorageAdvise", text="Storage Advise")
        self.hospital_table.heading("NHSnumber", text="NHS Number")
        self.hospital_table.heading("PatientName", text="Patient Name")
        self.hospital_table.heading("DateOfBirth", text="Date of Birth")
        self.hospital_table.heading("PatientAddress", text="Patient Address")

        # Display the headings
        self.hospital_table["show"] = "headings"

        self.hospital_table.column("NameTablet", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("Dose", width=100)
        self.hospital_table.column("Lot", width=100)
        self.hospital_table.column("issueDate", width=100)
        self.hospital_table.column("ExpDate", width=100)
        self.hospital_table.column("DailyDose", width=100)
        self.hospital_table.column("StorageAdvise", width=100)
        self.hospital_table.column("NHSnumber", width=100)
        self.hospital_table.column("PatientName", width=100)
        self.hospital_table.column("DateOfBirth", width=100)
        self.hospital_table.column("PatientAddress", width=100)
         
        self.hospital_table.pack(fill=tk.BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # ==================functionality declaration===================
    def iPrescription(self):
        self.textPrescription.insert(tk.END, "Name of Tablet: " + self.NameTablet.get() + "\n")
        self.textPrescription.insert(tk.END, "Reference No: " + self.ref.get() + "\n")
        self.textPrescription.insert(tk.END, "Dose: " + self.Dose.get() + "\n")
        self.textPrescription.insert(tk.END, "Lot: " + self.Lot.get() + "\n")
        self.textPrescription.insert(tk.END, "Issue Date: " + self.issueDate.get() + "\n")
        self.textPrescription.insert(tk.END, "Expiry Date: " + self.ExpDate.get() + "\n")
        self.textPrescription.insert(tk.END, "Daily Dose: " + self.DailyDose.get() + "\n")
        self.textPrescription.insert(tk.END, "Storage Advise: " + self.StorageAdvise.get() + "\n")
        self.textPrescription.insert(tk.END, "NHS Number: " + self.NHSnumber.get() + "\n")
        self.textPrescription.insert(tk.END, "Patient Name: " + self.PatientName.get() + "\n")
        self.textPrescription.insert(tk.END, "Date of Birth: " + self.DateOfBirth.get() + "\n")
        self.textPrescription.insert(tk.END, "Patient Address: " + self.PatientAddress.get() + "\n")

    def iPrescriptionData(self):
        if self.NameTablet.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Pravin@16", database="hmsdata")
                my_cursor = conn.cursor()
                
                # Ensure column names match the actual table schema
                my_cursor.execute("INSERT INTO hospital (NameTablet, ref, Dose, Lot, issueDate, ExpDate, DailyDose, StorageAdvise, NHSnumber, PatientName, DateOfBirth, PatientAddress) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                  (self.NameTablet.get(), self.ref.get(), self.Dose.get(), self.Lot.get(),
                                   self.issueDate.get(), self.ExpDate.get(), self.DailyDose.get(),
                                   self.StorageAdvise.get(), self.NHSnumber.get(), self.PatientName.get(),
                                   self.DateOfBirth.get(), self.PatientAddress.get()))
                
                conn.commit()
                conn.close()
                
                # Call fetch_data to update the displayed data in the treeview
                self.fetch_data()
                
                messagebox.showinfo("Success", "Prescription data added successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error in inserting data: {str(e)}")

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Pravin@16", database="hmsdata")
            my_cursor = conn.cursor()
            
            my_cursor.execute("SELECT * FROM hospital")
            rows = my_cursor.fetchall()
            
            # Clear existing data in the treeview
            self.hospital_table.delete(*self.hospital_table.get_children())
            
            # Insert fetched data into the treeview
            for row in rows:
                self.hospital_table.insert("", tk.END, values=row)
            
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error in fetching data: {str(e)}")


    def iPrescription(self):
        self.textPrescription.insert(tk.END, "NameTablet:\t\t\t" + self.NameTablet.get() + "\n")
        self.textPrescription.insert(tk.END, "ref:\t\t\t" + self.ref.get() + "\n")
        self.textPrescription.insert(tk.END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.textPrescription.insert(tk.END, "NumberTablet:\t\t\t" + self.NumberTablet.get() + "\n")
        self.textPrescription.insert(tk.END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.textPrescription.insert(tk.END, "issueDate:\t\t\t" + self.issueDate.get() + "\n")
        self.textPrescription.insert(tk.END, "ExpDate:\t\t\t" + self.ExpDate.get() + "\n")
        self.textPrescription.insert(tk.END, "DailyDose:\t\t\t" + self.DailyDose.get() + "\n")
        self.textPrescription.insert(tk.END, "PatientName:\t\t\t" + self.PatientName.get() + "\n")
        self.textPrescription.insert(tk.END, "NHSnumber:\t\t\t" + self.NHSnumber.get() + "\n")
        self.textPrescription.insert(tk.END, "DateOfBirth:\t\t\t" + self.DateOfBirth.get() + "\n")
    

    def get_cursor(self, event=None):
        cursor_row = self.hospital_table.focus()
        contents = self.hospital_table.item(cursor_row)
        row = contents['values']
        if row:  # Ensure row is not empty
            self.NameTablet.set(row[0])
            self.ref.set(row[1])
            self.Dose.set(row[2])
            self.Lot.set(row[3])
            self.issueDate.set(row[4])
            self.ExpDate.set(row[5])
            self.DailyDose.set(row[6])
            self.StorageAdvise.set(row[7])
            self.NHSnumber.set(row[8])
            self.PatientName.set(row[9])
            self.DateOfBirth.set(row[10])
            self.PatientAddress.set(row[11])

    def update_data(self):
        if self.ref.get() == "":
            messagebox.showerror("Error", "Reference Number is required to update")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Pravin@16", database="hmsdata")
                my_cursor = conn.cursor()
                
                my_cursor.execute(
                    "UPDATE hospital SET NameTablet=%s, Dose=%s, Lot=%s, issueDate=%s, ExpDate=%s, DailyDose=%s, StorageAdvise=%s, NHSnumber=%s, PatientName=%s, DateOfBirth=%s, PatientAddress=%s WHERE ref=%s",
                    (
                        self.NameTablet.get(),
                        self.Dose.get(),
                        self.Lot.get(),
                        self.issueDate.get(),
                        self.ExpDate.get(),
                        self.DailyDose.get(),
                        self.StorageAdvise.get(),
                        self.NHSnumber.get(),
                        self.PatientName.get(),
                        self.DateOfBirth.get(),
                        self.PatientAddress.get(),
                        self.ref.get()
                    )
                )
                
                conn.commit()
                conn.close()
                
                self.fetch_data()
                self.clear_data()
                
                messagebox.showinfo("Update", "Record updated successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error in updating data: {str(e)}")
 



    def delete_data(self):
        if self.ref.get() == "":
            messagebox.showerror("Error", "Reference Number is required to delete")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Pravin@16", database="hmsdata")
                my_cursor = conn.cursor()
                
                my_cursor.execute("DELETE FROM hospital WHERE ref=%s", (self.ref.get(),))
                
                conn.commit()
                conn.close()
                
                self.fetch_data()
                self.clear_data()
                
                messagebox.showinfo("Delete", "Record deleted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error in deleting data: {str(e)}")

    def clear_data(self):
        self.NameTablet.set("")
        self.ref.set("")
        self.NumberTablet.set("")
        self.Dose.set("")
        self.Lot.set("")
        self.issueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.FurtherInformation.set("")
        self.SideEffect.set("")
        self.BloodPressure.set("")
        self.StorageAdvise.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientID.set("")
        self.NHSnumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.textPrescription.delete("1.0", tk.END)

    def exit_app(self):
        self.root.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    hospital_app = Hospital(root)
    root.mainloop()
