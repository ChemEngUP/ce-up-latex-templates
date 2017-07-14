$pdf_mode = 1;
@default_files = ('report_template.tex');

add_cus_dep('nlo', 'nls', 0, 'makenlo2nls');
sub makenlo2nls {
  system("makeindex -s nomencl.ist -o \"$_[0].nls\" \"$_[0].nlo\"");
}
