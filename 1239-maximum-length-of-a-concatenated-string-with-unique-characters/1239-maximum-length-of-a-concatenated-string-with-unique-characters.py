class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        perm = []
        maxLen = 0
        currLen = 0
        
        def isPresent(s):
            for item in s:
                for element in perm:
                    if item in element:
                        return True
            return False
        
        
        def hasDuplicateItself(s):
            count = Counter(s)
            for val in count.values():
                if val > 1:
                    return True
                
            return False
        
        
        def dfs(start):
            
            nonlocal maxLen, currLen
            if start >= len(arr):
                return
            
            
            for i in range(start, len(arr)):
                
                if not isPresent(arr[i]) and not hasDuplicateItself(arr[i]):
                    perm.append(arr[i])
                    currLen += len(arr[i])
                    
                    dfs(i + 1)
                    
                    maxLen = max(maxLen, currLen)
                    currLen -= len(arr[i])                    
                    perm.pop()
                
        
        dfs(0)
        
        return maxLen
                
        