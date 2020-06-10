#to install reverse engineering tools
#BY KAUNG KHANT ZAW
import os
import sys
#Feel free to do better than me
def func():
    print (''' /$$$$$$                                         
 /$$___$$                                        
| $$  \ $$  /$$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$$ 
| $$$$$$$$ /$$_____/|____ /$$/ /$$__  $$| $$__  $$
| $$__  $$|  $$$$$$    /$$$$/ | $$  \ $$| $$  \ $$
| $$  | $$ \____  $$  /$$__/  | $$  | $$| $$  | $$
| $$  | $$ /$$$$$$$/ /$$$$$$$$|  $$$$$$/| $$  | $$
|__/  |__/|_______/ |________/ \______/ |__/  |__/
BY KAUNG KHANT ZAW''')
    print ('''1. CLANG 2. RADARE 3. NASM 
4. TO INSTALL ALL PROGRAMS
0. EXIT PROGRAM''')
    global bubu
    bubu = int(input('kali>>> '))
    if bubu == 1:
        os.system('sudo apt install clang')
    elif bubu == 2:
        os.system('sudo apt install radare2')
    elif bubu == 3:
        os.system('sudo apt install nasm')
    elif bubu == 4:
        os.system('sudo apt install clang radare2 nasm')
    elif bubu == 0:
        exit()
    else:
        print ('Invalid...')
while True:
    func()
else:
    exit()
