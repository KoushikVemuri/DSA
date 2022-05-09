class Hash_table:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def Hash_fun(self, Key):
        return int(Key)//10
    
    def __setitem__(self, Key, Value):
        Found = False
        h = self.Hash_fun(Key)
        for idx, element in enumerate(self.arr[h]):
            if element[0]==Key:
                self.arr[h][idx][1]= Value
                Found = True
        if not Found:
            self.arr[h].append([Key, Value])
    
    def __getitem__(self, Key):
        h = self.Hash_fun(Key)
        for element in self.arr[h]:
            if element[0] == Key:
                return element[1]
