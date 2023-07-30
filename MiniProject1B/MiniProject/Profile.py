from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image
import subprocess
from tkinter import messagebox
import re
import pymysql

window = Tk()  # instantiate an instance of a window
window.geometry("1000x650")
window.title("Prodigy's Pursuit")

logo = PhotoImage(file='Grand Logo.png')
window.iconphoto(True, logo)
window.config(background="#E7C6FF")

img = ImageTk.PhotoImage(Image.open("Paper Planes.png"))
label = Label(window, image=img)
label.pack()
label.place(x=0, y=0)

label = Label(window,
              text="Profile",
              font=('Grand Royal', 32),
              fg='#7209B7',
              bg='#E7C6FF')
label.pack()
label.place(x=500, y=50)

label = Label(window,
              text="Name:",
              font=('Cambria', 15),
              fg='#7209B7',
              bg='#E7C6FF')
label.pack()
label.place(x=500, y=120)

name_entry = Entry(window,
                   font=("Cambria", 15)
                   )
name_entry.pack(side=LEFT)
name_entry.place(x=650, y=120)

label = Label(window,
              text="Username:",
              font=('Cambria', 15),
              fg='#7209B7',
              bg='#E7C6FF')
label.pack()
label.place(x=500, y=200)

username_entry = Entry(window,
                       font=("Cambria", 15)
                       )
username_entry.pack(side=LEFT)
username_entry.place(x=650, y=200)

label = Label(window,
              text="Date of Birth:",
              font=('Cambria', 15),
              fg='#7209B7',
              bg='#E7C6FF')
label.pack()
label.place(x=500, y=280)

dob_entry = Entry(window,
                  font=("Cambria", 15)
                  )
dob_entry.pack(side=LEFT)
dob_entry.place(x=650, y=280)

label = Label(window,
              text="Email ID:",
              font=('Cambria', 15),
              fg='#7209B7',
              bg='#E7C6FF')
label.pack()
label.place(x=500, y=360)

email_entry = Entry(window,
                    font=("Cambria", 15)
                    )
email_entry.pack(side=LEFT)
email_entry.place(x=650, y=360)

label = Label(window,
              text="Mobile No.:",
              font=('Cambria', 15),
              fg='#7209B7',
              bg='#E7C6FF')
label.pack()
label.place(x=500, y=440)

mobile_entry = Entry(window,
                     font=("Cambria", 15)
                     )
mobile_entry.pack(side=LEFT)
mobile_entry.place(x=650, y=440)

# Connect to MySQL database
db = pymysql.connect(
    host="localhost",
    user="root",
    password="Hellojavashit69",
    database="prodigyspursuit"
)

# Create cursor object
cursor = db.cursor()


def clear():
    name_entry.delete(0, END)
    username_entry.delete(0, END)
    dob_entry.delete(0, END)
    email_entry.delete(0, END)
    mobile_entry.delete(0, END)


def validate_form():
    # Perform account creation logic here
    # Show a message box to indicate that the account was created successfully
    name = name_entry.get().strip()
    username = username_entry.get().strip()
    dob = dob_entry.get().strip()
    email = email_entry.get().strip()
    mobile = mobile_entry.get().strip()

    # Check if the fields are not empty
    if not name or not username or not dob or not email or not mobile:
        messagebox.showerror("Error", "All fields are required")
        return

    # Check if the name is valid
    if not all(char.isalpha() or char.isspace() for char in name):
        messagebox.showerror("Error", "Invalid name")
        return

    # Check if the username is valid
    if not username.isalnum():
        messagebox.showerror("Error", "Invalid username")
        return

    # Check if the date of birth is valid
    def validate_dob(dob):
        try:
            dob_entry = datetime.datetime.strptime(dob, '%Y-%m-%d')
            if dob_entry > datetime.datetime.now():
                return False
            return True
        except ValueError:
            return False

        dob_valid = validate_dob(dob)
        if not dob_valid:
            messagebox.showerror("Error", "Invalid date of birth. Please enter in DD-MM-YYYY format")
            return

    # Check if the email is valid
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Invalid email")
        return

    # Check if the mobile number is valid
    if not re.match(r"\d{10}$", mobile):
        messagebox.showerror("Error", "Invalid mobile number")
        return

    # Perform account creation logic here
    # Show a message box to indicate that the account was created successfully
    messagebox.showinfo("Success", "Submitted Successfully")


def connect_database():
    if not validate_form():
        return
    # Get user input from entry fields
    name = name_entry.get()
    username = username_entry.get()
    dob = dob_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()

    # Check if username already exists in database
    cursor.execute("SELECT * FROM user_info WHERE username=%s", (username,))
    user = cursor.fetchone()
    if user:
        messagebox.showerror("Error", "Username already exists")
    else:
        # Insert new userinfo into database
        cursor.execute(
            "INSERT INTO user_info (name, username, dob, email, mobile) VALUES (%s, %s, %s, %s, %s)",
            (name, username, dob, email, mobile))
        db.commit()
        messagebox.showinfo("Success", "Submitted Successfully")

        # Clear entry fields
        clear()


submit_button = Button(window,
                       text="SUBMIT",
                       command=connect_database,
                       font=("Jacques Francois", 15),
                       fg="#E7C6FF",
                       bg="#F72585",
                       activeforeground="#E7C6FF",
                       activebackground="#7209B7",
                       state=ACTIVE)
submit_button.pack(side=RIGHT)
submit_button.place(x=500, y=520)

reset_button = Button(window,
                      text="RESET",
                      command=clear,
                      font=("Jacques Francois", 15),
                      fg="#E7C6FF",
                      bg="#F72585",
                      activeforeground="#E7C6FF",
                      activebackground="#7209B7",
                      state=ACTIVE)
reset_button.pack(side=RIGHT)
reset_button.place(x=800, y=520)


def on_button_click():
    # Close the current file
    window.destroy()
    # Open the new file
    subprocess.Popen(["python", "Dashboard.py"])


button = Button(window,
                text=" ← ",
                command=on_button_click,
                font=("Montserrat", 15),
                fg="#E7C6FF",
                bg="#F72585",
                activeforeground="#E7C6FF",
                activebackground="#7209B7",
                state=ACTIVE)
button.pack()
button.place(x=950, y=10)

window.mainloop()
