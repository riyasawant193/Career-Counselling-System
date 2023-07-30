from tkinter import *
from PIL import ImageTk, Image
import subprocess

# widget =GUI elements: button, textboxes,labels, images
# windows= serves as a comtainer to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry("1000x650")
window.title("Prodigy's Pursuit- Take Assessment")

logo = PhotoImage(file='Grand Logo.png')
window.iconphoto(True, logo)
window.config(background="#E7C6FF")

window.geometry("1000x650")
img = ImageTk.PhotoImage(Image.open("Take Assessment.jpg"))
label = Label(window, image=img)
label.pack()
label.place(x=0, y=0)

# label = an area widget that holds text and/or an image within a window

label = Label(window,
              text="Appraisal Evaluation",
              font=('Grand Royal', 32),
              fg='#7209B7',
              bg='#d4d2fe')
label.pack()
label.place(x=500, y=100)

label = Label(window,
              text="Looking to test your engineering skills and find out what \nyou're good at?Look no further than "
                   "our engineering\n assessment test is here to guide oy through",
              justify="left",
              font=('Cambria', 15),
              fg='#7209B7',
              bg='#d4d2fe')
label.pack()
label.place(x=500, y=200)

label = Label(window,
              text="This assessment test is designed to\n evaluate your proficiency in the field of \n "
                   "technology. After completing the assessment,\nyou'll receive a graphical analysis outlining your "
                   "\nperformance and identifying areas where you excel.",
              justify="left",
              font=('Cambria', 15),
              fg='#7209B7',
              bg='#d4d2fe')
label.pack()
label.place(x=500, y=280)


def click():
    # Close the current file
    window.destroy()
    # Open the new file
    subprocess.Popen(["python", "AssessmentPage.py"])


button = Button(window,
                text="Take Assessment",
                command=click,
                font=("Jacques Francois", 20),
                fg="#E7C6FF",
                bg="#F72585",
                activeforeground="#E7C6FF",
                activebackground="#7209B7",
                state=ACTIVE)
button.pack()
button.place(x=600, y=450)


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
