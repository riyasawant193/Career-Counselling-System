import re
from tkinter import *
from PIL import ImageTk, Image
import subprocess
from tkinter import messagebox
import pymysql
import tkinter as tk

# widget =GUI elements: button, textboxes,labels, images
# windows= serves as a comtainer to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry("1000x650")
window.title("Prodigy's Pursuit- Contact Us")

logo = PhotoImage(file='Grand Logo.png')
window.iconphoto(True, logo)
window.config(background="#E7C6FF")

window.geometry("1000x650")
img = ImageTk.PhotoImage(Image.open("Contact Us.png"))
label = Label(window, image=img)
label.pack()
label.place(x=0, y=0)

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
    username_entry.delete(0, END)
    email_entry.delete(0, END)
    feedback_entry.delete(0, END)


def validate_form():
    username = username_entry.get().strip()
    email = email_entry.get().strip()
    feedback = feedback_entry.get("1.0", "end-1c").strip()

    # Check if the fields are not empty
    if not username or not email or not feedback:
        messagebox.showerror("Error", "Please fill all the fields")

        return False

    # Check if the username is valid
    if not username.isalnum():
        messagebox.showerror("Error", "Invalid username")
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Invalid email")
        return

    messagebox.showinfo("Success", "Message Sent Successfully")


def connect_database():
    if not validate_form():
        return
    # Get user input from entry fields
    username = username_entry.get()
    email = email_entry.get()
    feedback = feedback_entry.get("1.0", "end-1c")

    # Check if username already exists in database
    cursor.execute("SELECT * FROM student WHERE username=%s", (username,))
    user = cursor.fetchone()
    if user:
        messagebox.showerror("Error", "Username already exists")
    else:
        # Insert new student into database
        cursor.execute(
            "INSERT INTO student (username, email, feedback) VALUES (%s, %s, %s)",
            (username, email, feedback))
        db.commit()
        messagebox.showinfo("Success", "Message Sent Successfully")

        # Clear entry fields
        clear()


button = Button(window,
                text="Send",
                command=connect_database,
                font=("Jacques Francois", 15),
                fg="#E7C6FF",
                bg="#F72585",
                activeforeground="#E7C6FF",
                activebackground="#7209B7",
                state=ACTIVE)
button.pack()
button.place(x=706, y=402)

# for username
username_entry = Entry()
username_entry.config(font=('Jacques Francois', 15))  # change font
username_entry.config(bg='white')  # background
username_entry.config(fg='#7209B7')  # foreground
username_entry.config(width=10)
username_entry.pack()
username_entry.place(x=706, y=153)

# email id
email_entry = Entry()
email_entry.config(font=('Jacques Francois', 15))  # change font
email_entry.config(bg='white')  # background
email_entry.config(fg='#7209B7')  # foreground
email_entry.config(width=10)  # width displayed in characters
email_entry.pack()
email_entry.place(x=706, y=207)

# feedback
feedback_entry = tk.Text(window, height=3, width=45)
feedback_entry.pack()
feedback_entry.place(x=562, y=318)


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
