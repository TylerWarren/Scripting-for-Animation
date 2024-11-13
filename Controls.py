import maya.cmds as cmds

#Control transfrom data
control_data = [
    {"name": "Control1", "position": (1.01, 0, 0), "rotation": (90, 0, 0)},
    {"name": "Control2", "position": (-1.01, 0, 0), "rotation": (90, 0, 0)},
    {"name": "Control3", "position": (1.01, 1.01, 0), "rotation": (90, 0, 0)},
    {"name": "Control4", "position": (-1.01, 1.01, 0), "rotation": (90, 0, 0)},
    {"name": "Control5", "position": (1.01, 2.02, 0), "rotation": (90, 0, 0)},
    {"name": "Control6", "position": (-1.01, 2.02, 0), "rotation": (90, 0, 0)},
    {"name": "Control7", "position": (0, 3.01, 0), "rotation": (90, 0, 0)},
    {"name": "Control8", "position": (0, 3.25, 0), "rotation": (90, 0, 0)},
    {"name": "Control9", "position": (0, 4.25, 0), "rotation": (90, 0, 0)},
    {"name": "Control10", "position": (0, 5.25, 0), "rotation": (90, 0, 0)},
    {"name": "Control11", "position": (0, 6.25, 0), "rotation": (90, 0, 0)},
    {"name": "Control12", "position": (1.01, 5.25, 0), "rotation": (90, 0, 45)},
    {"name": "Control13", "position": (2.02, 4.3, -0.2), "rotation": (90, 0, 45)},
    {"name": "Control14", "position": (3.03, 3.3, 0), "rotation": (90, 0, 45)},
    {"name": "Control15", "position": (-1.01, 5.25, 0), "rotation": (90, 0, -45)},
    {"name": "Control16", "position": (-2.02, 4.3, -0.2), "rotation": (90, 0, -45)},
    {"name": "Control17", "position": (-3.03, 3.3, 0), "rotation": (90, 0, -45)},
]

#Loop for each control
for control in control_data:
    cont = cmds.circle(name=control["name"])[0]
    cmds.move(*control["position"])
    cmds.rotate(*control["rotation"])
    cmds.scale(0.8, 0.8, 0.8)
    cmds.select(cont)

    #Nameing the controls
    control_name = control["name"] + "_Ctrl"
    cont = cmds.rename(cont, control_name)

    #Naming the groups
    group_name = control["name"] + "_Ctrl_Grp"
    group = cmds.group(empty=True, name=group_name)

    #Parents the groups
    cmds.parent(cont, group)

    #Sets the group transformations to zero
    cmds.setAttr(group + ".translate", 0, 0, 0)
    cmds.setAttr(group + ".rotate", 0, 0, 0)
    
 