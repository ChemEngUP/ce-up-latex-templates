# Chemical Engineering @ UP LaTeX templates

## Quickstart on Overleaf

Download the latest release from [Releases](https://github.com/ChemEngUP/ce-up-latex-templates/releases). This .zip file can be uploaded directly to [Overleaf](https://overleaf.com) and should compile with no further work.

## Quickstart on Windows: TeXstudio

### TeXstudio (TS) not installed yet?

Download a LaTeX distribution such as [MikTeX](https://miktex.org/download).
Download the latest version of [TeXstudio](https://texstudio.org/).

### With TS installed.

Open TS
On the ribbon follow Options-->Configure TeXstudio.
Under Build-->Default Compiler, select Latexmk. This will allow the report to compile correctly with nomenclature when clicking the Build&View button (or F5) on the toolbar for the first compile and Compile (or F6) for subsequent compiling.

If this raises the error that the 'perl.exe' could not be found, you might need to install perl and add it to your Path.
Download and install [Strawberry Perl](http://strawberryperl.com/).
After closing the installer window, open file explorer. Here right click on 'This PC' and select Properties. Click on 'Advanced system settings'. Go to the Advanced tab and click the Environment variables button at the bottom of the window. 
Here you will find a list of Variables. If 'Path' is not listed create a new variable with name Path and value C:\strawberry\perl\bin. If Path is already listed, select it-->Edit-->New and use the same value as before.
The latex files should now compile.

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
