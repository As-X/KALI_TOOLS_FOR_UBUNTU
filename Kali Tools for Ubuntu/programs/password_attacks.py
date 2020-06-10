#to install password attack tools
#BY KAUNG KHANT ZAW
import os
import sys
def funfun():
    print ('''	 /$$$$$$                                         
    	 /$$___$$                                        
    	| $$  \ $$  /$$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$$ 
    	| $$$$$$$$ /$$_____/|____ /$$/ /$$__  $$| $$__  $$
    	| $$__  $$|  $$$$$$    /$$$$/ | $$  \ $$| $$  \ $$
    	| $$  | $$ \____  $$  /$$__/  | $$  | $$| $$  | $$
    	| $$  | $$ /$$$$$$$/ /$$$$$$$$|  $$$$$$/| $$  | $$
    	|__/  |__/|_______/ |________/ \______/ |__/  |__/''')
    print ('''1. CHNTPW 2. HASHCAT 3. HASHID 4. HASH-IDENTIFIER 5. SAMDUMP2 6. HYDRA 7. CRUNCH 8. CEWL 9. patator 10. JOHN
11. MEDUSA 12. NCRACK 13. OPHCRACK 14. WORDLISTS 15. MIMIKATZ
16. TO INSTALL ALL PROGRAMS 
0. EXIT PROGRAM''')
    global number
    number = int(input('kali>>> '))
    if number == 1:
        os.system('sudo apt install chntpw')
    elif number == 2:
        os.system('sudo apt install hashcat')
    elif number == 3:
        os.system('sudo apt install hashid')
    elif number == 4:
        os.system('sudo apt install hash-identifier')
    elif number == 5:
        os.system('sudo apt install samdump2')
    elif number == 6:
        os.system('sudo apt install hydra')
    elif number == 7:
        os.system('sudo apt install crunch')
    elif number == 8:
        os.system('sudo apt install cewl')
    elif number == 9:
        os.system('sudo apt install patator')
    elif number == 10:
        os.system('sudo apt install john')
    elif number == 11:
        os.system('sudo apt install medusa')
    elif number == 12:
        os.system('sudo apt install ncrack')
    elif number == 13:
        os.system('sudo apt install ophcrack')
    elif number == 14:
        os.system('sudo apt install wordlists')
    elif number == 15:
        os.system('sudo apt install mimikatz')
    elif number == 16:
        os.system('sudo apt install wordlists mimikatz ophcrack ncrack john medusa patator cewl crunch')
        os.system('sudo apt install samdump2 hash-identifier hashid hashcat chntpw')
    elif number == 0:
        exit()
    else:
        print ("Invalid...")
while True:
    funfun()
else:
    exit()
