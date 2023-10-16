class RandomizedSet:

    def __init__(self):
        self.items = set()

    def insert(self, val: int) -> bool:
        
        if val in self.items:
            return  False
        
        self.items.add(val)
        
        return True
        

    def remove(self, val: int) -> bool:
        
        if val not in self.items:
            return False
            
        self.items.remove(val) 
        
        return True
     
        

    def getRandom(self) -> int:
        
        random = randint(1, len(self.items))
        curr = 1
        
        for item in self.items:
            if random == curr:
                return item
            curr += 1
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()