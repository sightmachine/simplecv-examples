'''
*****************************************************
Light at the end of the tunnel example:

This is a simple detector showing how to use a custom display.
It detects if a light is on. You can think of it as a detector
to determine if a train is coming down the way. This could be
used as an indicator to either walk or don't walk.
*****************************************************
'''

print __doc__

from SimpleCV import *

cam = Camera()
img = cam.getImage()
display = Display()
width = img.width
height = img.height
screensize = width * height
divisor = 5 # used for automatically breaking up image.
threshold = 150 # color value to detect blob is a light

def stoplayer():
	newlayer = DrawingLayer(img.size())
	points = [(2 * width / divisor, height / divisor),
						(3 * width / divisor, height / divisor),
						(4 * width / divisor, 2 * height / divisor),
						(4 * width / divisor, 3 * height / divisor),
						(3 * width / divisor, 4 * height / divisor),
						(2 * width / divisor, 4 * height / divisor),
						(1 * width / divisor, 3 * height / divisor),
						(1 * width / divisor, 2 * height / divisor)
					]
	newlayer.polygon(points, filled=True, color=Color.RED)
	newlayer.setLayerAlpha(75)
	newlayer.text("STOP", (width / 2, height / 2), color=Color.WHITE)

	return newlayer

def golayer():
	newlayer = DrawingLayer(img.size())
	newlayer.circle((width / 2, height / 2), width / 4, filled=True, color=Color.GREEN)
	newlayer.setLayerAlpha(75)
	newlayer.text("GO", (width / 2, height / 2), color=Color.WHITE)

	return newlayer


while display.isNotDone():
	img = cam.getImage()
	min_blob_size = 0.10 * screensize # the minimum blob is at least 10% of screen
	max_blob_size = 0.80 * screensize # the maximum blob is at most 80% of screen
	blobs = img.findBlobs(minsize=min_blob_size, maxsize=max_blob_size) # get the largest blob on the screen

	layer = golayer()

	#If there is a light then show the stop
	if blobs:
		avgcolor = np.mean(blobs[-1].meanColor()) #get the average color of the blob

		if avgcolor >= threshold:
			layer = stoplayer()

	img.addDrawingLayer(layer)
	img.show()
