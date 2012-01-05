#!/usr/bin/python
'''
This example is meant to simulate long exposure across multiple
images.  It takes in a sequence of images and then creates the effect.
In this example a person is walking across the screen, you should
see a kind of ghost trail beind the person walking.
'''
print __doc__

from SimpleCV import *

image_directory = "../images/exposure/"
frames = ImageSet() #create an empty image set
frames.load(image_directory) #load the directory of images
img = Image(frames[0].size()) #create an initial empty image
num_of_frames = len(frames) #count the number of images

for frame in frames:
	img = img + (frame / num_of_frames) # merge the images together

img.show()
time.sleep(1000)



