# Install VNC on Ubuntu and configure with guacamole LB
Apache Guacamole guide
This guide has been tested on Ubuntu 18 LTS

Step 1 - download the files [ vnc-install.py, vncCheck.sh ]
Step 2 - create folder vnc in your home dir
```
$ mkdir ~/vnc/
```
Installation
Step 1 - run the following command:
Step 2 - if you need proxy server for update and installing please type y/yes Step 3 - for update the PC type y/yes or press ENTER to skip
Step 4 - on this step the installation will ask how many IP's you about to configure for the LoadBalancer on the guacamole

> Note: if you don't need to configure Loadbalancer or you wish to allow access to ANY IP just type enter
> 

Step 5 - the installation is now finished wait 1 minute for the service to start then try to log in the machine
Step 6 - Configure your Ubuntu machine that it will not lock herself \ shut down screen. Go to settings, Privacy and disable Lockscreen
go to Power and make sure that "turn off screen" option is set to Never.


## Create Service for VNC

to create a service for VNC so you wont lose connection even when you restarted, create a file called x11vnc.service
in the following locations;
```
/etc/systemd/system/
/lib/systemd/system/
```
the following service code should be:
```
[Unit]
Description=Start x11vnc at startup.
After=multi-user.target
[Service]
Type=simple
ExecStart=/usr/bin/x11vnc -bg -reopen -forever -rfbport 5900
[Install]
WantedBy=multi-user.target
```

once you're done, save it.
and type the following commands:
```
$ sudo systemctl enable x11vnc.service
$ sudo systemctl daemon-reload
$ sudo systemctl start x11vnc.service
```





## Debug(known issues) section:

* Make sure that once you've downloaded the file, you give a+x to vncCheck.sh
* x11vnc DO NOT SUPPORT IN WAYLAND so please use X.Org (how to do so? log out and change in the gear icon)
* If you by mistake logged out, it will disconnect your machine from network, to solve it use the commands below;
```
$ nmcli connection modify [CONNECTION-NAME] connection.permissions ''
$ nmcli connection modify [CONNECTION-NAME] connection.autoconnect yes
$ nmcli connection modify [CONNECTION-NAME] connection.autoconnect-priority 10
```

* if you're having an issue with port 5900 on VNC, please refer the application to 5901.
```
$ /usr/bin/x11vnc -bg -reopen -forever -rfbport 5901
```
* If you want to turn on log for issues you might run into, use the flag -o <FILE_LOCATION>
```
$ touch /var/log/x11vnc.log
$ sudo /usr/bin/x11vnc -bg -reopen -forever -o /var/log/x11vnc.log
```

* if you're having issue with the following error: **stack smashing detected** run the x11vnc with the flags: -noxrecord -xkb
```
$ sudo /usr/bin/x11vnc -bg -reopen -forever -noxrecord -xkb -o /var/log/x11vnc.log
```
* If The VNC refuse connection via Sharing \ x11vnc due to bad or need to change encryption
```
$ gsettings set org.gnome.Vino require-encryption false
```
