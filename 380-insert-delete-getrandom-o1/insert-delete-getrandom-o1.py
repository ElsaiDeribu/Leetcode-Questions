class RandomizedSet:

    def __init__(self):
        self.dic = defaultdict(int)
        self.lst = []
        

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False

        self.lst.append(val)
        self.dic[val] = len(self.lst) - 1
        
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False

        idx = self.dic[val]

        self.dic[self.lst[-1]] = idx
        
        self.lst[idx], self.lst[-1] = self.lst[-1], self.lst[idx]

        self.lst.pop()
        self.dic.pop(val)
        
        return True

    def getRandom(self) -> int:

        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()