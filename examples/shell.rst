SimpleCV Shell
---------------

The shell is the first place you will get started playing around with SimpleCV. This is because everything is already loaded up for you and is ready to begin to be your playground to develop full applications.

Starting the shell maybe different depending on what operating system you are on. If you are on windows there should be a shortcut on your desktop. On Mac or Ubuntu you should just be able to type 'simplecv' from the shell. If this isn't working then you can do it the standard way that should work regardless of what Operating system you are on.

If you can't find or get the launcher working, this is the manual way to start the shell.

Open the python shell, if you are on windows it should be somewhere in the program files if you just look around, and on Mac and Ubuntu you should be able to start it just by typing python.
You should see something like::


	Python 2.7.2+ (default, Oct  4 2011, 20:06:09)
	[GCC 4.6.1] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	Once you are at the shell just type the following to launch the SimpleCV Shell:
	>>> from SimpleCV import Shell
	>>> Shell.main()


That in turn should launch something that looks like the following:

	.. figure:: ../static/images/simplecv-shell.png
		 :scale: 100 %
		 :align: center
		 :alt: Photo of SimpleCV Shell



 
If you can't get to the shell, then head on over to the help forum at: http://help.simplecv.org


Getting Help Right in the Shell
==========

No joke, you can literally get help right in the shell. There is a built-in help system with search. Remember, just press 'q' to quit the help mode at any time while you are in it and you will just right back to the shell.
To see what is available just type:

	>>> help SimpleCV
	
The output from that command should look like:
Help on package SimpleCV::

	NAME
		SimpleCV

	FILE
		/home/xamox/Code/simplecv/SimpleCV/__init__.py

	PACKAGE CONTENTS
		Camera
		Color
		ColorModel
		Detection
		Display
		DrawingLayer
		Features (package)
		Font
		ImageClass
		Images
		MachineLearning (package)
		Segmentation (package)
		Shell (package)
		Stream

				
You can get help from on any of the listed libraries. If you're just starting out, Image is a great place to start.

To view the Image help, type:

	>>> help Image


The output should be similiar to before:
Help on class Image in module SimpleCV.ImageClass::

	class Image
		The Image class is the heart of SimpleCV and allows you to convert to and
		from a number of source types with ease.  It also has intelligent buffer
		management, so that modified copies of the Image required for algorithms
		such as edge detection, etc can be cached and reused when appropriate.
		.
		.
		.
		more




.. note:: The shell is case senstive, so typing 'help simplecv' won't work. Instead, you need to type 'help SimpleCV'. This case sensitivy applies to all of the other topics as well.
