class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.added = []
        self.visited = set()


    def popSmallest(self) -> int:
        
        # print("pop", self.curr, self.visited, self.added)
        
        if self.added:
            if self.curr < self.added[0]:
                num = self.curr
                self.curr += 1
            else:
                num = heappop(self.added)
                self.visited.remove(num)
                
        else:
            num = self.curr
            self.curr += 1
            
        return num

    
    def addBack(self, num: int) -> None:
        
        # print("add", num, self.curr, self.visited)
        if num < self.curr and num not in self.visited:
            
            self.visited.add(num)
            heappush(self.added, num)
                
        # print("added", num, self.curr, self.visited)

        

            
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)