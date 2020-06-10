#to install sniffing and spoofing tools
#BY KAUNG KHANT ZAW
import os
import sys
def funfun():
    print(''' /$$$$$$
 /$$___$$
| $$  \ $$  /$$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$$
| $$$$$$$$ /$$_____/|____ /$$/ /$$__  $$| $$__  $$
| $$__  $$|  $$$$$$    /$$$$/ | $$  \ $$| $$  \ $$
| $$  | $$ \____  $$  /$$__/  | $$  | $$| $$  | $$
| $$  | $$ /$$$$$$$/ /$$$$$$$$|  $$$$$$/| $$  | $$
|__/  |__/|_______/ |________/ \______/ |__/  |__/
BY KAUNG KHANT ZAW''')
    print ('''1. DNSCHEF 2. NETSNIFF-NG 3. BETTERCAP 4. ETTERCAP 5. MACCHANGER
6. WIRESHARK 7. RESPONDER 8. MITMPROXY 9. REBIND 10. SSLSPLIT 11. TCPREPLAY
12. TO INSTALL ALL PROGRAMS
0.EXIT PROGRAM''')
    global number
    number = int(input('kali>>> '))
    if number == 1:
        os.system('sudo apt install dnschef')
    elif number == 2:
        os.system('sudo apt install netsniff-ng')
    elif number == 3:
        os.system('sudo apt install bettercap bettercap-ui bettercap-dbgsym')
    elif number == 4:
        os.system('sudo apt install ettercap-common')
        os.system('sudo apt install ettercap-graphical')
    elif number == 5:
        os.system('sudo apt install macchanger')
    elif number == 6:
        os.system('sudo apt install wireshark wireshark-common wireshark-gtk')
    elif number == 7:
        os.system('sudo apt install responder')
    elif number == 8:
        os.system('sudo apt install mitmproxy')
    elif number == 9:
        os.system('sudo apt install rebind rebind-dbgsym')
    elif number == 10:
        os.system('sudo apt install sslsplit')
    elif number == 11:
        os.system('sudo apt install tcpreplay')
    elif number == 12:
        os.system('sudo apt install bettercap bettrecap-ui dnschef netsniff-ng bettercap-dbgsym')
        os.system('sudo apt install ettercap-common wireshark wireshark-dev wireshark-common wireshark-qt wireshark-gtk macchanger responder mitmproxy')
        os.system('sudo apt install tcpreplay sslsplit rebind rebind-dbgsym')
    elif number == 0:
        exit()
    else:
        print ('Invalid...')
while True:
    funfun()
else:
    exit()
