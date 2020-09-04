import threading
import time
xx=[]
def msg():
    while t !=0:
        x = input()
        xx.append(x)
        print ("time's up")
        time.sleep(1)#just enough to show the above msg
        print(xx)
    exit()
t=threading.Timer(3.0,msg)
t.start()