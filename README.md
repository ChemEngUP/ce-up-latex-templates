# Chemical Engineering @ UP LaTeX templates

## Quickstart on Overleaf

Download the latest release from "Releases". This .zip file can be uploaded directly to [Overleaf](overleaf.com) and should compile with no further work.

## To compile the document locally

To compile the report template document you need to run `samplefigure.py` to create the `samplefigure.pdf` file.

A full compile of the sample document involves running

    pdflatex report_template
    biber report_template
    makeindex report_template.nlo -s nomencl.ist -o report_template.nls
    pdflatex report_template
    pdflatex report_template
    
The multiple runs of `pdflatex` is so that the page numbers and cross-references are handled correctly.

You can also automate these tasks using [arara](https://github.com/cereda/arara) or `latexmk`. Use the tool which is already installed in your system.

Always ensure that you are using the most recent version by downloading from [GitHub](https://github.com/ChemEngUP/ce-up-latex-templates/)
