Image Arithmetic
=========================
As we discussed before, images are basically just matrices of pixel values
that range from 0 to 255.  And since they are built in this format, it is
actually easy to perform arithmetic (math) on images, such as addition or
subtraction.


There are many uses for performing image math.  For the first example
we will show what happens when we add two images together.

	>>> imgA = Image("simplecv")
	>>> added = imgA + imgA
	>>> added.show()


So what we did was take the original simplecv image logo that looked like

.. figure:: ../images/simplecv-logo.png
   :scale: 100 %
   :align: center



and converted so it looked like this:

.. figure:: ../images/image-math-add.png
   :scale: 100 %
   :align: center



If you note that since ( X + X = X * 2) we can also try this as well.

	>>> imgA = Image("simplecv")
	>>> mult = imgA * 2
	>>> mult.show()


You should get the same exact image as shown before.
You can also perform subtraction.  Except what is different here, is that
using subtraction will only show what has changed between the two images.

	>>> logo = Image("logo")
	>>> sub = logo - logo
	>>> sub.show()


You should get a completely black image.


..note: To perform image math the images have to be the same exact size


It is also possible to perform division on images.  This is useful for
lowering the contrast.  For instance if you use the SimpleCV logo:

.. figure:: ../images/simplecv-logo.png
   :scale: 100 %
   :align: center



And if we divide the image by 10:

	>>> scv = Image("simplecv")
	>>> div = scv / 10
	>>> div.show()


and you should get something that looks like:

.. figure:: ../images/image-math-div.png
   :scale: 100 %
   :align: center



Now you maybe asking when image math is actually useful.  Well let's give
a quick example.  We will show how simple subtraction can be used to
detect motion.  In this example we have a picture of a person, then the
next picture you can tell they waved their hand.  Then we will subtract
those two images and you will only what has changed between the two
images.



.. figure:: ../images/image-math-person1.png
	:scale: 100 %
	:align: center

	Previous Frame


.. figure:: ../images/image-math-person2.png
	:scale: 100 %
	:align: center

	Current Frame



.. figure:: ../images/image-math-person-sub.png
 :scale: 100 %
 :align: center

 Difference Image


As seen above only the pixels that changed between the two images are
shown.  To perform a similiar example just do:

	>>> cam = Camera()
	>>> prev = cam.getImage()
	>>> current = cam.getImage()
	>>> diff = current - prev
	>>> diff.show()


But how does that tell us that motion occured?  Well we can use some
basic math to figure that out.  We know if the pixel value was black (0)
then nothing had changed, but if not black, then something must have
changed.  We will compute how much of the entire picture actually changed.

To do this we will just get the image matrix and add a counter::


	>>> area = diff.width * diff.height
	307200 #this is our image area in pixels
	>>> matrix = diff.getNumpy()
	>>> matrix.shape
	(640, 480, 3)
	>>> flat = matrix.flatten()
	>>> counter = 0
	>>> for i in flat:
		if flat[i] == 0: #if black
			counter += 1

	>>> percent_change = float(counter) / float(len(flat))
	>>> print percent_change
	0.818358289930555


With this you are able to determine about 0.8 or 80% change in pixels.
Although this is not the most efficient way we can now use this change
as a threshold value.  For instance send an e-mail if 90% of the pixels
change, and using a threshold you can minimize the chance of false positives
happening.

As mentioned this probably isn't the most effecient way to determine if
motion has occured, but it is probably the most basic method and was just
meant to show how you can use image math to do some basic useful things.


We can also use other properties of the image. For instance any standard
type of mathematic statistics functions are available.  This could be mean,
standard deviation, etc.  As in the previous example we could instead use
the mean which is much quicker.

Let's use that in a complete program below::

	from SimpleCV import *

	cam = Camera()
	threshold = 5.0 # if mean exceeds this amount do something

	while True:
		previous = cam.getImage() #grab a frame
		time.sleep(0.5) #wait for half a second
		current = cam.getImage() #grab another frame
		diff = current - previous
		matrix = diff.getNumpy()
		mean = matrix.mean()

		diff.show()

		if mean >= threshold:
			print "Motion Detected"

	

:download:`Download the code <../code/motion-detection.py>`
	



