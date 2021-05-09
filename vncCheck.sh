var=$(ps -ef | grep /usr/bin/x11vnc | wc -l)  				# check if vnc sessions is open
var=$((var-1))  											# -1 for the ps session to get only the open sessions 
today=$(date)  												# get the date and time of today 


if [ $var -gt 0 ]; then
	echo $today" VNC server is ON "$var" sessions open"
	exit

else
	echo $today" VNC server is OFF "$var" sessions are open --> starting new VNC session" >> log.log
	$(/usr/bin/x11vnc)
	# $(/usr/bin/x11vnc -bg -reopen -forever)
	exit
fi

#EXAMPLES
#ps -ef | grep x11 | awk '{print $2}' | sed -n 2p
#ps -ef | grep x11 | awk '{print $2}' | wc -l

#export DISPLAY=:0.0; x11vnc -shared -forever -usepw -ncache 10
#x11vnc
