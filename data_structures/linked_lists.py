

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None
        self.length = 0
        #always starts empty

    def get_node(self, index):
        if index<0 or index>=self.length:
            return -1
        current_node = self.head
        i = index
        while i>0:
            current_node = current_node.next
            i-=1
        return current_node
    
    def get(self, index):
        node = self.get_node(index)
        if node == -1:
            return -1
        else:
            return node.val
    
    def append(self, val):
        if self.head is None:
            self.head = Node(val)
            self.length+=1
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(val)
        self.length+=1
    
    def prepend(self, val):
        self.head = Node(val, self.head)
        self.length+=1
    
    def insert(self, index, val):
        if index<0 or index>self.length:
            return "Error"
        if index==0:
            self.prepend(val)
            return
        previous_node = self.get_node(index-1)
        previous_node.next = Node(val, self.get_node(index))
        self.length+=1

    def delete(self,index):
        if index<0 or index>=self.length:
            return "Error"
        if index == 0:
            self.head = self.head.next
            self.length-=1
            return
        previous_node = self.get_node(index-1)
        next_node = self.get_node(index+1)
        if next_node!=-1:
            previous_node.next = next_node
        else:
            previous_node.next = None
        self.length-=1        
    
    def find(self, val):
        for i in range(self.length):  
            if self.get(i) == val:
                return i
        return -1
    
    def contains(self, val):
        for i in range(self.length):  
            if self.get(i) == val:
                return True
        return False
    