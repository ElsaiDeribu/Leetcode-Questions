class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        count = 0

        for c in range(len(strs[0])):
            for r in range(len(strs)):
                prev = r - 1 if r > 0 else 0
                if strs[prev][c] > strs[r][c]:
                    count +=1
                    break
                
            
        return count



        