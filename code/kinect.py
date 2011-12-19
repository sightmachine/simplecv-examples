"""
This example loads up a depth image from the xbox kinect.

What you are viewing is the depth image.

As things get closer to the kinect they will appear more black, as they get
further away they will appear more white.

Keep in mind the kinect has a range from about 1 meters in front to about 10
meters away

"""

print __doc__

from SimpleCV import *
cam = Kinect()


while True:
  depth = cam.getDepth()
  depth.show()
  
  
