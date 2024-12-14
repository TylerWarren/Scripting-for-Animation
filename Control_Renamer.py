import maya.cmds as cmds

def rename(naming_scheme):
    # Count the number of '#' symbols
    num_hashes = naming_scheme.count("#")
    selected_objects = cmds.ls(selection=True, long=True)

    valid_objects = [obj for obj in selected_objects if cmds.objExists(obj)]
    # Rename each valid object
    for i, obj in enumerate(valid_objects, start=1):
        padded_number = f"{i:0{num_hashes}}"
        new_name = naming_scheme.replace("#" * num_hashes, padded_number)
        
        # Rename the objects
        renamed_object = cmds.rename(obj, new_name)
        print(f"Result: {renamed_object}")


class ControlWindow:
    def __init__(self):
        self.window_name = "ControlName"
        
    def create(self):
        # Check if the window exists and delete it if necessary
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)
        
        # Create a new window
        self.window = cmds.window(self.window_name, title="Rename Controls", widthHeight=(300, 200))
        self.layout = cmds.columnLayout(adjustableColumn=True)
        
        # UI Elements
        cmds.text(label="Enter New Name (use # for numbering):")
        self.name_field = cmds.textField(placeholderText="e.g., L_Arm_##_Jnt")
        cmds.button(label="Rename", command=self.rename_selected_objects)
        
        cmds.showWindow(self.window)
        
    def rename_selected_objects(self, *args):
        naming_scheme = cmds.textField(self.name_field, query=True, text=True)
        rename(naming_scheme)

# Create and display the control window
my_window = ControlWindow()
my_window.create()

# Example usage:
# rename("L_Leg_###_Jnt")
# rename("R_Arm_##_Jnt")
# rename("Spine_####_Jnt")

# Select objects in Maya and then run this script
# Make sure objects are properly selected for the code to work
