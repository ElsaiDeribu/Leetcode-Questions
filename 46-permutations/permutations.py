class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # TC O(n! · n)
        # SC O(n! · n)
        
        ans = []
        path = []
        visited = set()

        def dfs():
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    path.append(nums[i])

                    dfs()

                    path.pop()
                    visited.remove(nums[i])

        dfs()

        return ans