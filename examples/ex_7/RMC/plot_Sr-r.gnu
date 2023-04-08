set encoding iso_8859_1
set term postscript eps enhanced color "Times-Roman, 32"
set output "Sr_EXAFS-r.eps"
set xlabel "R ({\305})" offset 0,0.5
set ylabel "chi(r)" offset 2,0
set xtics offset 0,0.2
set key font ",15"
plot 'Sr-EXAFS-2_OUTPUT-r.dat' u 1:7 pt 5 ps 0.5 lc rgb "blue" title \
"SrAl0.5Nb0.5O3 - Sr-EXAFS-r (EXP)", 'Sr-EXAFS-2_OUTPUT-r.dat' u 1:4 w l lw 2 lc rgb "red" title "SrAl0.5Nb0.5O3 - Sr-EXAFS-r (RMC)"
