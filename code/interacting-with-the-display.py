from SimpleCV import *
cam = Camera()
disp = Display()

while disp.isNotDone():
  img = cam.getImage()
  if disp.mouseLeft:
		break
  img.save(disp)
