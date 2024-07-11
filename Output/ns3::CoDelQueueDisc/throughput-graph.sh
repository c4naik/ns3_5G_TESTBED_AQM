python3 thscript.py "Udponoff2.tr"
python3 thscript.py "Gaming2.tr"
python3 thscript.py "Voip2.tr"
python3 thscript.py "Video2.tr"
python3 thscript.py "Dash2.tr"
# python3 thscript.py "Http2.tr"
# python3 thscript.py "Ftp2.tr"
# python3 thscript.py "Tcpbulk2.tr"

#generate graph
gnuplot -e "name ='Udponoff'" -e "datafile='Udponoff-throughput.csv'" plot_throughput.gp 
gnuplot -e "name ='Gaming'" -e "datafile='Gaming-throughput.csv'" plot_throughput.gp 
gnuplot -e "name ='Voip'" -e "datafile='Voip-throughput.csv'" plot_throughput.gp
gnuplot -e "name ='Video'" -e "datafile='Video-throughput.csv'" plot_throughput.gp
gnuplot -e "name ='Dash'" -e "datafile='Dash-throughput.csv'" plot_throughput.gp
# gnuplot -e "name ='Http'" -e "datafile='Http-throughput.csv'" plot_throughput.gp
# gnuplot -e "name ='Ftp'" -e "datafile='Ftp-throughput.csv'" plot_throughput.gp
# gnuplot -e "name ='Tcpbulk'" -e "datafile='Tcpbulk-throughput.csv'" plot_throughput.gp
        
