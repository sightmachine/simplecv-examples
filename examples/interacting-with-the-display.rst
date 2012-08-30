Interacting with the Display
==========================================
This actually isn't going to take much more work than the standard hello
world example.  Except we are introduction a new concept or object type.

The Display.

.. note:: type **help Display** from the SimpleCV shell for more help


What the display is doing different than the show() function is that it
allows us to get interaction from it.  So it in this case we want our program
to end when the left mouse button is clicked.

To create a display object we literally type:

	>>> disp = Display()


Now we will incorporate this into our example::

	from SimpleCV import *
	cam = Camera()
	disp = Display()

	while disp.isNotDone():
		img = cam.getImage()
		if disp.mouseLeft:
			break
		img.save(disp)


:download:`Download the script <../code/interacting-with-the-display.py>`

So what is happening here. Is we created a display object.  It then checks
it's function called isNotDone().  That function updates the display and
makes sure to see if any events have occurect, such as in our case the screen
had been clicked on with the left mouse, then update.

So the event is updated and the next time through the while loop we check::

	if disp.mouseLeft:


What this is doing is returns true or false depending of if it was clicked.
In the instance that it was actually clicked, then it runs **break**, which
tells the while() loop at the begin to break the loop, and of course our program
then exits.


