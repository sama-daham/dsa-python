class Array:
    def __init__ (self, size):
        self.size = size
        self.array = [None] * size
        self.length = 0 #tracks filled
    
    def get(self, index):
        if not (self.length > index >= 0):
            raise IndexError("Index out of range")
        return self.array[index]

    def set(self, index, val):
        if not (self.size > index >= 0):
            raise IndexError("Index out of range")
        self.array[index] = val

    def append(self, val):
        if self.is_full():
            raise OverflowError("Array is full")
        self.array[self.length] = val
        self.length += 1

    def insert(self, index, val):
        if self.is_full():
            raise OverflowError("Array is full")
        if not (self.size > index >= 0):
            raise IndexError("Index out of range")
        for i in range(self.length-1, index-1, -1):
            self.array[i+1] = self.array[i]
        self.array[index] = val
        self.length += 1

    def delete(self, index):
        if not (self.size > index >= 0):
            raise IndexError("Index out of range")
        for i in range(index, self.length-1):
            self.array[i] = self.array[i+1]
        self.length -= 1
        self.array[self.length] = None
    
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

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.size

    def __len__(self):
        return self.length

    def __repr__(self):
        return str(self.array[:self.length])

    