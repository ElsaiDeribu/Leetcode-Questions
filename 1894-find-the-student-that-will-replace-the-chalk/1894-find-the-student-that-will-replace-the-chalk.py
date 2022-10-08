class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total = sum(chalk)
        
        remainingChalk = k % total
        
        for i in range(len(chalk)):
            remainingChalk -= chalk[i]
            if remainingChalk < 0:
                return i
        