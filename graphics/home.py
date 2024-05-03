import tkinter as tk
from tkinter import ttk

def start_window(function_to_perform):
# Define colors
    bg_color = "#2c3e50"
    fg_color = "#ecf0f1"
    button_color = "#2980b9"

    # Create the main application window
    root = tk.Tk()
    root.title("Jarvis GUI")
    root.geometry("400x300")
    root.configure(bg=bg_color)

    # Create a label with Jarvis-style font and color
    label = ttk.Label(root, text="Jarvis GUI", font=("Helvetica", 24, "bold"), foreground=fg_color, background=bg_color)
    label.pack(pady=20)

    # Create a button with Jarvis-style colors and font
    button = ttk.Button(root, text="Run Main Function", command=function_to_perform, style="TButton", width=20)
    button.pack(pady=10)
    # Define a custom style for the button
    style = ttk.Style()
    style.configure("TButton", foreground=fg_color, background=button_color, font=("Helvetica", 12, "bold"))

    # Run the GUI event loop
    root.mainloop()
