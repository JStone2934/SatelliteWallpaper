import threading
import time

def print_111():
    while 1:
        print('1111')
        time.sleep(1)
def print_222():
    while 1:
        print('222')
        time.sleep(1)

threads = []

t1 = threading.Thread(target=print_111)
threads.append(t1)
t2 = threading.Thread(target=print_222)
threads.append(t2)
print("sfyuag")
if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
print ("退出线程")
