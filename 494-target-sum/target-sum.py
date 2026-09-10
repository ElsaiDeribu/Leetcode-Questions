class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        


        @cache
        def dfs(idx, trgt):

            if trgt == 0 and idx == len(nums): return 1

            if idx == len(nums): return 0


            return dfs(idx + 1, trgt - nums[idx]) + dfs(idx + 1, trgt + nums[idx])

            
            
        return dfs(0, target)