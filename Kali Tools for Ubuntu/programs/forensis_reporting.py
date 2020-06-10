#to install forensis and reporint tools
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
    print ('''1.AUTOPSY 2. HASHDEEP 3. BINWALK 4. BULK-EXTRACTOR 5. CUTYCAPT
6. PIPAL 7. MALTEGO 8. FARADAY 9. PDFID 10. GUYMAGER
11. TO INSTALL ALL PROGRAM
0. EXIT PROGRAM''')
    global  kaka
    kaka = int(input("kali>>> "))
    if kaka == 1:
        os.system('sudo apt install autopsy')
    elif kaka == 2:
        os.system('sudo apt install hashdeep')
    elif kaka == 3:
        os.system('sudo apt install binwalk')
    elif kaka == 4:
        os.system('sudo apt install bulk-extractor')
    elif kaka == 5:
        os.system('sudo apt install cutycapt')
    elif kaka == 6:
        os.system('sudo apt install pipal')
    elif kaka == 7:
        os.system('sudo apt install maltego')
    elif kaka == 8:
        os.system('sudo apt install faraday')
    elif kaka == 9:
        os.system('sudo apt install pdfid')
    elif kaka == 10:
        os.system('sudo apt install guymager')
    elif kaka == 11:
        os.system('sudo apt install autopsy hashdeep binwalk bulk-extractor cutycapt pipal maltego faraday pdfid guymager')
    elif kaka == 0:
        exit()
    else:
        print ('Invalid...')
while True:
    funfun()
else:
    exit()
