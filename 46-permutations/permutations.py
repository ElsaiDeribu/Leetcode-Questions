class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def dfs(visited, lst):
            if len(lst) == len(nums) :
                return ans.append(lst[:])
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    dfs(visited | set([nums[i]]), lst + [nums[i]])

        dfs(set(), [])

        return ans