class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        curr_list = []
        visited = set()

        def dfs():

            if len(curr_list) == len(nums):
                ans.append(curr_list.copy())


            for i in range(len(nums)):
                if nums[i] not in curr_list:
                    visited.add(nums[i])
                    curr_list.append(nums[i])
                    dfs()
                    curr_list.pop()
                    visited.remove(nums[i])


        dfs()

        return ans