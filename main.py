#File main.py

#needs to use tkinter
import tkinter as tk
#imports from tkinter
from tkinter import messagebox
from tkinter import simpledialog

""" 
four things: 
Learning Goals
Track Skills
Log Daily Sessions
Add Notes or Journal
"""

class App:
    #Four Function App, the starting app for an eventual ai learning assistant and advisor
    
    #Constructor
    def __init__(self, root):
        #stores the main window object as an instance variable
        self.root = root
        #set the title of the main app window
        self.root.title("Learnflow Base")
        #set the inital dimensions of the window
        self.root.geometry("400x300")
        
        #create a main frame as a container for other widgets, with padding
        main_frame = tk.Frame(root, padx=20, pady=20)
        #pack geometry manager call to make the frame visible and fill the window
        main_frame.pack(expand=True, fill=tk.BOTH)

        #label widget to display text
        self.display_label = tk.Label(
            #specify parent widget
            main_frame,
            #initial display text
            text="This is a text example.",
            #font family and size
            font=("Arial", 14),
            #vertical padding in the label
            pady=10
        )
