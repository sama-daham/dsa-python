class Queue:
    #FIFO
    def __init__(self, size):
        self.size = size
        self.array = [None]*size
        self.length = 0

    def enqueue(self,val):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.array[self.length]=val
        self.length+=1

        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.array[0]
        for i in range (self.length-1):
            self.array[i]=self.array[i+1]
        self.length-=1
        self.array[self.length]=None
        return item
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.array[0]


    def is_empty(self):
        return self.length==0
    
    def is_full(self):
        return self.length==self.size
    
    def __repr__(self):
        return str(self.array[:self.length])
