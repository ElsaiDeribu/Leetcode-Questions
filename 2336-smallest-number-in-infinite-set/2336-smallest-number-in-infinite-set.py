class SmallestInfiniteSet:

    def __init__(self):
        self.infSet = []
        self.visited = set()
        for i in range(1, 10001):
            self.infSet.append(i)
            self.visited.add(i)
            
        heapify(self.infSet)
        

    def popSmallest(self) -> int:
        
        if not self.infSet:
            return 
        
        num = heappop(self.infSet)
        self.visited.remove(num) 
        
        return num

    def addBack(self, num: int) -> None:
        
        if num not in self.visited: 
            self.visited.add(num)
            heappush(self.infSet, num)


            
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)