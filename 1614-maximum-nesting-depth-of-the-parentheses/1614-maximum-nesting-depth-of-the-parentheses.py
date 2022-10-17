class Solution:
    def maxDepth(self, s: str) -> int:
        
        maxDepth = 0
        count = 0
        
        for i in s:
            if i == '(':
                count += 1
                maxDepth = max(count, maxDepth)
            elif i == ')':
                count -= 1
                
        return maxDepth
