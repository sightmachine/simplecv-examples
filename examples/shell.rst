SimpleCV Shell
==============
The shell is the first place you will get started playing around with
SimpleCV. This is because everything is already loaded up for you and
is ready to begin to be your playground to develop full applications.

Starting the shell maybe different depending on what operating system you
are on. If you are on Windows there should be a shortcut on your desktop.
On Mac or Ubuntu you should just be able to type ``simplecv`` from the shell.::

    $ simplecv

If this isn't working then you can do it the standard way that should work
regardless of what Operating system you are on.

If you can't find or get the launcher working, this is the manual way to
start the shell.

Open the python shell, if you are on Windows it should be somewhere in the
program files if you just look around, and on Mac and Ubuntu you should be
able to start it just by typing ``python``.

You should see something like::

    $ python
    Python 2.7.3 (default, Aug  9 2012, 17:23:57) 
    [GCC 4.7.1 20120720 (Red Hat 4.7.1-5)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from SimpleCV import Shell
    >>> Shell.main()

That in turn should launch something that looks like the following::

    +-----------------------------------------------------------+
     SimpleCV 1.3.0 [interactive shell] - http://simplecv.org
    +-----------------------------------------------------------+

    Commands: 
	    "exit()" or press "Ctrl+ D" to exit the shell
	    "clear" to clear the shell screen
	    "tutorial" to begin the SimpleCV interactive tutorial
	    "example" gives a list of examples you can run
	    "forums" will launch a web browser for the help forums
	    "walkthrough" will launch a web browser with a walkthrough

    Usage:
	    dot complete works to show library
	    for example: Image().save("/tmp/test.jpg") will dot complete
	    just by touching TAB after typing Image().

    Documentation:
	    help(Image), ?Image, Image?, or Image()? all do the same
	    "docs" will launch webbrowser showing documentation

    SimpleCV:1>

If you can't get to the shell, then head on over to the help forum at:
http://help.simplecv.org


Getting Help Right in the Shell
-------------------------------
No joke, you can literally get help right in the shell. There is a built-in
help system with search. Remember, just press 'q' to quit the help mode at
any time while you are in it and you will just right back to the shell.

To see what is available just type::

    SimpleCV:1> help(SimpleCV)
	
The output from that command should look like::

    Help on package SimpleCV:

    NAME
        SimpleCV

    FILE
        /usr/lib/python2.7/site-packages/SimpleCV/__init__.py

    PACKAGE CONTENTS
        Camera
        Color
        ColorModel
        Display
        DrawingLayer
        EXIF
        Features (package)
        Font
        ImageClass
        MachineLearning (package)
        Segmentation (package)
        Shell (package)
        Stream
        base
        tests (package)

    SUBMODULES
        Detection
        __init__

You can get help from on any of the listed libraries. If you're just starting
out, Image is a great place to start.

To view the Image help, type::

    SimpleCV:1> help(Image)

The output should be similiar to before::

    Help on class Image in module SimpleCV.ImageClass:

    class Image
     |  **SUMMARY**
     |  
     |  The Image class is the heart of SimpleCV and allows you to convert to and 
     |  from a number of source types with ease.  It also has intelligent buffer
     |  management, so that modified copies of the Image required for algorithms
     |  such as edge detection, etc can be cached and reused when appropriate.
     |  
     |  
     |  Image are converted into 8-bit, 3-channel images in RGB colorspace.  It will
     |  automatically handle conversion from other representations into this
     |  standard format.  If dimensions are passed, an empty image is created.
     |  
     |  **EXAMPLE**
     |  
     |  >>> i = Image("/path/to/image.png")
     |  >>> i = Camera().getImage()
     |  
     |  
     |  You can also just load the SimpleCV logo using:
     |  
     |  >>> img = Image("simplecv")
     |  >>> img = Image("logo")
     |  >>> img = Image("logo_inverted")
     |  >>> img = Image("logo_transparent")
     |  
     |  Or you can load an image from a URL:
     |  
     |  much more here ...

.. note:: The shell is case senstive, so typing ``help(simplecv)`` won't work. 
          Instead, you need to type ``help(SimpleCV)``. This case sensitivy
          applies to all of the other topics as well.
