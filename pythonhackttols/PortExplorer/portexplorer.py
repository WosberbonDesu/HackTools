import socket

port_list = []
banner_list = []

folder = open("ip.txt","r")
ips = folder.read()
folder.close()
for ip in ips.splitlines():
    print(ip)
    for port in range(1,25):

        try:
            skt = socket.socket()
            skt.connect((str(ip),int(port)))
            banner = skt.recv(1024)
            banner_list.append(str(banner))
            port_list.append(str(port))
            skt.close()
            print(port)
            print(banner)

            if "SSH" in str(banner):
                print("system can be linux or network device")
                log = str(ip)+"\n"
                folder = open("linux.txt","a")
                folder.write(log)
                folder.close()

        except:
            pass

print(port_list)
print(banner_list)
