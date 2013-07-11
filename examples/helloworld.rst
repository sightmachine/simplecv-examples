.. pyckecher: http://pychecker.sourceforge.net/
.. pylint: https://bitbucket.org/logilab/pylint/

Writing the Hello World Program
===============================
The following is the ``hello world`` for SimpleCV. What is does is basically
opens up the camera, takes a picture and shows it.

Here is the code::

    from SimpleCV import *

    cam = Camera()

    while (1):
        img = cam.getImage()
        img.show()

:download:`Download the script <../code/helloworld.py>`

What is going on in this example is the::

    from SimpleCV import *

brings in all the SimpleCV library into the namespace. What does that mean?
It means less typing for us but will produce warning when you check your file
with `pychecker`_ or `pylint`_. Usually this is not desirable because it makes
it harder to maintain and debug your scripts.

The same program could also be written as::

    import SimpleCV
    cam = SimpleCV.Camera()

    while (1):
        img = cam.getImage()
        img.show()

Ordinarily only importing what you need is the common way to do it::

    from SimpleCV import Camera

    cam = Camera()

    while True:
        img = cam.getImage()
        img.show()

Of course are you free to choose the way that fits best your skills or your
needs. The first method is typically the way we will write the programs, until
you are comfortable enough with using SimpleCV outside of it’s built-in
libraries.
