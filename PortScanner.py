#!/usr/bin/python3

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(7)


#host = input("Please enter the IP you want to scan: \n")
#port = int(input("Please enter the port you want to scan: \n"))

def PortScan(port):
    if s.connect_ex((host,port)):
        print("The Port is closed.")
    else: 
        print("The Port is open.")

#PortScan(port)