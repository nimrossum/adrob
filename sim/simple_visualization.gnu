set xrange [-1:1]
set yrange [-1:1]
set terminal png

plot "points.dat" with points title "points", \
 "trajectory.dat" with vectors title "robot trajectory"
