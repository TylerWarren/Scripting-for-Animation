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



class ColorWindow:
    def __init__(self):
        self.window_name = "ColorWindow"

    def create(self):

        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)
        
        # Create the UI window
        self.window = cmds.window(self.window_name, title="Assign Colors", widthHeight=(300, 200))
        self.layout = cmds.columnLayout(adjustableColumn=True)
        cmds.text(label="Assign color:")

        # Create color buttons
        color_indices = [13, 6, 14,] 
        color_labels = ["Red", "Blue", "Green",]  
        for i, color in enumerate(color_indices):
            cmds.button(
                label=f"Assign {color_labels[i]}",
                backgroundColor=self.get_color(color),
                command=lambda _, c=color: changeColor(c) 
            )
            
        cmds.showWindow(self.window)

    def get_color(self, colorIndex):
        """
        Map Maya color indices to RGB values for button display.
        """
        color_map = {
            13: (1, 0, 0), 
            6: (0, 0, 1),  
            14: (0, 1, 0),  
        }
        return color_map.get(colorIndex, (0.5, 0.5, 0.5))

# Create the window
my_window = ColorWindow()
my_window.create()