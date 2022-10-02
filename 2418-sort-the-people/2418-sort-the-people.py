class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        ans = []
        
        for i in range(len(names)):
            ans.append((heights[i], names[i]))
            
        ans = sorted(ans, reverse = True)
        
        for i in range(len(ans)):
            ans[i] = ans[i][1]
            
            
        return ans
        
        
        