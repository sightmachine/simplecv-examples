Macro's
=============================
SimpleCV has the ability to use macro's built in.

If you aren't familiar with a macro, it's basically a way
to define a set of programming events to happen with just
using a single command.

In our case our macro's will be built off the history of commands
that we use in the shell.  This helps us test things that work, and what
doesn't.

Remember how to load an image, find the blobs and show the image?

	>>> img = Image("lenna")
	>>> blobs = img.findBlobs()
	>>> if blobs:
		blobs.draw()
	>>> img.show()


What happened there is we showed the image, but maybe we want to do that same
type of functionality but for different images.

We will reduce this::

	blobs = img.findBlobs()
	if blobs:
		blobs.draw()
	img.show()


To a single command like:

	>>> showblobs


To do this, we can create a macro.  If you type the command:

	>>> history


You should get an output similiar to::

	3: img = Image("lenna")
	4: blobs = img.findBlobs()
	5:
	if blobs:
			blobs.draw()
	6: img.show()
	7: _ip.magic("history ")


.. note:: you can tap up or down on the arrow keys to cycle through history as well


What you can see there is all the previous commands we have ran.
But in our case we want to build that into a macro.  To do this we want
lines 4,5, and 6 from the history, so to convert those into a macro it's
as easy as:

	>>> macro showblobs 4-6

It's just **macro name lines**.
Then to run it you just use:

	>>> showblobs

You will see the same thing as before, but now we can change
the image quickly and run it again.

	>>> img = Image("simplecv")
	>>> showblobs


This was pretty straight forward.  But say we want to change
the color of the blobs shown in our macro.  Then we need to use the macro
If you aren't familiar with using VI then it is recommended you read
editor manual here:
http://www.unix-manuals.com/tutorials/vi/vi-in-10-1.html

To edit our existing macro we just type:

	>>> edit showblobs


and you should get something similiar to::

	blobs = img.findBlobs()
	if blobs:
			blobs.draw()
	img.show()



We can just edit the blobs.draw() function so it reads:

	>>> blobs.draw(autocolor=True)


Press **ESC**
Then press ** ctrl + :**
Then type ** w + enter **
to save (write) the macro.


Press **ESC**
Then press ** ctrl + :** once again,
then type ** q + enter **
to quit the macro editor.

Now if you type:

	>>> showblobs


You will get the image, but the blobs will be multicolored.
This was just a very small intro into macros.  As you can see
they make writing code even faster and easier.

If you would like to learn more about macros just type:

	>>> macro ?



