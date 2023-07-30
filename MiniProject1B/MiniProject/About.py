from tkinter import *
from PIL import ImageTk, Image
import subprocess

# widget =GUI elements: button, textboxes,labels, images
# windows= serves as a container to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry("1000x650")
window.title("Prodigy's Pursuit")

logo = PhotoImage(file='Grand Logo.png')
window.iconphoto(True, logo)
window.config(background="#E7C6FF")

img = ImageTk.PhotoImage(Image.open("About.png"))
label = Label(window, image=img)
label.pack()
label.place(x=0, y=0)

label = Label(window,
              text="About",
              font=('Grand Royal', 22),
              fg='#3A0CA3',
              bg='#E5B3FE')
label.pack()
label.place(x=60, y=80)

label = Label(window,
              text="Prodigy's Pursuit",
              font=('Grand Royal', 32),
              fg='#3A0CA3',
              bg='#E5B3FE')
label.pack()
label.place(x=60, y=120)

label = Label(window,
              text="This career counselling platform for engineers is\n"
                   "designed to help users explore different engineering\n"
                   "career paths and make informed decisions about their\n"
                   "professional futures. It provides personalized career\n "
                   "guidance based on the user's qualifications, skills, and\n"
                   "interests, along with insights into the current job\n"
                   "market,educational resources, and networking \n"
                   "opportunities.Overall, it is a comprehensive \n"
                   "and user-friendly platform for engineers \n"
                   "to receive guidance and support \n"
                   "throughout their professional journeys.",
              justify="left",
              font=('Cambria', 12),
              fg='#3A0CA3',
              bg='#E5B3FE')
label.pack()
label.place(x="60", y=200)

submit_button = Button(window,
                       text="BACK",
                       font=("Jacques Francois", 15),
                       fg="#E7C6FF",
                       bg="#F72585",
                       activeforeground="#E7C6FF",
                       activebackground="#7209B7",
                       state=ACTIVE)
submit_button.pack(side=RIGHT)
submit_button.place(x=60, y=453)


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

window.mainloop()
