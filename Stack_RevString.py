'''Write a function in python that can reverse a string using stack data structure. Use Stack class'''

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
        
s = input('Enter a String to reverse')
Rev_Stack = Stack()
for x in s:
    Rev_Stack.push(x)
Rev_s = ""   
for i in range(len(s)):
    Rev_s+= Rev_Stack.pop()
print(Rev_s)
