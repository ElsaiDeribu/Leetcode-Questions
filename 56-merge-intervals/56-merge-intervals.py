class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ans = []
        intervals.sort()
        ans.append(intervals[0])
        
        for i in range(1, len(intervals)):
            
            if ans[-1][-1] >= intervals[i][0]:
                if ans[-1][-1] >= intervals[i][1]:
                    continue
                else:
                    ans[-1][-1] = intervals[i][1]
                
            else:
                ans.append(intervals[i])
                
        return ans
        