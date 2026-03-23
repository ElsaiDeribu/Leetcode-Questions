class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        subset = []


        def dfs(idx):
            if idx == len(nums):
                ans.add(tuple(sorted(subset.copy())))
                return

            # take
            subset.append(nums[idx])
            dfs(idx + 1)
            subset.pop()

            # not take
            dfs(idx + 1)            

        dfs(0)


        return [list(entry) for entry in ans]


        
        