Loading a directory of images to use
==========================================
This is something that is very useful all the time when using computer vision.
You may not have a camera readily available but you can easily load a directory
of images to play with.

Sometimes **sets** of images are nice to have as well. You can find data sets of
similiar things, for instance maybe a bunch of pictures of fruit and you want
to use computer vision to detect the type of fruit based on **features** that
we define.

.. note:: Free data sets are available in a list here: http://github.com/ingenuitas/SimpleCV/wiki/List-of-know-open-data-sets-for-testing


So what you will need to do is browse the web and download images into
a seperate directory or in the same directory as the script.  For this example
the file extensions have to be .png, but you can change the code to .jpg, .bmp, etc.


To load up and show a directory of images lets look at the code::

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



:download:`Download the script <../code/directory-of-images.py>`


As you can see it doesn't take much to load up and start changing files.


