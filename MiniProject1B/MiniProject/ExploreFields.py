from tkinter import *
from PIL import ImageTk, Image

#widget =GUI elements: button, textboxes,labels, images
#windows= serves as a comtainer to hold or contain these widgets

window = Tk() #instantiate an instance of a window
window.geometry("1000x650")
window.title("Prodigy's Pursuit- Explore Fields")

logo = PhotoImage(file='Grand Logo.png')
window.iconphoto(True,logo)
window.config(background="#E7C6FF")

window.geometry("1000x650")
img = ImageTk.PhotoImage(Image.open("ExploreFields.png"))
label = Label(window,image = img )
label.pack()
label.place(x=0,y=0)



#label = an area widget that holds text and/or an image within a window

label = Label(window,
              text="Explore Fields",
              font=('Grand Royal',32),
              fg='#7209B7',
              bg='#E7C6FF')
label.pack()
label.place(x=10,y=10)


window.mainloop() #place window on computer screen, lister for events

