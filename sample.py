#### GUI FRONTEND SCRIPT FOR DIFF-PDF (guiDiffPDF) ####
## Author: Brian Khuu 2014 briankhuu.com
## Description: This script will ask you for two files,
##              and then open a visual mode diff.
##              In other platform, just change diff-pdf.exe
## Install: Place in same location as diff-pdf.exe
##          Don't forget to put it in system path for handy access!
## Tested: On windows 8 with python V3.1
## Dependency: diff-pdf.exe @ https://github.com/vslavik/diff-pdf
import tkinter, sys
import tkinter.filedialog #https://mail.python.org/pipermail/python-list/2010-April/574512.html
import os



## START GUI ##
root = tkinter.Tk()         # open and start tkinter object
root.withdraw()             # hide the root window
## save sys.argv arguments (As file dialog changes it...) ##
optArgV = sys.argv[1:] # optional ArgV.

## ASK USER WHICH TWO FILES TO COMPARE ##
filePath1 = tkinter.filedialog.askopenfilename(title="Open First PDF - 1")
print ("pdf1: "+filePath1+"\n")  #Display first filepath
filePath2 = tkinter.filedialog.askopenfilename(title="Open Second PDF - 2")
print ("pdf1: "+filePath2+"\n")  #Display second filepath

## Run the command line instruction ##
cmdCommand = "WinMergeU" +" "+filePath1 +" " + filePath2 + " " + "-minimize" + " " +  "-noninteractive" + " " +  "-u" + " " + "-or" + " " + "C:/Users/User/Desktop/answer.htm"
print(cmdCommand)
os.popen(cmdCommand)