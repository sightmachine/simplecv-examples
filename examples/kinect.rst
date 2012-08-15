Kinect
==========================================
It is possible to use the Xbox kinect with SimpleCV.
This makes it much easier to filter things out of the image based on
depth.  It is possible get a 3D image from two cameras (called Stereopsis)
just as how humans see objects with their eyes.  Unfornately this method
is very computationally intensive, which means without a powerful computer
you probably won't be able to do it in real time.

The xbox significantly helps solve that computational problem by using
infrared dots in the image to do some detection of the depth.

In the first example we will do exactly that, just load up the kinect
and then get the depth image, where black is closer to the camera, and white
is further away.::

	from SimpleCV import *
	cam = Kinect()


	while True:
		depth = cam.getDepth()
		depth.show()
	

:download:`Download the script <../code/kinect.py>`


You should get an image similiar to:

.. figure:: ../static/images/kinect.png
   :scale: 100 %
   :align: center
   :alt: Photo of SimpleCV Shell


There is a little trick SimpleCV does to make the depth image play nice is
converts it to a greyscale image.  So normally the depth image is 11bit depth
and a greyscale image is 8 bit depth.   A greyscale image has a color from
0 to 255.  This is just like a color image, except a color image has three
channels that go from 0-255, and a greyscale only one.  What this means is
if you have 640 by 480 pixel image, each pixel on that image will be represent
with a number between 0 and 255.

For us this becomes useful because SimpleCV converts it from 11bit depth to 8bit
depth so you can treat the image just like a greyscale image.  This is useful
as mentioned before, for things like filtering on depth.  We can use a normal
image manipulation function to filter items out.  In our case we will use the
stretch() function to "stretch" the image pixel color from the filter values.

So lets make an example, where we filter out things that are further away.
To do this just add the following to the loop so you have::

	while True:
		depth = cam.getDepth()
		filtered = depth.stretch(0,150)
		depth.show()


As you can see things in the distance are no longer in the picture.

.. note:: If you want 11 bit depth for higher accuracy you can use **cam.getDepthMatrix()**, although keep in mind that standard image functions no longer work

