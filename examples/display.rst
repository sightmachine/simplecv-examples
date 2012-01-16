Drawing on Images in SimpleCV
=================================
Most of the time when using a vision system it is nice to have some
form of visual feedback to the user of the vision system that something
has occured when programmed to detect an object.  Throughout most of
programming the vision system we have used the command line to output
useful information.

For instance, say we were doing face detection, using the command line
we could print out the location of the face in it's X,Y coordinates, but
really that is not very useful visually because in our minds converting
that number to an actual location on the screen. It's much more useful to
say draw a box around the found face.

Fornately SimpleCV has very easy methods for being able to draw, or mark
up the images to notify that something is going on.  Before we get into
how to use some of the functionality we'll talk a little bit about how
things are structured.

In simplecv there is a single "display" object.  In turn these means you
can only have a single window open viewing the camera at any single time.
Even though SimpleCV supports multiple cameras, you can only view one at
at time using the standard method, although there are more advanced ways
to do it as well through a web browser, they will not be discussed here.


To show off a simple example, we will talk a little bit about layers.
Very similiar to the concept of layers on an onion.  In our case our layers
can be unlimited and what's ever above or on top of the other layer will
cover the layer below it.  Let's look at the simplecv logo with some text
written on it.


.. figure:: ../images/display-layers-logo.png


Which in reality is an image with 3 layers, each layer has the text
displayed.  If we rotate the image and expand the layers you can get a
better idea of what is really happening with image layers.


.. figure:: ../images/display-layers-exploded.png




Layers
----------------------
Now that you have an understanding of what layers are, we can now start
to use them within SimpleCV.  To get a better understanding of that we
need to take a look at the DrawingLayer class built into SimpleCV. This
class is where all the actual drawing takes place.  This is not to be
confused with the Display class as that is used for the actual rendering
of the layers.  The DrawingLayer class is used to store all the various
information about things like features that are found, or text being drawn.

To explain the DrawingLayer class more precisely,
DrawingLayer gives you a way to mark up Image classes without changing
the image data itself. This class wraps pygame's Surface class and
provides basic drawing and text rendering functions

 
Example::

	>>> scv = Image('simplecv')
	>>> logo = Image('logo')
	>>> scv.dl().blit(logo) #write image 2 on top of image


You should get an image similiar to:

.. figure:: ../images/display-blit.png


NOTE: Run **help DrawingLayer** for more information.


What just happened in the previous example was we added a layer, put
the logo on that new layer, then added that layer to the exist image.
In fact, that's what the **blit()** function did in one step, but instead
lets walk through that example.::

	>>> scv = Image('simplecv')
	>>> scv.addDrawingLayer()
	1
	>>> scv.addDrawingLayer()
	2
	>>> scv.getDrawingLayer(1)
	'a new image'
	>>> scv.getDrawingLayer(2)
	'another layer'
	

