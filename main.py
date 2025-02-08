"""
MAIN PROJECT FILE

Build a 2D drawing programm with tkinter canvas

"""

# General imports
from tkinter import *

# Custom imports
import mouse.canvasData as mouseData

####################################################################
##                            FUNCTIONS                           ##
####################################################################

def getCanvasSize(root, canvas):
    root.update()
    wi = canvas.winfo_width()
    hi = canvas.winfo_height() 
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
myCanvas = Canvas(root, bg='dark grey')
myCanvas.grid(row=0, column=0, sticky='nswe')


# Dummy shape
dummySquare = 200
myCanvas.create_rectangle(((2048/2.)-0.5*dummySquare), ((1209/2.)-0.5*dummySquare), ((2048/2.)+0.5*dummySquare), ((1209/2.)+0.5*dummySquare), fill='black')


###
# Mouse Data
###
def getCoordinates(event):
    w = event.widget
    x = w.canvasx(event.x)
    y = w.canvasy(event.y)
    return (x, y)

def getClickCoordinates(event):
    x, y = getCoordinates(event)
    mouseData.tempButton1 = (x,y)
    return

def pan(event):
    x, y = getCoordinates(event)
    xDiff = x-mouseData.tempButton1[0] 
    yDiff = y-mouseData.tempButton1[1] 
    mouseData.pan = (xDiff, yDiff)
    print(mouseData.pan)

    # Reset imported values
    mouseData.tempButton1 = (0,0)
    return

myCanvas.bind("<Button-1>", getClickCoordinates)
myCanvas.bind("<ButtonRelease-1>", pan)


####################################################################
##                               RUN                              ##
####################################################################
root.mainloop()