class Array:
    def __init__ (self, size):
        self.size = size
        self.array = [None] * size
        self.length = 0 #tracks filled
    
    def get(self, index):
        if self.size>index>=0:
            return self.array[index]
        else:
            return -1
    
    def set(self, index, val):
        if self.size>index>=0:
            self.array[index]=val
        else:
            return "Error"
        
    def append(self, val):
        if self.length == self.size:
            return "Error: Full"
        self.array[self.length]=val
        self.length+=1
    
    def insert(self, index, val):
        if self.length == self.size:
            return "Error: Full"
        if self.size>index>=0:
            for i in range(self.length-1, index-1, -1):
                self.array[i+1] = self.array[i]
            self.array[index]=val
            self.length+=1
        else:
            return "Error"
    
    def delete(self, index):
        if self.size>index>=0:
            #for(int i=index; i<self.size; i++){self.array[i]=self.array[i+1]}
            for i in range(index, self.length-1):
                self.array[i] = self.array[i+1]
            self.length-=1
            self.array[self.length]= None
        else:
            return "Error"
    
    def find(self, val):
        for i in range(0, self.length):
            if self.array[i] == val:
                return i
        return -1
    
    def contains(self, val):
        for i in range(0,self.length):
            if self.array[i] == val:
                return True
        return False

    