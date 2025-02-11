# General imports
import copy

# Custom imports
import canvas.data as canvasData

###
# Draw
###

def draw(myCanvas):
    myCanvas.delete("all")

    squareNodes = (
                   (0,0),
                   (200,200),
                  )
    
    scaledNodes = (
                    (squareNodes[0][0]*canvasData.scale, squareNodes[0][1]*canvasData.scale),
                    (squareNodes[1][0]*canvasData.scale, squareNodes[1][1]*canvasData.scale)
                  )

    panNodes = (
                    (scaledNodes[0][0]-canvasData.viewpoint[0], scaledNodes[0][1]-canvasData.viewpoint[1]),
                    (scaledNodes[1][0]-canvasData.viewpoint[0], scaledNodes[1][1]-canvasData.viewpoint[1])
                  )

    myCanvas.create_rectangle((panNodes[0][0], panNodes[0][1], panNodes[1][0], panNodes[1][1]), fill='black')



###
# Mouse data
###

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
    draw(w)

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
    draw(w)

    return