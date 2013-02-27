Deps
-------------------------------------
sudo apt-get tex-live-full
sudo apt-get latex-beamer
sudo apt-get okular //PDF viewer
sudo apt-get emacs23-acutex


acutex seems to be nice in emacs. 


You also need to install the minted package for source code highlighting

https://code.google.com/p/minted/downloads/detail?name=minted-v1.7.zip&can=2&q=

run make and move minted.sty to the build director.
I put a copy in the repo because I am lazy.

----------------------
To render

pdflatex --shell-escape PyConTutorial.tex 

pdflatex may whine if the style file is not found.
