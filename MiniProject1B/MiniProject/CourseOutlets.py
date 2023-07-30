from tkinter import *
from tkinter import ttk
import webbrowser
from PIL import ImageTk, Image


def open_link(link):
    webbrowser.open_new_tab(link)


# create a window
window = Tk()
window.geometry("1000x650")
window.title("Prodigy's Pursuit- Course Outlets")
window.config(background="#E7C6FF")

# set the logo and icon
logo = PhotoImage(file='Grand Logo.png')
window.iconphoto(True, logo)

# set the Course Outlets image
img = ImageTk.PhotoImage(Image.open("Course Outlets.png"))
label = Label(window, image=img)
label.pack()
label.place(x=0, y=0)

# set the "Course Outlets" label
label = Label(window,
              text="Course Outlets",
              font=('Grand Royal', 32),
              fg='#7209B7',
              bg='#EFD5ED')
label.pack()
label.place(x=10, y=20)

# set the course description label
label = Label(window,
              text="Here are Top 5 courses you can use to grow academically",
              font=('Cambria', 20),
              fg='#7209B7',
              bg='#EFD5ED')
label.pack()
label.place(x=10, y=100)

# set the MIT OpenCourseWare label with hyperlink
link = "https://ocw.mit.edu/"
label = Label(window,
              text="(1) MIT OpenCourseWare",
              font=('Cambria', 16),
              fg='#7209B7',
              bg='#EFD5ED',
              cursor="hand2")
label.pack()
label.place(x=10, y=180)
label.bind("<Button-1>", lambda e: open_link(link))

# set the Coursera label with hyperlink
link = "https://www.coursera.org/"
label = Label(window,
              text="(2) Coursera",
              font=('Cambria', 16),
              fg='#7209B7',
              bg='#EFD5ED',
              cursor="hand2")
label.pack()
label.place(x=10, y=240)
label.bind("<Button-1>", lambda e: open_link(link))

# set the edX label with hyperlink
link = "https://www.edx.org/"
label = Label(window,
              text="(3) edX",
              font=('Cambria', 16),
              fg='#7209B7',
              bg='#EFD5ED',
              cursor="hand2")
label.pack()
label.place(x=10, y=300)
label.bind("<Button-1>", lambda e: open_link(link))

# set the Udacity label with hyperlink
link = "https://www.udacity.com/"
label = Label(window,
              text="(4) Udacity",
              font=('Cambria', 16),
              fg='#7209B7',
              bg='#EFD5ED',
              cursor="hand2")
label.pack()
label.place(x=10, y=360)
label.bind("<Button-1>", lambda e: open_link(link))

# set the Udemy label with hyperlink
link = "https://www.udemy.com/"
label = Label(window,
              text="(5) Udemy",
              font=('Cambria', 16),
              fg='#7209B7',
              bg='#FFFFFF',
              cursor="hand2")
label.pack()
label.place(x=10, y=420)
label.bind("<Button-1>", lambda e: open_link(link))

# run the window
window.mainloop()
