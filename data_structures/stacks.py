class Stack:
    #LIFO
    def __init__(self, size):
        self.size = size
        self.array = [None]*size
        self.length = 0
    
    def push(self, val):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.array[self.length] = val
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        self.length -= 1
        val = self.array[self.length]
        self.array[self.length] = None
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.array[self.length-1]
    
    def is_empty(self):
        return self.length ==0
    
    def is_full(self):
        return self.length == self.size

    def __repr__(self):
        return str(self.array[:self.length])

