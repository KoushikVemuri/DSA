'''Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class'''

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
        
s = input('Enter an Equation')
Check_Stack = Stack()
Balanced = True
for x in s:
    if x == '[' or x=='{' or x=='(':
        Check_Stack.push(x)
    elif x == ']':
        if Check_Stack.is_empty() or Check_Stack.pop()!='[':
            Balanced = False
            break
    elif x == '}':
        if Check_Stack.is_empty() or Check_Stack.pop()!='{':
            Balanced = False
            break  
    elif x == ')':
        if Check_Stack.is_empty() or Check_Stack.pop()!='(':
            Balanced = False
            break
if Balanced:
        print("Equation is balanced")
else:
        print("Equation is not balanced")
