#!/usr/bin/python3

import socket

def banner(host,port):
    s = socket.socket()
    s.connect((host, int(port)))
    s.settimeout(7)
    print(s.recv(4096)).strip('b', "\r\n'")

def main():
    try:
        host = input("Please enter the target IP address: \n")
        port = str(input("Please enter the target port: \n"))
        banner(host, port)
    except KeyboardInterrupt:
        print('User iterrupted the transmission.')

main()