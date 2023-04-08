set encoding iso_8859_1
set term postscript eps enhanced color "Times-Roman, 32"
set output "Sr_EXAFS-k.eps"
set xlabel "k ({\305} )" offset 0,0.5
set ylabel "chi(k)" offset 2,0
set xrange [2:14]
set xtics offset 0,0.2
set key font ",15"
set label "-1" font ",14" at 8.35,-3.3
plot 'Sr-EXAFS-2_OUTPUT-k.dat' u 1:3 pt 5 ps 0.5 lc rgb "blue" title \
"SrAl0.5Nb0.5O3 - Sr-EXAFS-k (EXP)", 'Sr-EXAFS-2_OUTPUT-k.dat' u 1:2 w l lw 2 lc rgb "red" title "SrAl0.5Nb0.5O3 - Sr-EXAFS-k (RMC)"
