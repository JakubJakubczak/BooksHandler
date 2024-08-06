from tkinter import Menu, Label, Frame
def show_planning(frame):
    # Clear the content frame and display the planning section
    label = Label(frame, text="Planning:\n1. Reading Schedule\n2. Future Books to Read", font=("Arial", 14))
    label.pack(pady=20)