class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ans = []
        
        intervals.sort()
        
        ans.append(intervals[0])
        for i in range(1, len(intervals)):
            
            if intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
                
            elif intervals[i][0] <= ans[-1][1] and intervals[i][1] > ans[-1][1]:
                ans[-1][1] = intervals[i][1]
            
           
        return ans