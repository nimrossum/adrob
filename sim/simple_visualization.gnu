set xrange [-1:1]
set yrange [-1:1]
set terminal png
plot "trajectory.dat" with vectors title "robot trajectory"
