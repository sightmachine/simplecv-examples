#!/usr/bin/python 
from operator import add
from SimpleCV import *

cam = Camera()

frames_to_blur = 4
frames = ImageSet()

while True:
  frames.append(cam.getImage())

  if len(frames) > frames_to_blur:
    frames.pop(0)  #remove the earliest frame if we're at max

  pic = reduce(add, [i / float(len(frames)) for i in frames])
  #add the frames in the array, weighted by 1 / number of frames

  pic.show()
