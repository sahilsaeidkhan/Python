import threading
import time

def func(seconds):
    print("Just trying multithreading",seconds)
    print("")
    time.sleep(seconds)


t1 = threading.Thread(target=func,args=[3])
t2 = threading.Thread(target=func,args=[4])

t1.start()
t2.start()


t1.join()
t2.join()

print("Done")