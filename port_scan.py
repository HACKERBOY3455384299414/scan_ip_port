import socket
from IPy import IP 
from colorama import init, Fore, Style


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + ' 0 Scanning Target : ' + str(target))

    for port in range(1, 500):
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
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print(Fore.GREEN + "[+] Open Port " + str(port) + " : " + str(banner.decode().strip('\n')))
        except:
            print(Fore.GREEN + "[+] Open Port " + str(port))
    except:
        pass # ამით გამპგვაქვს მარტო ღია პორტები
        # print(Fore.RED + "[-]Port " + str(port) + " Is Closee")

targets = input(Fore.GREEN + "[+] Enter Targer/s To Scan(split multiple targets with ,): ")
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)

  
