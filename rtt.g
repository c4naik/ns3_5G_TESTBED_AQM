set title "RTT vs Time"
set xlabel "Time"
set ylabel "RTT"
set grid
set term png
set output "rtt_vs_time.png"
plot "rtt_vs_time.txt" using 2:1 with lines title "RTT"

