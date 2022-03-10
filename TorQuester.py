#!/bin/python3

#made to simulate TOR traffic from various nodes to a specified web page
#replace "http://httpbin.org/ip" with any page to simulate traffic
#usage: ./TorQuester.py <https://url.com>

import requests
import time
import subprocess
import sys

def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

i = 1
while i < 4:
	try:
		session = get_tor_session()
		print("TOR request sending.")
		print(session.get(sys.argv[1]).text)
		print("TOR response received.")
		# Following prints your TOR public IP
		print("Current TOR IP: ", i)
		print(session.get("http://httpbin.org/ip").text)
		# Following prints your normal public IP
		print("Home IP:")
		print(requests.get("http://httpbin.org/ip").text)
		time.sleep(1)
		subprocess.run(["sudo", "service", "tor", "restart"])
		time.sleep(3)
		session = get_tor_session()
		i = i + 1
		time.sleep(1.5)
	except KeyboardInterrupt:
		print('\n')
		print('\nUser interrupted process -- Exiting!')
		break