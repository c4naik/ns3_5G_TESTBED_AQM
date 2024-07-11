python3 delayscript.py Udponoff1.tr Udponoff2.tr 
# python3 delayscript.py Http1.tr Http2.tr
# python3 delayscript.py Ftp1.tr Ftp2.tr 
python3 delayscript.py Gaming1.tr Gaming2.tr
python3 delayscript.py Video1.tr Video2.tr
python3 delayscript.py Dash1.tr Dash2.tr
# python3 delayscript.py Tcpbulk1.tr Tcpbulk2.tr
python3 delayscript.py Voip1.tr Voip2.tr

gnuplot -e "name ='Udponoff'" -e "datafile='Udponoff-delay.csv'" plot_delay.gp 
gnuplot -e "name ='Gaming'" -e "datafile='Gaming-delay.csv'" plot_delay.gp 
gnuplot -e "name ='Video'" -e "datafile='Video-delay.csv'" plot_delay.gp 
gnuplot -e "name ='Dash'" -e "datafile='Dash-delay.csv'" plot_delay.gp 
gnuplot -e "name ='Voip'" -e "datafile='Voip-delay.csv'" plot_delay.gp 
# gnuplot -e "name ='Http'" -e "datafile='Http-delay.csv'" plot_delay.gp 
# gnuplot -e "name ='Tcpbulk'" -e "datafile='Tcpbulk-delay.csv'" plot_delay.gp 
# gnuplot -e "name ='Ftp'" -e "datafile='Ftp-delay.csv'" plot_delay.gp 
