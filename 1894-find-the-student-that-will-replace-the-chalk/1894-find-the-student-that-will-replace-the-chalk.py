class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total = sum(chalk)
        
        lastRoundKLeft = k % total
        
        for i in range(len(chalk)):
            lastRoundKLeft -= chalk[i]
            if lastRoundKLeft < 0:
                return i
        