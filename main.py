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
        #use pack to make the label visible and add vertical padding
        self.display_label.pack(pady=(0,20))

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
        self.info_button.pack(fill=tk.X, pady=5)

        #method to show the info message box
        def show_info_message(self):
            #informational message box
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
        root_window.mainloop
