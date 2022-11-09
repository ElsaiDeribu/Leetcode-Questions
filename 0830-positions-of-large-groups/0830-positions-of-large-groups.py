class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        ans = []
        i = j = 0
        
        while j < len(s):
            while s[i] != s[j]:
                i += 1
            j += 1
            if j < len(s) and s[i] != s[j]:
                if j - i >= 3:
                    ans.append([i, j - 1])
            elif j == len(s):
                if j - i >= 3:
                    ans.append([i, j - 1])
                    
        
        return ans