class Hash_Map:
    def __init__(self, size):
        self.size = size
        self.array = [[] for _ in range(size)]
        self.length = 0
    
    def hash(self,key):
        return sum(ord(c) for c in str(key)) % self.size
    
    def set(self, key, val):
        slot = self.hash(key)
        if self.contains(key):
            for i, element in enumerate(self.array[slot]):
                if element[0] == key:
                    self.array[slot][i] = (key,val)
                    return
        self.array[slot].append((key,val))
        self.length+=1
        
    def get(self, key):
        if self.contains(key):
            slot = self.hash(key)
            for i, element in enumerate(self.array[slot]):
                if element[0] == key:
                    return element[1]
        raise KeyError("Key does not exist")
    
    def delete(self, key):
        if self.contains(key):
            slot = self.hash(key)
            for i, element in enumerate(self.array[slot]):
                if element[0] ==key:
                    del self.array[slot][i]
                    self.length-=1
                    return
        raise KeyError("Key does not exist")
    
    def contains(self, key):
        slot = self.hash(key)
        for element in self.array[slot]:
            if element[0] == key:
                return True
        return False
    
    def keys(self):
        keys = []
        for slot in self.array:
            for key, val in slot:
                keys.append(key)
        return keys
    
    def values(self):
        vals = []
        for slot in self.array:
            for key, val in slot:
                vals.append(val)
        return vals
    
    def __repr__(self):
        pairs = []
        for slot in self.array:
            for key, val in slot:
                pairs.append(f"{key}: {val}")
        return "{" + ", ".join(pairs) + "}"
    

    
            
