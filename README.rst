.. -*- mode: rst -*-

About
==========================================

``SimpleCV'' is a open source cross platform machine vision framework in python

The purpose of the ``simplecv-tutorial`` subproject is to learn
how to apply computer vision to practical situations using the
tools implemented in the ``SimpleCV`` framework.

The target audience is those new to computer vision but also has the ability
to be extended to more advanced computer vision tasks.


Building the tutorial
==========================================

You can build the HTML and PDF (requires pdflatex) versions of this
tutorial by installing sphinx (1.0.0+)::

  $ sudo pip install -U sphinx

Then for the html variant::

  $ make html


If you want to rebuild make sure you clean::

  $ make clean
  $ make html


Auto Building the tutorial
==========================================

If you are able to push to the master branch at:
http://github.com/ingenuitas/simplecv-examples

Then it should autobuild soon after and be found at:
http://simplecv-examples.readthedocs.org
