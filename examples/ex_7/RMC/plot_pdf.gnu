set encoding iso_8859_1
set term postscript eps enhanced color "Times-Roman, 32"
set output "snao_pdf.eps"
set xlabel "R ({\305})" offset 0,0.5
set ylabel "G(r)" offset 2,0
set xtics offset 0,0.2
set xrange [1.5:20]
set yrange [-0.5:1.5]
set key font ",18"
set key at 19,1.4
plot 'snao_PDF1.csv' u 1:5 pt 5 ps 0.5 lc rgb "blue" title "SrAl0.5Nb0.5O3 - PDF \
(EXP)", 'snao_PDF1.csv' u 1:3 w l lw 2 lc rgb "red" title "SrAl0.5Nb0.5O3 - PDF (RMC)", \
