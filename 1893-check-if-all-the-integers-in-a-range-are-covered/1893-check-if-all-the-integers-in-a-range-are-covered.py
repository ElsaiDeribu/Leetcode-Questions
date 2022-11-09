class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        rangeNums = set()
        
        for i in range(len(ranges)):
            for j in range(ranges[i][0], ranges[i][1] + 1):
                rangeNums.add(j)
                
        for i in range(left, right + 1):
            if not i in rangeNums:
                return False
            
        return True