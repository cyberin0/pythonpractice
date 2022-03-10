#!/usr/bin/env python3
#Scans the local network via arp, then nmap scans all found addresses, including the user's victim machine.
#Linux only
#Assumes nmap is installed

import subprocess
import time
import os

#-----------------------
savefilearp=open("addresses.txt","w")#create temp arp-scan file
def arpscanner():
    i=1
    while i<6: #pings 5 times
        try:
            print('Sweeping the network.', '\nPining every second.')
            print('-----', 'Local ARP scan', i, "\n")
            addresses = subprocess.run(["ip", "n"], stdout=subprocess.PIPE, universal_newlines=True, text=True).stdout.strip("CompletedProcess(args=['ip', 'n'], returncode=0, stdout='')")
            time.sleep(1)
            savefilearp.write(str(addresses))
            i = 1+i
        except KeyboardInterrupt:
            print("\nUser interrupted the process. Quitting!")
            break
            pass

arpscanner() #run the arp scan
savefilearp.close()
time.sleep(.2)


#--------------------
savefilenmap=open("cybscannmap.txt", "w")#create nmap-scan file
def nmapper():
    i=1
    if i<2:
        try:
            print("Beginning the NMAP scan.", "\n", "Please be patient.")
            services = subprocess.run(["sudo", "nmap", "-sV", "-iL", "addresses.txt", "-T4", "-O"], stdout=subprocess.PIPE, universal_newlines=True, text=True).stdout.strip('CompletedProcess(args="sudo", "nmap", "-sV", "-iL", "addresses.txt", "-T4", "-O", returncode=0, stdout='')')
            savefilenmap.write(str(services))
        except KeyboardInterrupt:
            print("\nUser interrupted the process. Quitting!")
            pass

nmapper()
savefilenmap.close()


#--------------------
#delete all temp files
def fileremover():
    try:
        os.remove("addresses.txt")
        os.remove("cybscannmap.txt")
    except:
        pass

fileremover()
time.sleep(.2)
print('File removal complete', "\n", "Internal Network scan complete.")
