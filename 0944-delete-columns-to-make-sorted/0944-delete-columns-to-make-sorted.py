class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        colsToDelete = 0
        
        for col in range(len(strs[0])):
            currLetter = strs[0][col] 
            for row in range(1,len(strs)):
                if strs[row][col] < currLetter:
                    colsToDelete += 1
                    break
                currLetter = strs[row][col]
                
                
        return colsToDelete