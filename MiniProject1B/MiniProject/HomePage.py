from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import subprocess


# widget =GUI elements: button, textboxes,labels, images
# windows= serves as a container to hold or contain these widgets


root = tk.Tk()
root.geometry("1000x650")
root.title("Prodigy's Pursuit")

logo = PhotoImage(file='Grand Logo.png')
root.iconphoto(True, logo)
root.config(background="#E7C6FF")

img = ImageTk.PhotoImage(Image.open("Prodigy's Pursuit.png"))
label = Label(root, image=img)
label.pack()
label.place(x=0, y=0)

# label = an area widget that holds text and/or an image within a window
# button = you click it, then it does stuff


def on_button_click():
    # Close the current file
    root.destroy()
    # Open the new file
    subprocess.Popen(["python", "SignUp.py"])


button = Button(root,
                text="Get Started",
                command=on_button_click,
                font=("Jacques Francois", 15),
                fg="#E7C6FF",
                bg="#F72585",
                activeforeground="#7209B7",
                activebackground="#E7C6FF",
                state=ACTIVE)
button.pack()
button.place(x=112, y=565)


def on_button_click():
    # Close the current file
    root.destroy()
    # Open the new file
    subprocess.Popen(["python", "ContactUs.py"])


button3 = Button(root,
                 text="CONTACT US",
                 command=on_button_click,
                 font=("Jacques Francois", 10),
                 fg="#3A0CA3",
                 bg="#E7C6FF",
                 activeforeground="#3A0CA3",
                 activebackground="#E7C6FF",
                 state=ACTIVE)
button3.pack()
button3.place(x=818, y=26)


def on_button_click():
    # Close the current file
    root.destroy()
    # Open the new file
    subprocess.Popen(["python", "About.py"])


button4 = Button(root,
                 text="ABOUT",
                 command=on_button_click,
                 font=("Jacques Francois", 10),
                 fg="#3A0CA3",
                 bg="#E7C6FF",
                 activeforeground="#3A0CA3",
                 activebackground="#E7C6FF",
                 state=ACTIVE)
button4.pack()
button4.place(x=727, y=26)


def on_button_click():
    # Close the current file
    root.destroy()
    # Open the new file
    subprocess.Popen(["python", "SignIn.py"])


button5 = Button(root,
                 text="SIGN IN",
                 command=on_button_click,
                 font=("Jacques Francois", 10),
                 fg="#3A0CA3",
                 bg="#E7C6FF",
                 activeforeground="#3A0CA3",
                 activebackground="#E7C6FF",
                 state=ACTIVE)
button5.pack()
button5.place(x=642, y=26)

count = 0


def click():
    print("You clicked the button")


button6 = Button(root,
                 text="HOME",
                 command=click,
                 font=("Jacques Francois", 10),
                 fg="#3A0CA3",
                 bg="#E7C6FF",
                 activeforeground="#3A0CA3",
                 activebackground="#E7C6FF",
                 state=ACTIVE)
button6.pack()
button6.place(x=559, y=26)

root.mainloop()  # place window on computer screen, lister for events
