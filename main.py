"""
MAIN PROJECT FILE

Build a 2D drawing programm with tkinter canvas

"""

# General imports
from tkinter import *

# Custom imports
import canvas.data as canvasData
import canvas.functions as canvasFunc

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
# Canvas
###
myCanvas = Canvas(root, bg='dark grey')
myCanvas.grid(row=0, column=0, sticky='nswe')


# Dummy shape - Initial draw
h,w = getCanvasSize(root, myCanvas)
canvasData.viewpoint = [-h/2., -w/2.]
canvasFunc.draw(myCanvas)


###
# Mouse Data
###

myCanvas.bind("<Button-1>", canvasFunc.getClickCoordinates)
myCanvas.bind("<B1-Motion>", canvasFunc.drag)
myCanvas.bind("<MouseWheel>", canvasFunc.zoom)



####################################################################
##                               RUN                              ##
####################################################################
root.mainloop()