#to install database assement tools
#BY KAUNG KHANT ZAW
import os
import sys
print (''' /$$$$$$                                         
 /$$___$$                                        
| $$  \ $$  /$$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$$ 
| $$$$$$$$ /$$_____/|____ /$$/ /$$__  $$| $$__  $$
| $$__  $$|  $$$$$$    /$$$$/ | $$  \ $$| $$  \ $$
| $$  | $$ \____  $$  /$$__/  | $$  | $$| $$  | $$
| $$  | $$ /$$$$$$$/ /$$$$$$$$|  $$$$$$/| $$  | $$
|__/  |__/|_______/ |________/ \______/ |__/  |__/''')
print ("BY KAUNG KHANT ZAW")
def fuc():
    print ('''1. JSQL 2. SQLMAP 3. sqlite
4. TO ALL PROGRAMS
0. EXIT PROGRAM''')
    global num_num
    num_num = int(input('kali>>> '))
    if num_num == 1:
        os.system('sudo apt install jsql')
    elif num_num == 2:
        os.system('sudo apt install sqlmap')
    elif num_num == 3:
        os.system('sudo apt install sqlite')
    elif num_num == 4:
        os.system('sudo apt install jsql sqlmap sqlite')
    elif num_num == 0:
        exit()
    else:
        print('Invalid...')
while True:
    fuc()
else:
    exit()
