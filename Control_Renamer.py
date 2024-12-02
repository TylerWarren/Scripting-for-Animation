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



# Example usage:
# rename("L_Leg_###_Jnt")
# rename("R_Arm_##_Jnt")
# rename("Spine_####_Jnt")

# Select objects in Maya and then run this script
# Make sure objects are properly selected for the code to work
