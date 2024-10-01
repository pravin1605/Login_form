import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import Label, RIDGE, IntVar
from PIL import Image, ImageTk
from tkinter import  Frame, LabelFrame,Entry,Text,Button,StringVar,END
from tkinter import Frame,TOP,messagebox,Checkbutton


import random
import time
import datetime
import mysql.connector
 




class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1540x800+0+0")

        #===================variable declaration===========
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_a = StringVar()
        self.var_security_q = StringVar()
        self.var_password = StringVar()
        self.var_conf_password = StringVar()

        # Load and process the background image
        self.bg_image = Image.open(r"C:\Users\Admin\OneDrive\Documents\Login_Form\3536bb257ad4fc9ff2522920740927fe.png")
        self.bg_image = self.bg_image.resize((1540, 800), Image.LANCZOS)  # Resize to fit the window
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Place the background image in the window
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=-25, relwidth=1, relheight=1)

        # ========== Main Frame ============================
        frame = tk.Frame(self.root, bg="white", bd=5, relief=tk.RIDGE)
        frame.place(x=618, y=44, width=646, height=560)

        register_lbl = Label(frame, text="Register Here", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=10)

        # ==================================== Labels ===================================
        # Row 1
        fname_lbl = tk.Label(frame, text="First Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        fname_lbl.place(x=40, y=70)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=40, y=100, width=270)

        lname_lbl = tk.Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        lname_lbl.place(x=340, y=70)

        self.lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.lname_entry.place(x=340, y=100, width=270)

        contact_lbl = tk.Label(frame, text="Contact No.", font=("times new roman", 15, "bold"), fg="black", bg="white")
        contact_lbl.place(x=40, y=150)

        self.contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.contact_entry.place(x=40, y=180, width=270)

        email_lbl = tk.Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="black", bg="white")
        email_lbl.place(x=340, y=150)

        self.email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.email_entry.place(x=340, y=180, width=270)

        # Row 2
        security_q_lbl = tk.Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_q_lbl.place(x=40, y=230)

        self.combo_security_q = ttk.Combobox(frame, textvariable=self.var_security_q, font=("times new roman", 10, "bold"), state="readonly")
        self.combo_security_q['values'] = ("Select Question", "What is your mother's maiden name?", "What was the name of your first pet?", "What was your first car?", "Your birth date?")
        self.combo_security_q.place(x=40, y=260, width=270)
        self.combo_security_q.current(0)

        security_a_lbl = tk.Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_a_lbl.place(x=340, y=230)

        self.security_a_entry = ttk.Entry(frame, textvariable=self.var_security_a, font=("times new roman", 15, "bold"))
        self.security_a_entry.place(x=340, y=260, width=270)

        password_lbl = tk.Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        password_lbl.place(x=40, y=310)

        self.txt_password = ttk.Entry(frame, textvariable=self.var_password, font=("times new roman", 15, "bold"), show='*')
        self.txt_password.place(x=40, y=340, width=270)

        confirm_pswd = tk.Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        confirm_pswd.place(x=340, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_conf_password, font=("times new roman", 15, "bold"), show='*')
        self.txt_confirm_pswd.place(x=340, y=340, width=270)

        #================check Button==================================
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=("times new roman", 15, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=140, y=390)

        # Register Button
        register_btn = tk.Button(frame, command=self.register_data, text="Register", font=("times new roman", 15, "bold"), bg="darkgreen", fg="white", cursor="hand2")
        register_btn.place(x=250, y=430, width=150, height=40)

        login_btn = tk.Button(frame, text="Login", font=("times new roman", 15, "bold"), bg="darkblue", fg="white", cursor="hand2")
        login_btn.place(x=10, y=470, width=100, height=40)

    #=============================Function declaration=================
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_security_q.get() == "Select Question":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_password.get() != self.var_conf_password.get():
            messagebox.showerror("Error", "Password and confirm password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to the terms and conditions")
        else: #daabase connection start
            conn=mysql.connector.connect(host="localhost",user="root",password="Pravin@16",database="hmsdata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exist,try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_security_q.get(),
                                                                                        self.var_security_a.get(),
                                                                                        self.var_password.get()

                                                                                            ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Succesful","Register Successfully")
            













if __name__ == "__main__":
    root = tk.Tk()
    app = Register(root)
    root.mainloop()