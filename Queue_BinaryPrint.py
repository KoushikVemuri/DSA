'''Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010
Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

You also need to add front() function in queue class that can return the front element in the queue.'''


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
    def front(self):
        return self.buffer[-1]
    
q=Queue()

q.enqueue("1")
while q.front() != "1010":
    val = q.dequeue()
    print(val)
    q.enqueue(val + "0")
    q.enqueue(val + "1")
    
print(q.dequeue())
