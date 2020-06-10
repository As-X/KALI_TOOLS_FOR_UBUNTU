#to add kali linux repository
#by aszon (Kaung Khant Zaw)
import os
#os.system("grep -v '#' /etc/apt/sources.list | sort -u")
#os.system('echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee /etc/apt/sources.list')
#os.system('echo "deb http://http.kali.org/kali kali-last-snapshot main non-free contrib" | sudo tee /etc/apt/sources.list')
#os.system('echo "deb http://http.kali.org/kali kali-experimental main non-free contrib" | sudo tee -a /etc/apt/sources.list')
#os.system('apt update')
os.system("apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
os.system("echo '# Kali linux repositories | Added by Kaung Khant Zaw\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
os.system('sudo apt update')
