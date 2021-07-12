import multiprocessing as mp
import time

def do(num):
    # time.sleep(0.1)
    print(num)

def hello():
    # time.sleep(0.1)
    print("Hello")

if (__name__=='__main__'):
    i=0
    for j in range(1,6):
        p = mp.Process(target=do(i))
        q = mp.Process(target=hello)
        time.sleep(0.1)
        p.start()
        time.sleep(0.1)
        q.start()
        i +=1
