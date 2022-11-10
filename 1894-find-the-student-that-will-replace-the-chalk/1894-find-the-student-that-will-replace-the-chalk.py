class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        lastRoundChalks = k % sum(chalk)
        
        for i in range(len(chalk)):
            if chalk[i] > lastRoundChalks:
                return i
            
            lastRoundChalks -= chalk[i]
        