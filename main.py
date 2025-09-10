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
    
    """
    Constructor
    """
    def __init__(self, root):
        #stores the main window object as an instance variable
        self.root = root
        #set the title of the main app window
        self.root.title("Learnflow Base")
        #set the inital dimensions of the window
        self.root.geometry("400x200")
        
        #create a main frame as a container for other widgets, with padding
        main_frame = tk.Frame(root, padx=10, pady=10)
        #grid geometry manager call to make the frame visible and fill the window
        main_frame.grid(row=0, column=0, sticky="nsew")

        """
        Widgets
        """

        """Labels"""
        
        #label widget to display text
        self.display_label = tk.Label(
            #specify parent widget
            main_frame,
            #initial display text
            text="Welcome to Learnflow\nChoose an option below",
            #font family and size
            font=("Arial", 12),
            #vertical padding in the label
            pady=2,
            #center text
            justify="center"
        )
        #use grid to make the label visible, fill the column span, and add vertical padding
        self.display_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        """Buttons"""

        self.goal_button = tk.Button(
            main_frame, 
            text="Goal", 
            width=10, 
            command=self.add_learning_goal)
        
        self.skill_button = tk.Button(
            main_frame, 
            text="Skill", 
            width=10, 
            command=self.track_skill)
        
        self.session_button = tk.Button(
            main_frame, 
            text="Session", 
            width=10, 
            command=self.log_session)
        
        self.notes_button = tk.Button(
            main_frame, 
            text="Note", 
            width=10, 
            command=self.add_notes)
        
        self.quit_button = tk.Button(
            main_frame, 
            text="Exit", 
            width=6, 
            command=self.root.quit)
        
        # Place buttons in a row using grid
        self.goal_button.grid(row=1, column=0, padx=4)
        self.skill_button.grid(row=1, column=1, padx=4)
        self.session_button.grid(row=1, column=2, padx=4)
        self.notes_button.grid(row=1, column=3, padx=4)
        self.quit_button.grid(row=0, column=3, padx=4)  # More space before Exit

        #button widget
        self.info_button = tk.Button(
            #specify parent widget
            main_frame,
            #text that appears on the button
            text="Example Button",
            #function called when button is clicked
            command=self.show_info_message
        )
        #use pack  to make the button visible, fill horizontal space, and add vertical padding
        #self.info_button.pack(fill=tk.X, pady=5)

    """
    Methods
    """

    #method to show the info message box
    def show_info_message(self):
        #informational message box
        messagebox.showinfo(
            #title of the message box window
            "This is some info",
            #message content
            "This is more info shown to the user.\nIt is very important"
            )
    
    def add_learning_goal(self):
        messagebox.showinfo(
            #title of the message box window
            "This is some info",
            #message content
            "This is more info shown to the user.\nIt is very important"
            )
        
    def track_skill(self):
        messagebox.showinfo(
            #title of the message box window
            "This is some info",
            #message content
            "This is more info shown to the user.\nIt is very important"
            )
        
    def log_session(self):
        messagebox.showinfo(
            #title of the message box window
            "This is some info",
            #message content
            "This is more info shown to the user.\nIt is very important"
            )
        
    def add_notes(self):
        messagebox.showinfo(
            #title of the message box window
            "This is some info",
            #message content
            "This is more info shown to the user.\nIt is very important"
            )
    
#python construct to check if script is being run directly
if __name__== "__main__":
    #main tkinter window object
    root_window = tk.Tk()
    #instance of the App class, passing main window to it
    app_instance = App(root_window)
    #Tkinter event loop, listening for events and keep the GUI running
    root_window.mainloop()
