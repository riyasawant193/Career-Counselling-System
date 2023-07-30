from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import subprocess

window = Tk()  # instantiate an instance of a window
window.geometry("1000x650")
window.title("Prodigy's Pursuit")

logo = PhotoImage(file='Grand Logo.png')
window.iconphoto(True, logo)
window.config(background="#E7C6FF")

img = ImageTk.PhotoImage(Image.open("Ladder.png"))
label = Label(window, image=img)
label.pack()
label.place(x=0, y=0)


def on_button_click():
    # Close the current file
    window.destroy()
    # Open the new file
    subprocess.Popen(["python", "Profile.py"])


profile_button = Button(window,
                        text="PROFILE",
                        command=on_button_click,
                        font=("Jacques Francois", 15, 'bold'),
                        fg="#E7C6FF",
                        bg="#B5179E",
                        activeforeground="#E7C6FF",
                        activebackground="#B5179E",
                        state=ACTIVE)
profile_button.pack(side=RIGHT)
profile_button.place(x=885, y=15)


def on_button_click():
    # Close the current file
    window.destroy()
    # Open the new file
    subprocess.Popen(["python", "CourseOutlets.py"])


co_button = Button(window,
                   text="Course Outlets",
                   command=on_button_click,
                   font=("Jacques Francois", 10, 'bold'),
                   fg="#7209B7",
                   bg="#E7C6FF",
                   activeforeground="#7209B7",
                   activebackground="#E7C6FF",
                   state=ACTIVE)
co_button.pack(side=RIGHT)
co_button.place(x=540, y=385)


def on_button_click():
    # Close the current file
    window.destroy()
    # Open the new file
    subprocess.Popen(["python", "Take Assessment.py"])


ta_button = Button(window,
                   text="Take Assessment",
                   command=on_button_click,
                   font=("Jacques Francois", 10, 'bold'),
                   fg="#7209B7",
                   bg="#E7C6FF",
                   activeforeground="#7209B7",
                   activebackground="#E7C6FF",
                   state=ACTIVE)
ta_button.pack(side=RIGHT)
ta_button.place(x=100, y=250)


def on_button_click():
    # Close the current file
    window.destroy()
    # Open the new file
    subprocess.Popen(["python", "ShowResults.py"])


ef_button = Button(window,
                   text="Results",
                   command=on_button_click,
                   font=("Jacques Francois", 10, 'bold'),
                   fg="#7209B7",
                   bg="#E7C6FF",
                   activeforeground="#7209B7",
                   activebackground="#E7C6FF",
                   state=ACTIVE)
ef_button.pack(side=RIGHT)
ef_button.place(x=335, y=310)


def on_button_click():
    # Close the current file
    window.destroy()
    # Open the new file
    subprocess.Popen(["python", "ToDoHome.py"])


other_button = Button(window,
                      text="Others",
                      command=on_button_click,
                      font=("Jacques Francois", 10, 'bold'),
                      fg="#7209B7",
                      bg="#E7C6FF",
                      activeforeground="#7209B7",
                      activebackground="#E7C6FF",
                      state=ACTIVE)
other_button.pack(side=RIGHT)
other_button.place(x=800, y=460)


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
button.place(x=10, y=10)


window.mainloop()
