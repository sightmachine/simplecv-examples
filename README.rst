.. -*- mode: rst -*-

.. _SimpleCV: http://simplecv.org/
.. _Python: http://python.org/
.. _Sphinx: http://sphinx-doc.org/
.. _Python Package Index: http://pypi.python.org/pypi/Sphinx

About
=====

`SimpleCV`_ is a open source cross platform machine vision framework written
in `Python`_.

The purpose of the **simplecv-tutorial** subproject is to learn how to apply
computer vision to practical situations using the tools implemented in the 
**SimpleCV** framework.

The target audience is those new to computer vision but also has the ability
to be extended to more advanced computer vision tasks.

Setup the build tool
====================

To build the HTML or the PDF (requires pdflatex) versions of this tutorial
`Sphinx`_ (1.0.0+) is needed. You can get from the `Python Package Index`_.::

    $ sudo pip install -U sphinx

Or use the Package management system of your distribution. For Fedora::

    $ sudo yum -y install python-sphinx

For Debian/Ubuntu::

    $ sudo apt-get install python-sphinx

Building the tutorial
=====================

Switch your ``simplecv-examples`` folder and build the html variant::

    $ make html

If you want to rebuild make sure you clean first::

    $ make clean
    $ make html

Auto Building the tutorial
==========================

If you are able to push to the master branch at:
http://github.com/ingenuitas/simplecv-examples

Then it should autobuild soon after and be found at:
http://simplecv-examples.readthedocs.org
