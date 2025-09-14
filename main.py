#File main.py

"""
Learnflow Base - Personal Learning Tracker
Author: Matt Lindborg
Course: MS5548 - Advanced Programming Concepts and Ai
Assignment: Week 1 Python GUI
Date: 9/13/2025

Purpose:
This application provides a simple personal learning tracker that allows
the user to manage learning goals, track skills, log daily sessions,
and add notes or reflections. The program is event-driven, using buttons
to trigger user input popups and update a display area. It also includes
an Exit option and a Clear option to reset the tracker. This makes the
application purposeful, not just a GUI demo, and helps users maintain
structure in their ongoing education.
"""

#imports from tkinter
import tkinter as tk
from tkinter import messagebox

class App:
    
    """
    Constructor
    """
    def __init__(self, root):
        # save the main window object as part of this class
        self.root = root
        
        # set the window title text shown in the top bar
        self.root.title("Learnflow Base")

        # disable resizing so the user cannot stretch the window
        self.root.resizable(False, False)
        
        # dictionary to store the text entries for each feature
        self.entries = {"Goal": "", "Skill": "", "Session": "", "Notes": ""}
        
        # create the main container frame that holds everything
        main_frame = tk.Frame(root, padx=10, pady=10)   # add padding around edges
        main_frame.grid(row=0, column=0, sticky="nsew") # place frame into grid
        
        # allow the single column to expand with content
        main_frame.columnconfigure(0, weight=1)
        
        """ ----------------- TOP ROW: LABEL + EXIT BUTTON ----------------- """
        
        # frame that will hold both the welcome label (left) and the exit button (right)
        top_frame = tk.Frame(main_frame)                # new frame from parent frame
        top_frame.grid(row=0, column=0, sticky="ew")    # expand horizontally
        
        # make first column of top_frame stretch
        top_frame.columnconfigure(0, weight=1)
        
        # create a welcome label widget
        self.display_label = tk.Label(
            top_frame,                              # parent frame
            text="Welcome to Learnflow\nPlease choose an option",  # label text
            font=("Arial", 12),                     # font type and size
            pady=2,                                 # vertical padding inside widget
            justify="left"                          # align text to left
        )
        # position the label on the left side
        self.display_label.grid(row=0, column=0, sticky="w")
        
        # create an exit button widget
        self.quit_button = tk.Button(
            top_frame,          # parent frame
            text="Exit",        # text shown on button
            width=6,            # button width
            command=self.root.quit  # action: close the app
        )
        # place exit button on right side of same row
        self.quit_button.grid(row=0, column=1, sticky="e")

        # create a clear button widget
        self.clear_button = tk.Button(
            top_frame,          # parent frame
            text="Clear",       # text shown on button
            width=7,            # button width
            command=self.clear_entries  # action: clear data entries
        )
        # place clear button before exit button on same row
        self.clear_button.grid(row=0, column=1, sticky="e", padx=(0,63))
        
        """ ----------------- MIDDLE ROW: BUTTONS + IMAGE ----------------- """
        
        # frame to hold both the vertical button stack and the image
        side_frame = tk.Frame(main_frame)              # new frame from parent frame
        side_frame.grid(row=1, column=0, sticky="w")   # anchor to left
        
        # sub-frame for vertical button stack
        buttons_frame = tk.Frame(side_frame)           # new frame from parent frame
        buttons_frame.pack(side="left", anchor="n", padx=(0,5))  # small gap to image
        
        # create "Goal" button
        self.goal_button = tk.Button(
            buttons_frame,                          # parent frame
            text="Goal",                            # text shown on button
            width=10,                               # button width
            command=lambda: self.add_or_edit_entry("Goal") # on click action
        )
        self.goal_button.pack(pady=2, anchor="w") # pack with small vertical gap
        
        # create "Skill" button
        self.skill_button = tk.Button(
            buttons_frame,                          # parent frame
            text="Skill",                           # text shown on button
            width=10,                               # button width
            command=lambda: self.add_or_edit_entry("Skill") # on click action
        )
        self.skill_button.pack(pady=2, anchor="w") # pack with small vertical gap
        
        # create "Session" button
        self.session_button = tk.Button(
            buttons_frame,                          # parent frame
            text="Session",                         # text shown on button
            width=10,                               # button width
            command=lambda: self.add_or_edit_entry("Session") # on click action
        )
        self.session_button.pack(pady=2, anchor="w") # pack with small vertical gap
        
        # create "Notes" button
        self.notes_button = tk.Button(
            buttons_frame,                          # parent frame
            text="Notes",                           # text shown on button
            width=10,                               # button width
            command=lambda: self.add_or_edit_entry("Notes") # on click action
        )
        self.notes_button.pack(pady=2, anchor="w") # pack with small vertical gap

        # load image file
        self.image = tk.PhotoImage(file="images\\image2_50pc.png")
        
        # create a label to display the image
        self.image_label = tk.Label(side_frame, image=self.image)
        
        # place image next to the button stack
        self.image_label.pack(side="left", anchor="n")
        
        """ ----------------- BOTTOM ROW: TEXT BOX ----------------- """
        
        # frame to hold text box and scrollbar
        output_frame = tk.Frame(main_frame) # new frame from parent frame
        output_frame.grid(row=2, column=0, sticky="ew", pady=10) # stretch horizontally
        
        # vertical scrollbar widget
        scrollbar = tk.Scrollbar(output_frame) # new frame from parent frame
        scrollbar.pack(side="right", fill="y") # attach to right edge
        
        # text widget for output (user entries)
        self.output_box = tk.Text(
            output_frame, 
            height=6,                # number of visible lines
            wrap="word",             # wrap long text at word boundaries
            state="disabled",        # read-only by default
            yscrollcommand=scrollbar.set # link scrollbar to text box
        )
        self.output_box.pack(side="left", fill="both", expand=True)  # fill available space
        
        # link scrollbar back to text widget
        scrollbar.config(command=self.output_box.yview)
        
        """ ----------------- AUTO-SIZE WINDOW ----------------- """
        
        # let Tkinter calculate the "natural size" of window from widgets
        self.root.update_idletasks()
        
        # get calculated width and height
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        
        # set the minimum size so window cannot shrink smaller than content
        self.root.minsize(w, h)

    """
    Methods
    """

    # custom popup input window
    def custom_input(self, title, prompt):
        # create a popup window

        popup = tk.Toplevel(self.root)
        popup.title(title)

         # desired popup size
        popup_width = 300
        popup_height = 150

        # make sure root window geometry info is current
        self.root.update_idletasks()

        # get main window position and size
        main_x = self.root.winfo_x()
        main_y = self.root.winfo_y()
        main_width = self.root.winfo_width()
        main_height = self.root.winfo_height()

        # calculate popup position:
        # centered horizontally, quarter way down vertically
        pos_x = main_x + (main_width // 2) - (popup_width // 2)
        pos_y = main_y + (main_height // 4) - (popup_height // 2)

        # apply popup geometry
        popup.geometry(f"{popup_width}x{popup_height}+{pos_x}+{pos_y}")

        # label for prompt
        label = tk.Label(
            popup,              # parent frame
            text=prompt,        # displayed text
            font=("Arial", 12)  # text font and size
            )
        label.pack(pady=10)     # display label

        # entry field for user input
        entry = tk.Entry(
            popup, # parent frame
            width=40 # width of text entry
            )
        entry.pack(pady=5)      # display field

        # focus cursor immediately
        entry.focus_set()

        # variable to store result
        result = {"value": None}

        # function when OK is pressed
        def on_ok(event=None):
            result["value"] = entry.get() # get the text entry
            popup.destroy()  # close popup

        # ok button
        ok_button = tk.Button(
            popup,          # parent frame
            text="OK",      # button text
            command=on_ok   # on click action
            ) 
        ok_button.pack(pady=10) # display button

        # bind Enter key for convenience
        popup.bind("<Return>", on_ok)

        # wait until popup is closed
        self.root.wait_window(popup)
        
        # method returns the result
        return result["value"]

    # method to clear all entries from the tracker
    def clear_entries(self):
        # loop to reset all stored values back to empty strings
        for key in self.entries:
            self.entries[key] = ""
        # refresh the output box to reflect cleared data
        self.update_output()
        # show confirmation popup
        messagebox.showinfo("Cleared", "All entries have been cleared.")

    # method to refresh the content of the output text box
    def update_output(self):
        # temporarily allow editing of the text box
        self.output_box.config(state="normal")  
        # clear previous contents
        self.output_box.delete("1.0", tk.END)   
        # loop to iterate over saved entries and display them
        for key, value in self.entries.items():
            if value:
                self.output_box.insert(tk.END, f"{key}: {value}\n") # insert text value for specific key
        # set text box back to read-only
        self.output_box.config(state="disabled")  

    # method to add or edit a text entry when a button is clicked
    def add_or_edit_entry(self, entry_type):
        # prompt user with custom input dialog
        text = self.custom_input("Input", f"Enter your {entry_type}:")
        # if user entered something
        if text:
            # save entry to dictionary
            self.entries[entry_type] = text  
            # update the text box display
            self.update_output()             
    
""" MAIN PROGRAM LOOP """

# python construct to check if script is being run directly
if __name__== "__main__":
    #create the main tkinter window object
    root_window = tk.Tk()
    #create an instance of the App class, passing the window to it
    app_instance = App(root_window)
    #Tkinter event loop, listening for events and keeping the GUI running
    root_window.mainloop()
