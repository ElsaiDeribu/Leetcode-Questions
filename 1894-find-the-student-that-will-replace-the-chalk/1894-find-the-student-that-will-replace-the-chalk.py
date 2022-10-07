class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        usage = list(accumulate(chalk))
        k %= usage[-1]
        
        return bisect.bisect_right(usage,k)
        