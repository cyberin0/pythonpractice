#!/bin/env/python3

import nmap

nm = nmap.PortScanner()
nm.command_line()


def main(host, port):
    host = input("Please enter the IP address to the command line.\n")
    print("You are scanning: ", host)

    scantype = input(""" \nWhat type of scan do you want to run?
                            1) SYN ACK
                            2) UDP
                            3) Comprehensive\n""")
    print("You will scan using the", input, "methodology\n")

    if scantype == '1':
        print("Nmap Version: ", nm.nmap_version())
        nm.scan(host, "1-1024", '-sS')
        print(nm.scaninfo())
        print("The Host is ", nm[host].state())
        print(nm[host].all_protocols())
        print(nm[host]['tcp'].keys())
    elif scantype == '2':
        print("Nmap Version: ", nm.nmap_version())
        nm.scan(host, "1-1024", '-sU')
        print(nm.scaninfo())
        print("The Host is ", nm[host].state())
        print(nm[host].all_protocols())
        print(nm[host]['udp'].keys())
    elif scantype == '3':
        print("Nmap Version: ", nm.nmap_version())
        nm.scan(host, "1-1024", '-v -sS -A')
        print(nm.scaninfo())
        print("The Host is ", nm[host].state())
        print(nm[host].all_protocols())
        print(nm[host]['tcp'].keys())
    elif scantype >= '4':
        print("Please enter a valid option.")



main()