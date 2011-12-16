Writing the Hello World Program
==========================================
The following is the hello world for SimpleCV.  What is does is basically
opens up the camera, takes a picture and shows it.

Here is the code::

	from SimpleCV import *
	cam = Camera()

	while (1):
		i = cam.getImage()
		i.show()




What is going on in this example is the::

	from SimpleCV import *


brings in all the SimpleCV library into the namespace.
What does that mean?  It means less typing for us.

The same program could also be written as::

	import SimpleCV
	cam = SimpleCV.Camera()

	while(1):
		i = cam.getImage()
		i.show()



The first method is typically the way we will write the programs, until
you are comfortable enough with using SimpleCV outside of it's built in libraries.



	
