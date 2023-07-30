import re
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess
import pymysql

# widget =GUI elements: button, textboxes,labels, images
# windows= serves as a container to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry("1000x650")
window.title("Prodigy's Pursuit - Sign Up")

logo = PhotoImage(file='Grand Logo.png')
window.iconphoto(True, logo)
window.config(background="#E7C6FF")

img = ImageTk.PhotoImage(Image.open("Sign up Page.png"))
label = Label(window, image=img)
label.pack()
label.place(x=0, y=0)

firstname_entry = Entry(window,
                        font=("Cambria", 10)
                        )
firstname_entry.pack(side=LEFT)
firstname_entry.place(x=595, y=240)

lastname_entry = Entry(window,
                       font=("Cambria", 10)
                       )
lastname_entry.pack(side=LEFT)
lastname_entry.place(x=780, y=240)

username_entry = Entry(window,
                       font=("Montserrat", 10)
                       )
username_entry.pack(side=LEFT)
username_entry.place(x=730, y=300)

email_entry = Entry(window,
                    font=("Montserrat", 10)
                    )
email_entry.pack(side=LEFT)
email_entry.place(x=730, y=355)

password_entry = Entry(window,
                       font=("Cambria", 10),
                       show='*')
password_entry.pack(side=LEFT)
password_entry.place(x=599, y=440)

confirm_password_entry = Entry(window,
                               font=("Cambria", 10),
                               show='*')
confirm_password_entry.pack(side=LEFT)
confirm_password_entry.place(x=780, y=440)

# Connect to MySQL database
db = pymysql.connect(
    host="localhost",
    user="root",
    password="Hellojavashit69",
    database="prodigyspursuit"
)

# Create cursor object
cursor = db.cursor()


def validate_form():
    # Get user input from entry fields
    firstname = firstname_entry.get().strip()
    lastname = lastname_entry.get().strip()
    username = username_entry.get().strip()
    emailid = email_entry.get().strip()
    password = password_entry.get().strip()
    cpassword = confirm_password_entry.get().strip()

    # Check if all fields are filled
    if not firstname or not lastname or not username or not emailid or not password or not cpassword:
        messagebox.showerror("Error", "Please fill all the fields")
        return

        # Validate first name and last name
    if not re.match(r"^[A-Za-z ]+$", firstname) or not re.match(r"^[A-Za-z ]+$", lastname):
        messagebox.showerror("Error", "Invalid first or last name")
        return

        # Validate username (allow only alphanumeric characters and underscores)
    if not re.match(r"^\w+$", username):
        messagebox.showerror("Error", "Invalid username")
        return

        # Validate email
    if not re.match(r"[^@]+@[^@]+\.[^@]+", emailid):
        messagebox.showerror("Error", "Invalid email")
        return

        # Check if password and confirm password match
    if password != cpassword:
        messagebox.showerror("Error", "Passwords do not match")
    return True


def connect_database():
    if not validate_form():
        return
    # Get user input from entry fields
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    cpassword = confirm_password_entry.get()

    # Check if username already exists in database
    cursor.execute("SELECT * FROM signup WHERE username=%s", (username,))
    user = cursor.fetchone()
    if user:
        messagebox.showerror("Error", "Username already exists")
    else:
        # Insert new info into database
        cursor.execute(
            "INSERT INTO signup (firstname, lastname, username, email, password,cpassword) VALUES (%s, %s, %s, %s, "
            "%s,%s)",
            (firstname, lastname, username, email, password, cpassword))
        db.commit()
        messagebox.showinfo("Success", "Account created Successfully")

        # Close sign up window and open login window
        window.destroy()
        subprocess.Popen(["python", "Dashboard.py"])


button = Button(window,
                text="Create Account",
                command=connect_database,
                font=("Montserrat Light", 12),
                fg="#e5b3fe",
                bg="#7b2cbf",
                activeforeground="#e5b3fe",
                activebackground="#7209B7",
                state=ACTIVE)
button.pack()
button.place(x=750, y=510)


def on_button_click():
    # Close the current file
    window.destroy()
    # Open the new file
    subprocess.Popen(["python", "HomePage.py"])


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

window.mainloop()  # place window on computer screen, lister for events
