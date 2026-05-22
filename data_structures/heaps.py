class Heap:
    #max heap
    def __init__(self, size):
        self.size = size
        self.array = [None]*size
        self.length = 0
    '''
    i parent:    (i-1)//2
    left child:  2*i+1
    right child: 2*i +2
    '''

    def insert(self,val):
        if self.is_full():
            raise OverflowError("Heap is full")
        self.array[self.length] = val
        self.length+=1
        i = self.length-1
        #bubble up
        while i>0:
            parent_index = (i-1)//2
            if self.array[i]>self.array[parent_index]:
                #can swap in python: a,b = b,a
                self.array[i], self.array[parent_index]=self.array[parent_index], self.array[i]
                i=parent_index
            else:
                break

    def pop(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        val = self.array[0]
        self.array[0], self.array[self.length-1] = self.array[self.length-1], self.array[0]
        self.array[self.length-1] = None
        self.length -= 1
        i = 0
        #bubble down
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < self.length and self.array[left] > self.array[largest]:
                largest = left
            if right < self.length and self.array[right] > self.array[largest]:
                largest = right
            if largest == i:
                break
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            i = largest
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.array[0]

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.size

    def __repr__(self):
        return str(self.array[:self.length])
