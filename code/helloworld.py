from SimpleCV import *
cam = Camera()

while True:
  i = cam.getImage()
  i.show()
