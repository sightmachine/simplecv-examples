Deps
-------------------------------------
sudo apt-get tex-live-full
sudo apt-get latex-beamer
sudo apt-get okular //PDF viewer
sudo apt-get emacs23-auctex




You also need to install the minted package for source code highlighting

https://code.google.com/p/minted/downloads/detail?name=minted-v1.7.zip&can=2&q=

run make and move minted.sty to the build director.
I put a copy in the repo because I am lazy.

----------------------
To render

pdflatex --shell-escape PyConTutorial.tex 

pdflatex may whine if the style file is not found.

-----------------------
Resources:

- [http://tex.stackexchange.com/questions/73163/change-color-scheme-for-example-box-in-beamer](Color
Boxes)
- [http://tex.stackexchange.com/questions/83204/how-can-i-make-source-code-included-with-minted-copyable/83218#83218](Copy
Pasta Minted)
- [http://tex.stackexchange.com/questions/83204/how-can-i-make-source-code-included-with-minted-copyable/83218#83218](More
on minted)
- [http://ctan.math.utah.edu/ctan/tex-archive/macros/latex/contrib/minted/minted.pdf]
(More Minted)
- [http://piotrkazmierczak.com/2010/05/13/emacs-as-the-ultimate-latex-editor/screenshot_001/](AucTex)
-
[http://en.wikibooks.org/wiki/LaTeX/Floats,_Figures_and_Captions](Figures
and such.)
