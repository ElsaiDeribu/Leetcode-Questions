class RandomizedSet:

    def __init__(self):
        self.table = {}
        self.arr = []
    
    def insert(self, val):
        if val not in self.table:
            self.table[val]= len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val):
        
        if val in self.table:
            last_index, val_index = self.table[self.arr[-1]], self.table[val]

            self.arr[val_index], self.arr[last_index] = self.arr[last_index], self.arr[val_index]
            self.table[self.arr[val_index]] = val_index

            del self.table[val]

            self.arr.pop()
            return True
        return False

    
    def getRandom(self):
        return random.choice(self.arr)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()