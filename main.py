import tkinter as tk
from tkinter import Menu, Label, Frame
import constraints
import books
import goals
import habits
import analyse
import planning


def clear_content(frame):
    # Clear the content frame
    for widget in frame.winfo_children():
        widget.destroy()

def on_click_menu_item(item):
    clear_content(content_frame)

    if item == "List of books":
        books.show_books(content_frame)
    elif item == "Planning":
        planning.show_planning(content_frame)
    elif item == "Habits":
        habits.show_habits(content_frame)
    elif item == "Goals":
        goals.show_goals(content_frame)
    elif item == "Analysis":
        analyse.show_analyse(content_frame)
    else:
        clear_content(content_frame)

if __name__ == '__main__':
    # Create the main window
    root = tk.Tk()
    root.title("Books Handler")

    # Set the window size
    root.geometry("1000x700")  # Width x Height

    # Create a frame for the custom menu
    menu_frame = tk.Frame(root, bg=constraints.menu_bg_color)
    menu_frame.pack(side="top", fill="x")

    # Add menu items as labels
    menu_items = ["List of books", "Habits", "Goals", "Planning", "Analysis"]

    # Add menu labels with buttons and visual effects
    for itemm in menu_items:
        lbl = tk.Label(menu_frame, text=itemm, font=("Helvetica", 14), fg=constraints.font_color, bg=constraints.menu_bg_color,
                       padx=20, pady=10, cursor="hand2")
        lbl.pack(side="left")
        lbl.bind("<Button-1>", lambda e, item=itemm: on_click_menu_item(item))
        lbl.bind("<Enter>", lambda e: e.widget.config(fg="#007bff"))
        lbl.bind("<Leave>", lambda e: e.widget.config(fg=constraints.font_color))

    # Main content area
    content_frame = tk.Frame(root, bg=constraints.content_bg_color)
    content_frame.pack(fill="both", expand=True)

    # Initial welcome message
    welcome_label = tk.Label(content_frame, text="Welcome to your Book Manager!", font=("Helvetica", 18, "bold"), bg=constraints.content_bg_color, fg=constraints.font_color)
    welcome_label.pack(pady=20)

    # Run the main loop
    root.mainloop()

