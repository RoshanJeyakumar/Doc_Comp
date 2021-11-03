# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
import tkinter
from tkinter import *
import webbrowser
import os

# import filedialog module
from tkinter import filedialog

# Function for opening the
# file explorer window
def browseFiles1():
  global filepath1 
  filepath1 = tkinter.filedialog.askopenfilename(title="Open First PDF")
  print ("pdf1: "+filepath1+"\n")

def browseFiles2():
  global filepath2
  filepath2 = tkinter.filedialog.askopenfilename(title="Open Second PDF")
  print ("pdf2: "+filepath2+"\n")
  

def submit():
  cmdCommand = "WinMergeU" +" "+filepath1 +" " + filepath2 + " " + "-minimize" + " " +  "-noninteractive" + " " +  "-u" + " " + "-or" + " " + "C:/Users/User/Desktop/answer.htm"
  os.popen(cmdCommand)
  webbrowser.get().open('file://'+ 'C:/Users/User/Desktop/answer.htm' )
	
																							
# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,text = "File Comparison Tool",width = 100, height = 4,fg = "blue")

	
button_explore_1 = Button(window,text = "Choose File 1",command = browseFiles1)
button_explore_2 = Button(window,text = "Choose File 2",command = browseFiles2)
button_exit = Button(window,text = "Output",command = submit)
label_file_explorer.grid(column = 1, row = 1)

button_explore_1.grid(column = 1, row = 2)

button_explore_2.grid(column = 1,row = 3)

button_exit.grid(column = 1,row = 4)


# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns

# Let the window wait for any events
window.mainloop()
