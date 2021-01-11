from tkinter import *
import datetime
import requests


response = requests.get("https://www.usom.gov.tr/url-list.txt",verify=False)
folder = open("bad.txt","w")
folder.write(str(response.content))
folder.close()

def check_it():
    folder = open("bad.txt","r")
    content = folder.read()
    folder.close()
    ip = entry1.get()
    today = datetime.datetime.now

    if str(ip) in content:
        folder = open("log.txt","a")

        rex = str(ip)+" malicious\nDate: "+str(today)+"\n"
        folder.write(rex)
        folder.close()
        v.set("ip address contains malware")
    else:
        folder = open("log.txt","a")

        rex = str(ip)+"not malicious\nDate: "+str(today)+"\n"
        folder.write(rex)
        folder.close()
        v.set("ip address is safe not contains malware")


top = Tk()
top.title("WosberbonDesu IP Control")
B = Button(top,text = "Check",command = check_it)
B.place(x = 60, y = 60)
B.pack()
label1 = Label(top, text= "Enter the ip address to check:")
label1.place(x=60,y=80)
label1.pack()
entry1 = Entry(top)
entry1.place(x=60,y=90)
entry1.pack()
v = StringVar()
entry2 = Entry(top,textvariable=v)
entry2.place(x=60,y=100)
entry2.pack()
top.mainloop()