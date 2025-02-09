###
# Draw
###

import canvas.data as canvasData

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

import canvas.data as canvasData

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

    # Zoom-in
    if event.delta>0 : canvasData.scale += canvasData.scrollSensitivity
    # Zoom-out
    elif canvasData.scale == 0.0001: return
    elif canvasData.scale-canvasData.scrollSensitivity <= 0: canvasData.scale = 0.0001
    else: canvasData.scale -= canvasData.scrollSensitivity

    # Redraw canvas
    w = event.widget
    draw(w)

    return