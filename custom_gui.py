# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
import Tkinter
from Tkinter import *
import webbrowser
import os
from PIL import ImageTk,Image

# import filedialog module
import tkFileDialog

# Function for opening the
# file explorer window
def browseFiles1():
  global filepath1 
  filepath1 = tkFileDialog.askopenfilename(title="Open First File")
  label_filepath1 = Label(window,text = str(filepath1))
  label_filepath1.grid(column = 2, row = 2)
  print ("file1: "+filepath1+"\n")

def browseFiles2():
  global filepath2
  filepath2 = tkFileDialog.askopenfilename(title="Open Second File")
  label_filepath2 = Label(window,text = str(filepath2))
  label_filepath2.grid(column = 2, row = 4)
  print ("file2: "+filepath2+"\n")
  

def submit():
  cmdCommand = "WinMergeU" +" "+filepath1 +" " + filepath2 + " " + "-minimize" + " " +  "-noninteractive" + " " +  "-u" + " " + "-or" + " " + "C:/Users/roshan.jp/Desktop/moderna_file_difference.htm"
  os.popen(cmdCommand)
  webbrowser.get().open('file://'+ 'C:/Users/roshan.jp/Desktop/moderna_file_difference.htm')
	
																							
# Create the root window
window = Tk()

# Set window title
window.title('Content Comparator')

# Set window size
window.geometry("825x500")

#Set window background color
window.config(background = "white")

image1 = ImageTk.PhotoImage(Image.open('C:/Users/roshan.jp/AppData/Local/Programs/WinMerge/fractal.jpg'))
image2 = ImageTk.PhotoImage(Image.open('C:/Users/roshan.jp/AppData/Local/Programs/WinMerge/moderna.jpg'))
image3 = ImageTk.PhotoImage(Image.open('C:/Users/roshan.jp/AppData/Local/Programs/WinMerge/legend.png'))


# Create a File Explorer label
label_file_explorer = Label(window,text = "Legend :",width=10,fg = "red",font = ('Helvetica',15,'bold'),background='white',anchor='w')
stop_gap1 = Label(window,text = "           ",background='white')
stop_gap2 = Label(window,text = "           ",background='white')
stop_gap3 = Label(window,text = "           ",background='white')
stop_gap4 = Label(window,text = "                                                                                                      ",background='white')
logo1 = Label(window,image=image1)
logo2 = Label(window,image=image2)
logo3 = Label(window,image=image3)


	
button_explore_1 = Button(window,text = "Choose File 1",command = browseFiles1)
button_explore_2 = Button(window,text = "Choose File 2",command = browseFiles2)
button_exit = Button(window,text = "Compare",command = submit)

stop_gap3.grid(column=1,row=1)
button_explore_1.grid(column = 1, row = 2)
stop_gap1.grid(column=1,row=3)
button_explore_2.grid(column = 1,row = 4)
stop_gap2.grid(column=1,row=5)
stop_gap4.grid(column=2,row=0)
button_exit.grid(column = 1,row = 6)
label_file_explorer.grid(sticky='W',column = 0, row = 7)
logo3.grid(sticky='W',column = 0,row =8)
logo1.grid(column = 0,row=0)
logo2.grid(column=3,row=0)


# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns

# Let the window wait for any events
window.mainloop()
