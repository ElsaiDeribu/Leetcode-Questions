class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        count = 0

        for c in range(len(strs[0])):
            for r in range(1, len(strs)):
                if strs[r - 1][c] > strs[r][c]:
                    count +=1
                    break
                
            
        return count



        