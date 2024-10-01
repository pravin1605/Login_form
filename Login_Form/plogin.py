import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import Label, RIDGE, Toplevel, IntVar
from PIL import Image, ImageTk
from tkinter import Frame, LabelFrame, Entry, Text, Button, StringVar, END
from tkinter import Frame, TOP, messagebox, Checkbutton

import random
import time
import datetime
import mysql.connector

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1540x800+0+0")

        self.var_email = StringVar()
        self.var_password = StringVar()

        self.bg_image = Image.open(r"C:\Users\Admin\OneDrive\Documents\Login_Form\2023-hacker-login-form.png")
        self.bg_image = self.bg_image.resize((1540, 800), Image.LANCZOS)  # Resize to fit the window
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Place the background image in the window
        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create the frame
        frame = Frame(self.root, bg="#0c1e2c", bd=2, relief=RIDGE)
        frame.place(x=(1540-570)//2, y=(800-600)//2, width=570, height=600)

        # Add a header image
        img1 = Image.open(r"C:\Users\Admin\OneDrive\Documents\Login_Form\brain-machine-interface.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="#0c1e2c", borderwidth=0)
        lblimg1.place(x=(1540-100)//2, y=(800-600)//2-100, width=100, height=100)

        # Header text
        get_str = Label(frame, text="Get Started", font=("times new roman", 40, "bold"), fg="white", bg="#0c1e2c")
        get_str.place(x=130, y=50)

        # ================================= Labels =================================
        username = Label(frame, text="Username", font=("times new roman", 20, "bold"), fg="white", bg="#0c1e2c")
        username.place(x=100, y=170)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=150, y=200, width=270)

        password = Label(frame, text="Password", font=("times new roman", 20, "bold"), fg="white", bg="#0c1e2c")
        password.place(x=100, y=270)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show='*')
        self.txtpass.place(x=150, y=300, width=270)

        # ==================== Icon Image ===========================
        img2 = Image.open(r"C:\Users\Admin\OneDrive\Documents\Login_Form\lock-4441691_1280.png")
        img2 = img2.resize((40, 40), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(frame, image=self.photoimage2, bg="#0c1e2c", borderwidth=0)
        lblimg2.place(x=50, y=200, width=40, height=40)

        img3 = Image.open(r"C:\Users\Admin\OneDrive\Documents\Login_Form\85e5492d-f360-4273-92b0-4ce2324807cb.jpg")
        img3 = img3.resize((40, 40), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(frame, image=self.photoimage3, bg="#0c1e2c", borderwidth=0)
        lblimg3.place(x=50, y=300, width=40, height=40)

        # ==================== Buttons ===========================
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), fg="white", bg="#1c6e8c", cursor="hand2", activebackground="#1c6e8c", activeforeground="white")
        loginbtn.place(x=215, y=380, width=120, height=35)

        forgotbtn = Button(frame, command=self.forgot_password_window, text="Forgot Password?", font=("times new roman", 10, "bold"), fg="white", bg="#0c1e2c", cursor="hand2", borderwidth=0, activebackground="#0c1e2c", activeforeground="white")
        forgotbtn.place(x=50, y=450, width=130, height=35)

        newuserbtn = Button(frame, command=self.register_window, text="New Register", font=("times new roman", 10, "bold"), fg="white", bg="#0c1e2c", cursor="hand2", borderwidth=0, activebackground="#0c1e2c", activeforeground="white")
        newuserbtn.place(x=370, y=450, width=130, height=35)

    def login(self):
        pass

    def forgot_password_window(self):
        pass

    def register_window(self):
        pass

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = Login_Window(root)
    root.mainloop()
