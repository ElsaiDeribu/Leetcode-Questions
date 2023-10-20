# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = []
        
        def dfs(curr): 
                
            for element in curr: 
                num = element.getInteger()
                lst = element.getList()
                if num != None:
                    self.arr.append(num)
                    
                else:
                    dfs(lst)
            
        dfs(nestedList)   
        
        self.nxt = 0        
    
    def next(self) -> int:
        
        self.nxt += 1
        
        return self.arr[self.nxt - 1 ]
    
    def hasNext(self) -> bool:
        
        if self.nxt >= len(self.arr):
            return False
        
        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())