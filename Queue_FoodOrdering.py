'''Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
Use this video to get yourself familiar with multithreading in python

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']'''

from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.buffer=deque()
    def enqueue(self,value):
        self.buffer.appendleft(value)
    def dequeue(self):
        return self.buffer.pop()
    def is_Empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)
    
q=Queue()

def place_orders():
    orders = ['pizza','samosa','pasta','biryani','burger']
    for x in orders:
        q.enqueue(x)
        print("Placing Order: ",x)
        time.sleep(0.5)
    print("All orders placed!!")
    return

def serve_orders(): 
    print("Serving Order : ",q.dequeue())
    time.sleep(2)
    if not q.is_Empty():
        serve_orders()
    return

t1=threading.Thread(target=place_orders)
t2=threading.Thread(target=serve_orders)

t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()
print("All orders Served!!")
