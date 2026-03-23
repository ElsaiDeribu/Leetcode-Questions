class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        ans = []
        subset = []

        def dfs(idx):

            ans.append(subset.copy())

            for i in range(idx, len(nums)):

                if i > idx and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
    

    
        dfs(0)

        return ans



        