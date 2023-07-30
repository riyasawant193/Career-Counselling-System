# Import necessary packages/libraries
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import pymysql
from tkinter import messagebox

# Create a window/instantiate an instance of a window
window = Tk()  # instantiate an instance of a window
window.geometry("1000x650")
window.title("Prodigy's Pursuit")
logo = PhotoImage(file='Grand Logo.png')
window.iconphoto(True, logo)
window.config(background="#E7C6FF")

# Create a canvas to display questions and options
canvas = Canvas(window, height=500, width=800, bg='white')
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Add the background image
background_image = PhotoImage(file='Assessment webpage.png')
canvas.create_image(0, 0, image=background_image, anchor=NW)

# Create a scrollbar for the canvas
scrollbar = Scrollbar(window, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.config(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox('all')))

# Fetch the questions and radio buttons stored in the database

# Connect to MySQL database
db = pymysql.connect(
    host="localhost",
    user="root",
    password="Hellojavashit69",
    database="prodigyspursuit"
)

# Create cursor object
cursor = db.cursor()

# Get the questions and options from the database
query = "SELECT question,option1,option2,option3,option4 FROM questions"
cursor.execute(query)
questions = cursor.fetchall()

# Create a label and entry widget for username
username_label = Label(canvas, text="Enter username:", font=('Arial', 16))
canvas.create_window(400, 60 * 130 + 40, anchor=CENTER, window=username_label)
username_entry = Entry(canvas, font=('Arial', 16))
canvas.create_window(650, 60 * 130 + 40, anchor=CENTER, window=username_entry)


def submit_test():
    # Check if all questions have been attempted
    if None in selected_options:
        messagebox.showerror("Error", "Please attempt all questions before submitting the test.")
        return

    # Get the username entered by the user
    username = username_entry.get()

    # Check if the username exists in the signup table
    query = f"SELECT Username FROM signup WHERE Username='{username}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if not result:
        messagebox.showerror("Error", "Username does not exist.")
    else:
        # Calculate the score for each field of technology
        scores = [0] * 15
        for i, question in enumerate(questions):
            # Get the correct answer from the database
            query = f"SELECT answers FROM questions WHERE qno={i + 1}"
            cursor.execute(query)
            correct_answer = cursor.fetchone()

            # Check if the user's answer matches the correct answer
            if selected_options[i] == correct_answer:
                scores[field - 1] += 2

        # Store the scores in the user_scores table
        query = "INSERT INTO user_scores (username, frontend_dev, backend_dev, data_science, artificial_intel, devops, machine_learn, cloud_compute, fullstack_dev, ui_developer, software, cyber_security, computer_graphics, android_dev, nlp, big_data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (username,) + tuple(scores)
        cursor.execute(query, values)
        db.commit()

        messagebox.showinfo("Success", "Test submitted successfully.")


# Create a submit button at the end of the canvas
submit_button = Button(window, text="Submit", font=('Arial', 16), command=submit_test)
canvas.create_window(400, 60 * 130 + 100, anchor=CENTER, window=submit_button)

# Create a list to store the selected options for each question
selected_options = []


def select_option(question_num, option_num):
    selected_options[question_num] = option_num

    # Store user's selection in the database
    query = "INSERT INTO user_responses (qno, question, response) VALUES ( %s, %s, %s)"
    values = (question_num + 1, option_num)
    cursor.execute(query, values)
    db.commit()

    # Calculate the score
    score = 0
    for i, question in enumerate(questions):
        # Get the correct answer from the database
        query = f"SELECT answer FROM questions WHERE qno={i + 1}"
        cursor.execute(query)
        correct_answer = cursor.fetchone()[0]

        # Check if the user's answer matches the correct answer
        if selected_options[i] == correct_answer:
            score += 1


# Loop through each question and create a set of radio buttons for each option
for i, question in enumerate(questions):
    # Create a frame for the question and option widgets
    question_frame = tk.Frame(canvas, bg='white')
    canvas.create_window(70, 150 * i, anchor=NW, window=question_frame)

    # Create a label for the question
    question_label = tk.Label(question_frame, text=question[0])
    question_label.grid(row=0, column=0)

    # Create a tk.IntVar() variable for this question
    question_var = tk.IntVar()

    # Create a set of radio buttons for each option
    for j in range(4):
        option_button = tk.Radiobutton(question_frame, text=question[j + 1], variable=question_var, value=j + 1,
                                       command=lambda question_num=i, option_num=j + 1: select_option(question_num,
                                                                                                      option_num))
        option_button.grid(row=j + 1, column=0, sticky=W)

    # Set the initial selected option for this question to 0
    selected_options.append(None)

    # Add the tk.IntVar() variable for this question to the list
    selected_options.append(question_var)

window.mainloop()
