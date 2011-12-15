.. topic:: Examples in computer vision using SimpleCV

    ``SimpleCV`` is a Python module integrating classic computer vision
    algorithms and libraries and tying them into a clean, easy to install
    and use type of programming interface.

    It aims to be a way that programmers who may not have experience
    with computer vision can get up and running quickly.

    

.. note:: This document is meant to be used with **simple version
   1.2**


.. toctree::
   :numbered:
   :maxdepth: 2
	<!-- Here is where you will put the name of examples as they are added -->
	<!-- for example say we write a face recognition example and call that -->
	<!-- file face-detect.rst, then you just add 'facedetect' without quotes -->
	<!-- right below these comments -->
	

Installation
====================

1-click installers are available for Windows, Mac, and Ubuntu on the main
website: http://www.simplecv.org


There is also instructions in the documentation that tells how to do a
manual install if you want to use the "cutting edge" version or if you
are having trouble with the 1-click installers



The Shell
====================

The shell is the first place you will get started playing around with SimpleCV.
This is because everything is already loaded up for you and is ready to
begin to be your playground to develop full applications.

Starting the shell maybe different depending on what operating system you are
on.  If you are on windows there should be a shortcut on your desktop. On Mac
or Ubuntu you should just be able to type 'simplecv' from the shell.  If this
isn't working then you can do it the standard way that should work regardless
of what Operating system you are on.

If you can't find or get the launcher working, this is the manual way to start
the shell.

Open the python shell, if you are on windows it should be somewhere in the
program files if you just look around, and on Mac and Ubuntu you should be
able to start it just by typing python.

You should see something like:

	>>> Python 2.7.2+ (default, Oct  4 2011, 20:06:09) 
	>>> [GCC 4.6.1] on linux2
	>>> Type "help", "copyright", "credits" or "license" for more information.
	>>>

Once you are at the shell just type the following to launch the SimpleCV Shell:

	>>> from SimpleCV import Shell
	>>> Shell.main()


That in turn should launch something that looks like the following:

.. figure:: images/simplecv-shell.png
   :scale: 100 %
   :align: center
   :alt: Photo of SimpleCV Shell


If you can't get to the shell, then head over to: http://help.simplecv.org



Loading and Saving Images
====================
First thing we are going to do is load an image:

	>>> logo = Image("simplecv")

what that will do is load the SimpleCV logo into memory.
Now we want to see it:

	>>> logo.show()





To load an image, specify the file path in the constructor:

	>>> my_image = Image("path/to/image.jpg")

To save the image, use the save method.  It will automatically use the file
you loaded the image from:

	>>> my_image.save()



