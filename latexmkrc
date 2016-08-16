$pdf_mode = 1;
@default_files = ('report_template.tex');
@cus_dep_list = (@cus_dep_list, "glo gls 0 makenomenclature");
sub makenomenclature {
   system("makeindex $_[0].glo -s nomencl.ist -o $_[0].gls"); }
@generated_exts = (@generated_exts, 'glo');
