import os 
import time

# print("do you want to configure proxy ? for external installation")
# ans = input()
# if ans == "y" or ans == "yes":
#     os.system("export http_proxy=http://<PROXY_URL:PORT>")
#     os.system("export https_proxy=http://<PROXY_URL:PORT>")

print("do you need proxy ? type y/yes")
prox = input()

update = str(input("do you want to update your pc? - [[y/yes to accept ENTER to skip]] "))
if update == "y" or update == "yes" or update == "Y" or update == "YES":
    if prox == "y" or prox == "yes":
        os.system("http_proxy=http://<PROXY_URL:PORT> apt-get update -y")
    else:
        print("installing updates")
        os.system("apt-get update -y")
else:
    print("OK no update needed")
    
if prox == "y" or prox == "yes":
    print("installing VNC-server")
    os.system("http_proxy=http://<PROXY_URL:PORT> apt-get install x11vnc -y")
else:
    print("installing VNC-server")
    os.system("apt-get install x11vnc -y")

amountOFip=1
print("if you about to connect to LoadBalancer please type the amount of ip's you need. to open for any host just type enter")
iplist = []
try:
    amountOFip = int(input())
    # x = amountOFip
    while amountOFip > 0:
        ip = input("Enter loadBalancerIP --> ")
        print("the ip is "+ ip + " approve? y/yes - ENTER or anything else to try again")
        approve = input()
        if approve == "y" or approve == "yes":
            amountOFip = amountOFip - 1
            iplist.append(ip)
            print("Saved")
    print(iplist)
    for a in iplist:
        os.system("ufw allow from "+ a + " to any port 5900")
        # print("ufw allow from "+ a + " to any port 5900")

except:
    # amountOFip = 1
    os.system("ufw allow 5900/tcp")
    os.system("ufw allow 5900/udp")

print("exporting display")
os.system("export DISPLAY=:0.0")

print("edit cronjob")
os.system("(crontab -l ; echo '* * * * * cd ~/vnc/ && ./vncStrig.sh')| crontab -")
time.sleep(3)
print("Installation is done please wait 1 minute and try to login")
