

# Custom imports
import canvas.data as canvasData
import modelDataBase as mdb
import modelObjects.vertex as vertexObject
import modelObjects.line as lineObject
import modelObjects.face as faceObject

###
# LOAD DATA TO MDB - TEMP
###

modelData = (['vertex-0', -100, -100],
             ['vertex-1',  100, -100],
             ['vertex-2',  100,  100],
             ['vertex-3', -100,  100])

# Create mdb.vertices
for m in modelData:
    mdb.vertices[m[0]] = vertexObject.Vertex(m[0],(m[1], m[2]))


# LINES

modelData = (('line-0','vertex-0','vertex-1'),
            ('line-1','vertex-1','vertex-2'),
            ('line-2','vertex-2','vertex-3'),
            ('line-3','vertex-3','vertex-0'))


# Create mdb.vertices
for m in modelData:
    mdb.lines[m[0]] = lineObject.Line(m[0],(m[1], m[2]))



# FACES
modelData = (('face-0','line-0','line-1','line-2','line-3'),)
# Create mdb.faces
for m in modelData:
    mdb.faces[m[0]] = faceObject.Face(m[0],(m[1], m[2], m[3], m[4]))


###
# Draw
###

def geo(myCanvas):
    myCanvas.delete("all")

    # Plot faces
    for m in mdb.faces.values():
        coords = []
        for l in m.lines:
            v1 = mdb.vertices[mdb.lines[l].vertices[0]].coordinates
            v2 = mdb.vertices[mdb.lines[l].vertices[1]].coordinates

            v1s = (v1[0]*canvasData.scale-canvasData.viewpoint[0],
                   v1[1]*canvasData.scale-canvasData.viewpoint[1])
            v2s = (v2[0]*canvasData.scale-canvasData.viewpoint[0],
                   v2[1]*canvasData.scale-canvasData.viewpoint[1])
            
            coords.append(v1s)
            coords.append(v2s)
        
        myCanvas.create_polygon(coords, fill=m.color)
    
    # Plot lines
    for m in mdb.lines.values():
        v1 = mdb.vertices[m.vertices[0]].coordinates
        v2 = mdb.vertices[m.vertices[1]].coordinates

        v1s = (v1[0]*canvasData.scale-canvasData.viewpoint[0],
               v1[1]*canvasData.scale-canvasData.viewpoint[1])
        v2s = (v2[0]*canvasData.scale-canvasData.viewpoint[0],
               v2[1]*canvasData.scale-canvasData.viewpoint[1])
        
        width = m.size
        color = m.color

        myCanvas.create_line(v1s, v2s, fill=color, width=width)
    
    # Plot vertices
    for m in mdb.vertices.values():
        c = m.coordinates
        v = (c[0]*canvasData.scale-canvasData.viewpoint[0],
             c[1]*canvasData.scale-canvasData.viewpoint[1])
        
        r = m.size
        color = m.color

        myCanvas.create_oval(v[0]-r, v[1]-r, v[0]+r, v[1]+r, fill=color)
    
        
    
        