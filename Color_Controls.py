import maya.cmds as cmds

def changeColor(colorIndex=15):
    # Get the selected objects
    selected_objects = cmds.ls(selection=True)

    for obj in selected_objects:
        shapes = cmds.listRelatives(obj, shapes=True) or []
            
    for shape in shapes:
        #Enable the overrides
        cmds.setAttr(f"{shape}.overrideEnabled", 1)
        cmds.setAttr(f"{shape}.overrideColor", colorIndex)

#Example: changeColor(13) 
#Change the number to get diffrent colors
#Enter the script into the script editor and type the command
#Be sure to turn on wireframe for the colors to properly display