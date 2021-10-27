# -*- coding: utf-8 -*-
# Created By IzzSecurity
# This Is For Penetration Testing Tools

import socket
import os
import sys
from IPy import IP
from pyfiglet import Figlet

import colorama
from colorama import Fore

os.system("clear")

print(Fore.GREEN + " " )

custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('IzzScanner'))


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[Scanning Target] ' + str(target))
    for port in range(1,100):
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5) # We set time to 0.5 Or up to you if you want to change
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass

print ("             Port Scanner For Penetration Testing ")

print("")
target = input('[+] Enter Target/s To Scan (split multiple targets with ,) : ')
if ',' in target:
    for ip_add in target.split(','):
        scan(ip_add.strip(' '))
else:
     scan(target)
