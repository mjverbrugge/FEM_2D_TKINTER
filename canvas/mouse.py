# General imports
import copy

# Custom imports
import canvas.data as canvasData
import canvas.draw as canvasDraw

# PAN #

def getCoordinates(event):
    w = event.widget
    x = w.canvasx(event.x)
    y = w.canvasy(event.y)
    return (x, y)

def getClickCoordinates(event):
    x, y = getCoordinates(event)
    canvasData.mousePosition = (x,y)
    return

def drag(event):
    vp = canvasData.viewpoint
    
    x, y = getCoordinates(event)
    xDiff = x-canvasData.mousePosition[0] 
    yDiff = y-canvasData.mousePosition[1] 
    canvasData.viewpoint = [vp[0]-xDiff, vp[1]-yDiff]

    # Redraw canvas
    w = event.widget
    canvasDraw.geo(w)

    # Reset imported values
    canvasData.mousePosition = (x,y)
    return



# ZOOM #

def zoom(event):
    # Update scale based on zoom input

    vp = canvasData.viewpoint
    # Reconstruct mouse position
    x, y = getCoordinates(event)
    # Save initial scale factor
    scaleInitial = copy.deepcopy(canvasData.scale)


    # Zoom-in
    if event.delta>0 : canvasData.scale += canvasData.scrollSensitivity
    # Zoom-out
    elif canvasData.scale == 0.0001: return
    elif canvasData.scale-canvasData.scrollSensitivity <= 0: canvasData.scale = 0.0001
    else: canvasData.scale -= canvasData.scrollSensitivity

    # Scale to mouse
    sR = canvasData.scale/scaleInitial # Scale ratio

    #canvasData.viewpoint[0] = vp[0]-xDif
    canvasData.viewpoint[0] = vp[0]*sR + (sR-1)*x
    canvasData.viewpoint[1] = vp[1]*sR + (sR-1)*y

    # Redraw canvas
    w = event.widget
    canvasDraw.geo(w)

    return