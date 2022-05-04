class Node:
    def __init__(self, Data=None, Next=None):
        self.data = Data
        self.Next = Next

class Linked_List:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def remove_at_beginning(self):
         if self.head == None:
            print("Empty Linked List")
            return
         self.head = self.head.Next
        
    def insert_at_end(self, data):
        itr = self.head
        if self.head == None:
            self.insert_at_beginning(data)
            return
        while itr.Next!= None:
            itr = itr.Next
        itr.Next = Node(data, None)
    
    def remove_at_end(self):
        itr = self.head
        while itr.Next.Next!= None:
            itr = itr.Next
        itr.Next = None

    def insert_after_value(self, data_after, data_insert):
        if self.head == None:
            print("Empty Linked List")
            return
        
        itr = self.head
        while itr.data !=data_after:
            itr=itr.Next
        node = Node(data_insert, itr.Next)
        
        itr.Next = node
    
    def remove_by_value(self, data):
        itr = self.head
        if self.head == None:
            print("Empty Linked List")
            return
        
        while itr.Next!=None and itr.Next.data !=data :
            itr = itr.Next
        if itr.Next==None: print("Element does not exist")
        else: itr.Next = itr.Next.Next
        
    
    def insert_values(self, data_list):
        itr = self.head
        for data in data_list:
           self.insert_at_end(data)
            
    def Print(self):
        itr = self.head
        while itr != None:
            print(str(itr.data) + '--->', end='')
            itr=itr.Next

ll= ["banana","mango","grapes","orange"]
ll1 = Linked_List()
ll1.insert_values(ll)
ll1.insert_after_value('mango','apple')
ll1.remove_by_value('orange')
ll1.remove_by_value("figs")

ll1.Print()
