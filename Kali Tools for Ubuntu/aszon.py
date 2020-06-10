#to run the main script
#by KAUNG KHANT ZAW
import os
import sys


def function():
    print(''' /$$$$$$                                         
 /$$___$$                                        
| $$  \ $$  /$$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$$ 
| $$$$$$$$ /$$_____/|____ /$$/ /$$__  $$| $$__  $$
| $$__  $$|  $$$$$$    /$$$$/ | $$  \ $$| $$  \ $$
| $$  | $$ \____  $$  /$$__/  | $$  | $$| $$  | $$
| $$  | $$ /$$$$$$$/ /$$$$$$$$|  $$$$$$/| $$  | $$
|__/  |__/|_______/ |________/ \______/ |__/  |__/''')
    print ('BY KAUNG KHANT ZAW')
    print ('''
0. To Add Kali Linux Repository
1. Information Gathering 
2. Vulnerability Analysis
3. Web Application Analysis
4. Password Attacks
5. Wireless Attacks
6. Reverse Engineering
7. Exploitation Tools
8. Sniffing & Spoofing Tools
9. Post Exploitation
10. Forensis And Reporting Tools
11. EXIT PROGRAM''')
    global get_no
    get_no = int(input("Enter your choice : "))
    if get_no == 1:
        os.system('sudo python3 programs/information_gathering.py')
    elif get_no == 0:
        os.system('sudo python3 programs/add_repository.py')
    elif get_no == 2:
        os.system('sudo python3 programs/vulnerability_analysis.py')
    elif get_no == 3:
        os.system('sudo python3 programs/web_application_analysis.py')
    elif get_no == 4:
        os.system('sudo python3 programs/password_attacks.py')
    elif get_no == 5:
        os.system('sudo python3 programs/wireless_attacks.py')
    elif get_no == 6:
        os.system('sudo python3 programs/reverse_engineering.py')
    elif get_no == 7:
        os.system('sudo python3 programs/exploitation_tools.py')
    elif get_no == 8:
        os.system('sudo python3 programs/sniffing_spoofing.py')
    elif get_no == 9:
        os.system('sudo python3 programs/post_exploitation.py')
    elif get_no == 10:
        os.system('sudo python3 programs/forensis_reporting.py')
    elif get_no == 11:
        exit()
    else:
        print ('Invalid...')
while True:
    function()
else:
    exit()
