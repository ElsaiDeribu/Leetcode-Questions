class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        
        diff = [defaultdict(lambda: 1) for _ in range(len(nums))]

        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                d = nums[i] - nums[j]
                diff[i][d] = diff[j][d] + 1
                ans = max(ans,  diff[i][d])
                
        return ans