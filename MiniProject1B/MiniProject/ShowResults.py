from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import pymysql

# widget =GUI elements: button, textboxes,labels, images
# windows= serves as a container to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry("1000x650")
window.title("Prodigy's Pursuit- Show Results")
window.geometry("1000x650")
img = ImageTk.PhotoImage(Image.open("Showresults.png"))
label = Label(window, image=img)
label.pack()
label.place(x=0, y=0)

label = Label(window,
              text="USERNAME:",
              font=('Grand Royal', 32),
              fg='black',
              bg='#A3B18A')
label.pack()
label.place(x=270, y=230)

entry = Entry()
entry.config(font=('Jacques Francois', 20))  # change font
entry.config(bg='#F8BBD5')  # background
entry.config(fg='black')  # foreground
entry.config(width=10)
entry.pack()
entry.place(x=550, y=230)

# Connect to MySQL database
db = pymysql.connect(
    host="localhost",
    user="root",
    password="Hellojavashit69",
    database="prodigyspursuit"
)

# Create cursor object
cursor = db.cursor()

# Define the field names and maximum scores
fields = ['Frontend \n Developer', 'Backend \n Developer', 'Data Science', 'Artificial \n Intelligence', 'DevOps', 'Machine \n Learning', 'Cloud \n Computing', 'Full Stack \n Developer', 'UI Developer', 'Software \n Developer', 'Cyber \n Security', 'Computer \n Graphics', 'Android \n Developer', 'Natural Language \n Processing', 'Big Data \n Engineering']
max_scores = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]


def on_button_click():
    # Get the entered username
    username = entry.get()

    # Check if the user has taken the test
    query = f"SELECT * FROM user_scores WHERE username='{username}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result is None:
        messagebox.showerror("Error", "This user has not taken the test yet.")
        return

    # Extract the scores from the result
    user_scores = list(result)[1:]

    # Compute the angles of the vertices of the inner pentagon
    angles = np.linspace(0, 2 * np.pi, len(fields), endpoint=False)

    # Plot the outer pentagon
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)
    ax.plot(np.concatenate((angles, [angles[0]])), np.concatenate((max_scores, [max_scores[0]])), 'k-', linewidth=1)

    # Plot the inner pentagon
    ax.plot(np.concatenate((angles, [angles[0]])), np.concatenate((user_scores, [user_scores[0]])), 'r-', linewidth=2)

    # Fill in the area between the pentagons
    ax.fill(np.concatenate((angles, [angles[0]])), np.concatenate((user_scores, [user_scores[0]])), alpha=0.3)

    # Set the labels for each field
    ax.set_thetagrids(angles * 180 / np.pi, fields)

    # Set the range of the radial axis
    ax.set_ylim(0, 10)

    # Add a title to the chart
    plt.title('Radar chart representing your interest in respective field of technology')

    # Show the chart
    plt.show()


viewresult_button = Button(window,
                           text="VIEW RESULT",
                           command=on_button_click,
                           font=("Jacques Francois", 15),
                           fg="#F72585",
                           bg="#E7C6FF",
                           state=ACTIVE)
viewresult_button.pack(side=RIGHT)
viewresult_button.place(x=550, y=380)

window.mainloop()
