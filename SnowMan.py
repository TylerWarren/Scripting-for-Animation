import maya.cmds as cmbs

# Generates the snowman body
cmds.polySphere(radius=2, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0])
cmds.move(0, 1, 0)

cmds.polySphere(radius=1.35, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0])
cmds.move(0, 3, 0)

cmds.polySphere(radius=0.7, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0])
cmds.move(0, 4.5, 0)

#Generates the snowman hat
cmds.polyCylinder(radius=0.5, height=1, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0])
cmds.move(0, 5.5, 0)

cmds.polyCylinder(radius=0.9, height=0.2, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0])
cmds.move(0, 5, 0)

#Generates the buttons
cmds.polyCylinder(radius=0.134, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0])
cmds.move(0, 3.822, 0.144)
cmds.rotate( '90deg', 0, 0, r=True )

cmds.polyCylinder(radius=0.134, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0])
cmds.move(0, 3.457, 0.330)
cmds.rotate( '90deg', 0, 0, r=True )

cmds.polyCylinder(radius=0.134, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0])
cmds.move(0, 2.998, 0.402)
cmds.rotate( '90deg', 0, 0, r=True )

#Generates the eyes and nose
cmds.polyCone(radius=0.200, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0])
cmds.move(0, 4.569, 0.402)
cmds.rotate( '90deg', 0, 0, r=True )

cmds.polyCylinder(radius=0.05, height=0.1, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0])
cmds.move(0.232, 4.763, 0.581)
cmds.rotate( '90deg', 0, 0, r=True )

cmds.polyCylinder(radius=0.05, height=0.1, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0])
cmds.move(-0.232, 4.763, 0.581)
cmds.rotate( '90deg', 0, 0, r=True )

#Generates the arms

cmds.polyCylinder(radius=0.1, height=2, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0])
cmds.move(1.675, 4.150, 0)
cmds.rotate( 0, 0, '-40deg', r=True )

cmds.polyCylinder(radius=0.1, height=2, subdivisionsX=20, subdivisionsY=20, axis=[0,1,0])
cmds.move(-1.675, 4.150, 0)
cmds.rotate( 0, 0, '40deg', r=True )


