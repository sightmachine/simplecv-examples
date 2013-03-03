all: big nb sanitize

big: 
	pdflatex --shell-escape PyConTutorial.tex

nb:
	unzip iPythonNB.zip

ipynb: 
	zip iPythonNB.zip PyConTutorial.ipynb

sanitize:
	rm -rf *.toc *.out *.vrb *.nav *.aux *.snm *.log *flymake.* *.py~ 

small: big ipynb sanitize
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dQUIET -dBATCH -sOutputFile=PyConTutorialSmall.pdf PyConTutorial.pdf
	rm PyConTutorial.pdf

clean: 
	rm -rf *.toc *.out *.vrb *.nav *.aux *.snm *.log *flymake.* *.py~ *.pdf