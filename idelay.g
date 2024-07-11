set title "Delay vs Time"
set xlabel "Time"
set ylabel "Delay"
set grid
set term png
set output "delay_vs_time.png"
plot "delay_vs_time.txt" using 2:1 with lines title "Delay"

