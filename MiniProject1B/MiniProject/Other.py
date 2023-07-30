from tkinter import *
from PIL import ImageTk, Image
import subprocess

# widget =GUI elements: button, textboxes,labels, images
# windows= serves as a comtainer to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry("1000x650")
window.title("Prodigy's Pursuit- Other")

logo = PhotoImage(file='Grand Logo.png')
window.iconphoto(True, logo)
window.config(background="#E7C6FF")

window.geometry("1000x650")
img = ImageTk.PhotoImage(Image.open("Other Features.png"))
label = Label(window, image=img)
label.pack()
label.place(x=0, y=0)


def click():
    print("You clicked the button")


button = Button(window,
                text="Schedule Maker",
                command=click,
                font=("Montserrat Light", 15),
                fg="#e5b3fe",
                bg="#7b2cbf",
                activeforeground="#e5b3fe",
                activebackground="#7209B7",
                state=ACTIVE)
button.pack()
button.place(x=120, y=180)


button = Button(window,
                text="Todo",
                command=click,
                font=("Montserrat Light", 15),
                fg="#e5b3fe",
                bg="#7b2cbf",
                activeforeground="#e5b3fe",
                activebackground="#7209B7",
                state=ACTIVE)
button.pack()
button.place(x=120, y=428)


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

window.mainloop()  # place window on computer screen, lister for events
