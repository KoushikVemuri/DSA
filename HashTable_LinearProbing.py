class Hash_table:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def Hash_fun(self, Key):
        return int(Key)//10
    
    def __setitem__(self, Key, Value):
        Found = False
        h = self.Hash_fun(Key)
        h1=h-1
        while self.arr[h]!=None:
            if h==h1:
                print("Array is full")
                return
            h=(h+1)%self.MAX
    
        self.arr[h] = [Key, Value]   
        
    
    def __getitem__(self, Key):
        h = self.Hash_fun(Key)
        h1=h-1
        while self.arr[h][0]!=Key:
            if h==h1:
                print("Element not found")
                return
            h=(h+1)%self.MAX
        return self.arr[h][1] 
