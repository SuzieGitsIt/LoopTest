# File:     TkinterGUI_2023-03-24
# Version:  0.0.01
# Author:   Susan Haynes
# Comments/Notes: 
#   (0,0) coordinates are the top left corner of the screen for 1920x1080
#   (0,0) coordinates are the bottom right corner of the screen for 1919x1079
# Online References: 
#   https://pypi.org/project/PyAutoGUI/
#   https://pyautogui.readthedocs.io/en/latest/mouse.html
# Revision History: N/A 
# To check tkinter is installed, use this in command promt.
# python -m tkinter 

import tkinter as tk                                    # Tkinter's Tk class
import tkinter.ttk as ttk                               # Tkinter's Tkk class
import datetime as dt
import time
from PIL import ImageTk, Image
from tkinter import messagebox
from random import shuffle
from enum import global_flag_repr
from functools import partial

GUI = tk.Tk()
GUI.title("LAL Measurement")
GUI.geometry("1000x700")                                # Set the geometry of Tkinter frame
GUI.configure(bg = 'white')                             # Set background color
GUI.option_add("*Font", "Helvetica 12 bold")            # set the font and size for entire gui
GUI.option_add("*fg", "black")                          # set the text color, hex works too "#FFFFFF"
GUI.option_add("*bg", "white")                          # set the background color to white

def resize_image(event):
    new_width = event.width
    new_height = event.height
    background_image = copy_of_image.resize((new_width, new_height))
    bkgnd_img = ImageTk.PhotoImage(background_image)
    lbl_photo.config(image = bkgnd_img)
    lbl_photo.background_image = bkgnd_img #avoid garbage collection

background_image = Image.open(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\TkinterGUI_2023-03-24\LAL.png")
copy_of_image = background_image.copy()
bkgnd_img = ImageTk.PhotoImage(background_image)

lbl_photo = ttk.Label(GUI, image = bkgnd_img)
lbl_photo.bind('<Configure>', resize_image)
lbl_photo.pack(fill=tk.BOTH, expand = True)

# Python is serial, so each widget will output in order placed below;

################################################         TODAYS DATE (AUTOFILL)           ################################################   
date = dt.datetime.now()

lbl_cmd_date = tk.Label(                                # set the constant output text command to the user with instructions
    text="Today's Date is:",                            # set text for the operator to read
    bg = "WHITE",                                       # set the background color, hex works too "#FFFFFF"
    width = 12,                                         # set the width of text box, measured in text units '0'. 50 = 50 zeros wide
    height= 1                                           # if height is 1, then no need to call it out.
) 
lbl_cmd_date.place(x=50,y=50)  

lbl_out_date = tk.Label(                                # Initialize a Label to display the User Input
    GUI, 
    text =f"{date:%B, %d, %Y}", 
    bg = "white",                                     
    width= 15                                          # Longest month spelling is September, this width accounts for that.
)
lbl_out_date.place(x=300, y=50)

################################################                    INITIALS                ################################################ 
lbl_command_cred = tk.Label(                            # set the constant output text command to the user with instructions
    text="Enter Operator Credentials:",   
    bg = "WHITE",                                     
    width = 20                                         
) 
lbl_command_cred.place(x=50,y=100)  

entry_cred = tk.Entry(                                  # Create an Entry widget to accept User Input
    GUI,
    bg = "WHITE",
    width= 10
)
entry_cred.focus_set()
entry_cred.place(x=300,y=100)  

# Display the inputs as outputs
# Initials
lbl_disp_cred = tk.Label(                               # Initialize a Label to display the User Input
    GUI, 
    text="Initials:",
    bg = "white",
    width= 7
)
lbl_disp_cred.place(x=45, y=450)

lbl_out_cred = tk.Label(                                # Initialize a Label to display the User Input
    GUI, 
    text = "", 
    bg = "white",
    width= 3
)
lbl_out_cred.place(x=300, y=450)

def display_cred():                                     # Display user input
   global entry
   credentials = entry_cred.get()
   lbl_out_cred.configure(text = credentials)

# Button when finished to display the outputs
btn_cred = tk.Button(GUI, text="Confirm",bg = "grey", width= 10,command = display_cred).place(x=450,y=90)  

################################################           WORK ORDER NUMBER            ################################################   
lbl_command_WO = tk.Label(                                
    text="Enter Work Order Number:",   
    bg = "WHITE",                                                                             
    width = 20                                         
) 
lbl_command_WO.place(x=50,y=150)  

entry_WO = tk.Entry(                                       
    GUI,
    bg = "WHITE",
    width= 10
)
entry_WO.place(x=300,y=150)  

lbl_disp_WO = tk.Label(               
    GUI, 
    text="Work Order Number:",
    bg = "white",                                  
    width= 16
)
lbl_disp_WO.place(x=50, y=500)

lbl_out_WO = tk.Label(                                
    GUI, 
    text = "", 
    bg = "white",                                  
    width= 10
)
lbl_out_WO.place(x=300, y=500)

def display_WO():                        
   global entry
   WO = entry_WO.get()
   lbl_out_WO.configure(text = WO)

btn_WO = tk.Button(       
    GUI, 
    text="Confirm",
    bg = "grey",
    width= 10,
    command = display_WO
).place(x=450,y=140)  

################################################             SAMPLE SIZE              ################################################   
lbl_command_samp = tk.Label(                                
    text="Enter Sample Size:",   
    bg = "WHITE",                                                                            
    width = 15                                         
) 
lbl_command_samp.place(x=50,y=200)  

entry_samp = tk.Entry(                                       
    GUI,
    bg = "WHITE",
    width= 10
)
entry_samp.place(x=300,y=200)  

lbl_disp_samp = tk.Label(               
    GUI, 
    text="Sample Size:",
    bg = "white",                                
    width= 10
)
lbl_disp_samp.place(x=50, y=550)

lbl_out_samp = tk.Label(                                
    GUI, 
    text = "", 
    bg = "white",                                    
    width= 3
)
lbl_out_samp.place(x=300, y=550)

def display_samp():                        
   global entry
   samp = entry_samp.get()
   lbl_out_samp.configure(text = samp)

btn_samp = tk.Button(       
    GUI, 
    text="Confirm",
    bg = "grey",
    width= 10,
    command = display_samp
).place(x=450,y=190)  

'''
################################################         015 OR 040 MEASUREMENTS           ################################################   
# MEASUREMENT SIZE WIDGET BUTTONS
lbl_cmd_meas = tk.Label(text="Select Measurement Size:",    bg= "white", width= 20).place(x=50,y=250)  
lbl_disp_meas = tk.Label(GUI, text="Measurement Size:",  bg= "white", width= 15).place(x=50, y=600)
lbl_out_samp = tk.Label(GUI, text= "", bg= "white", width= 3) .place(x=300, y=550)
def display_015_040(text):
   disp_meas = tk.Entry(GUI, width= 3)
   disp_meas.insert(0,text)
   disp_meas.place(x=300, y=600)
   print(text)
btn_015  = tk.Button(GUI, text= "015", bg= "grey", width= 5, command=partial(display_015_040,"015")).place(x=300,y=250) 
btn_040  = tk.Button(GUI, text= "040", bg= "grey", width= 5, command=partial(display_015_040,"040")).place(x=400,y=250)
'''
""" NEEDS WORK, nothing happens when button is clicked.
################################################        RANDOM PINK BUTTON         ################################################   
colors = ['#FF69B4']

def rand_pink():
    randomized = []
    for i in range (3):
        randomized.append(random.choice(colors))

but_pink = tk.Button(
    GUI,          
    text="Click Me",  
    bg = colors,
    width= 7,
    command=rand_pink
).place(x=750,y=630)
"""

################################################             EXIT BUTTON             ################################################   
def exit_application():
    msg_box = tk.messagebox.askquestion('Exit', 'Are you sure you want to exit the application?', icon='warning')
    if msg_box == 'yes':
        GUI.destroy()
    else:
        tk.messagebox.showinfo('Exit', 'Thanks for staying, please continue.')

but_exit = tk.Button(
    GUI,          
    text="Exit",                            
    bg = "grey",
    width= 5,
    command=exit_application
).place(x=900,y=630)

GUI.mainloop()                                  # Must be at the end of the program in order for the application to run b/c windows is constantly updating
