"""
MAIN PROJECT FILE

Build a 2D drawing programm with tkinter canvas

"""

# General imports
from tkinter import *

####################################################################
##                            FUNCTIONS                           ##
####################################################################

def getFrameSize(root, frame):
    root.update()
    wi = frame.winfo_width()
    hi = frame.winfo_height() 
    return(wi, hi)


####################################################################
##                              ROOT                              ##
####################################################################

###
# Create main window
###

root = Tk()
root.state('zoomed')
root.minsize(height=400, width=600)


###
# Root Configuration
###

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

###
# Canvas Frame
###
CanvasFrame = Frame(root, bg='red')
CanvasFrame.grid(row=0, column=0, sticky='nswe')


####################################################################
##                               RUN                              ##
####################################################################
root.mainloop()