class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # TC: O(n · 2ⁿ)
        # SC: O(n · 2ⁿ)
        
        ans = []
        perm = []
        nums.sort()

        def dfs(idx):

            if idx == len(nums):
                ans.append(perm[:])
                return

            # take
            perm.append(nums[idx])
            dfs(idx + 1)
            perm.pop()

            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1

            # not take
            dfs(idx + 1)


        dfs(0)


        return ans
