import threading
import time

def A(name,family):
    for i in range(10):
        print("Hello",name,family)

def B():
    for i in range(10):
        print("Bye Bye")

t1 = threading.Thread(target=A, args=["kia","keynia"])
t2 = threading.Thread(target=B)

t1.start()
time.sleep(1)
t2.start()