all: big nb sanitize

big: # make the pdf
	pdflatex --shell-escape PyConTutorial.tex

nb: # unzip the notebook
	unzip iPythonNB.zip

ipynb: # zip the notebook
	zip iPythonNB.zip PyConTutorial.ipynb

sanitize: # clean up the latex garbage
	rm -rf *.toc *.out *.vrb *.nav *.aux *.snm *.log *flymake.* *.py~ 

small: big ipynb sanitize # shrink everything - do this before commit
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dQUIET -dBATCH -sOutputFile=PyConTutorialSmall.pdf PyConTutorial.pdf
	rm PyConTutorial.pdf

clean: #like it should be
	rm -rf *.toc *.out *.vrb *.nav *.aux *.snm *.log *flymake.* *.py~ *.pdf