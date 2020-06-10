#to install wireless attacks tools
#BY KAUNG KHANT ZAW
import os
import sys
def function():
    print (''' /$$$$$$                                         
 /$$___$$                                        
| $$  \ $$  /$$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$$ 
| $$$$$$$$ /$$_____/|____ /$$/ /$$__  $$| $$__  $$
| $$__  $$|  $$$$$$    /$$$$/ | $$  \ $$| $$  \ $$
| $$  | $$ \____  $$  /$$__/  | $$  | $$| $$  | $$
| $$  | $$ /$$$$$$$/ /$$$$$$$$|  $$$$$$/| $$  | $$
|__/  |__/|_______/ |________/ \______/ |__/  |__/''')
    print ('BY KAUNG KHANT ZAW')
    print ('''1. AIRCRACK-NG 2. BULLY 3. FERN-WIFI-CRACKER 4. REAVER 5. WIFITE
6. KISMET 7. SPOOFTOOPH 8. PIXIEWPS
9. TO INSTALL ALL PROGRAMS
0. EXIT PROGRAM''')
    global number_no
    number_no = int(input('kali>>> '))
    if number_no == 1:
        os.system('sudo apt install aircrack-ng')
    elif number_no == 2:
        os.system('sudo apt install bully')
    elif number_no == 3:
        os.system('sudo apt install fern-wifi-cracker')
    elif number_no == 4:
        os.system('sudo apt install reaver')
    elif number_no == 5:
        os.system('sudo apt install wifite')
    elif number_no == 6:
        os.system('sudo apt install kismet')
    elif number_no == 7:
        os.system('sudo apt install spooftooph')
    elif number_no == 8:
        os.system('sudo apt install pixiewps')
    elif number_no == 9:
        os.system('sudo apt install reaver wifite kismet spooftooph pixiewps bully fern-wifi-cracker aircrack-ng')
    elif number_no == 0:
        exit()
    else:
        print ('Invalid...')
while True:
    function()
else:
    exit()
