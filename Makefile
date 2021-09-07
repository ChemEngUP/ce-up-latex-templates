texfiles=main.tex contents/*.tex

all: $(texfiles) upreport.sty graph/samplefigure.pdf
	latexmk main.tex

graph/samplefigure.pdf: samplefigure.py
	python samplefigure.py

dist: graph/samplefigure.pdf
	zip -r dist.zip README.md biblatex.cfg $(texfiles) latexmkrc report.bib graph samplefigure.py upreport.sty

clean:
	-rm graph/*.pdf
	-latexmk -c

.PHONY: all dist
