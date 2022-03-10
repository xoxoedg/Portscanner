import socket
import termcolor
import os


def scan(target, ports):
    print('\n' + " Starting Scan For " + str(target))
    for port in range(1, ports):
        scan_port(target , port)


def scan_port(ipadress, port):
    try:
        sock = socket.socket()
        sock.connect((ipadress, port))
        print("[+] Port open " + str(port))
        sock.close()
    except:
        pass


targets = input("[*] Enter Targets to Scan(split them by ',' ): ")
ports = int(input("[*] Enter How many Ports you want to Scan: "))
if "," in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"), "green"))
    for ip_adress in targets.split(","):
        scan(ip_adress.strip(" "), ports)
else:
    scan(targets, ports)

