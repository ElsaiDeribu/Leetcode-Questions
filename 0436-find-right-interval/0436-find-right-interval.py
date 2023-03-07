class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        
        ans = [0] * len(intervals)
        
        sortd = [(index, val[0]) for index, val in enumerate(intervals)]
        sortd = sorted(sortd, key = lambda x : x[1] )
        
        def findRight(num):
            
            left = -1
            right = len(sortd) - 1
            
            
            while left + 1 < right:
                mid = left + (right - left)//2
                
                if sortd[mid][1] >= num:
                    right = mid
                
                else:
                    left = mid
            
            return sortd[right]
            
        for i in range(len(intervals)):
            
            result = findRight(intervals[i][1])
            
            ans[i] = result[0] if result[1] >= intervals[i][1] else -1
            
        return ans