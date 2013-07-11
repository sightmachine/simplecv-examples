from SimpleCV import *

cam = Camera()

while True:
    img = cam.getImage()
    img.show()
