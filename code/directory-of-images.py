"""
This program loads all the images in the current directory
with the file extension .png

Feel free to change the extension around if you want the images
to be something else.

If nothing is shown then you are either pointing to the wrong directory,
aren't using the correct extension, or there aren't any images in that directory
"""
import os
import glob
import time
from SimpleCV import *

print __doc__

#Settings
my_images_path = "/tmp/cats/" #put your image path here if you want to override current directory
extension = "*.png"


#Program
if not my_images_path:
  path = os.getcwd() #get the current directory
else:
  path = my_images_path
  
imgs = list() #load up an image list
directory = os.path.join(path, extension)
files = glob.glob(directory)

for file in files:
  new_img = Image(file)
  new_img.show()
  time.sleep(1) #wait for 1 second
