import tkinter as tk
from tkinter import Menu, Label, Frame
from tkinter import ttk


#Constaints:

menu_bg_color = "#00009f"
content_bg_color = "#00005f"
font_color = "#ffffff"
def show_books():
    # Clear the content frame and display the list of books
    clear_content()
    label = Label(content_frame, text="List of Books:\n1. Book One\n2. Book Two\n3. Book Three", font=("Arial", 14))
    label.pack(pady=20)

def show_habits():
    # Clear the content frame and display the list of books
    clear_content()
    label = Label(content_frame, text="habits", font=("Arial", 14))
    label.pack(pady=20)

def show_analyse():
    # Clear the content frame and display the list of books
    clear_content()
    label = Label(content_frame, text="analyse", font=("Arial", 14))
    label.pack(pady=20)

def show_goals():
    # Clear the content frame and display the list of books
    clear_content()
    label = Label(content_frame, text="goals", font=("Arial", 14))
    label.pack(pady=20)
def show_planning():
    # Clear the content frame and display the planning section
    clear_content()
    label = Label(content_frame, text="Planning:\n1. Reading Schedule\n2. Future Books to Read", font=("Arial", 14))
    label.pack(pady=20)

def clear_content():
    # Clear the content frame
    for widget in content_frame.winfo_children():
        widget.destroy()

def on_click_menu_item(item):
    # selected_item.set(item)
    if item == "List of books":
        show_books()
    elif item == "Planning":
        show_planning()
    elif item == "Habits":
        show_habits()
    elif item == "Goals":
        show_goals()
    elif item == "Analysis":
        show_analyse()
    else:
        clear_content()

if __name__ == '__main__':
    # Create the main window
    root = tk.Tk()
    root.title("Books Handler")

    # Set the window size
    root.geometry("1000x700")  # Width x Height

    # Create a frame for the custom menu
    menu_frame = tk.Frame(root, bg=menu_bg_color)
    menu_frame.pack(side="top", fill="x")

    # Add menu items as labels
    menu_items = ["List of books", "Habits", "Goals", "Planning", "Analysis"]
    # selected_item = tk.StringVar()

    # Add menu labels with buttons and visual effects
    for itemm in menu_items:
        lbl = tk.Label(menu_frame, text=itemm, font=("Helvetica", 14), fg=font_color, bg=menu_bg_color,
                       padx=20, pady=10, cursor="hand2")
        lbl.pack(side="left")
        lbl.bind("<Button-1>", lambda e, item=itemm: on_click_menu_item(item))
        lbl.bind("<Enter>", lambda e: e.widget.config(fg="#007bff"))
        lbl.bind("<Leave>", lambda e: e.widget.config(fg=font_color))

    # Main content area
    content_frame = tk.Frame(root, bg=content_bg_color)
    content_frame.pack(fill="both", expand=True)

    # Initial welcome message
    welcome_label = tk.Label(content_frame, text="Welcome to your Book Manager!", font=("Helvetica", 18, "bold"), bg=content_bg_color, fg=font_color)
    welcome_label.pack(pady=20)

    # Run the main loop
    root.mainloop()

