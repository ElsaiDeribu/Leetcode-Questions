class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
      
        ans = []
        perm = []
        visited = set()

        def dfs():
            if len(perm) == len(nums):
                ans.append(perm[:])
                return

            for num in nums:
                if num not in visited:
                    visited.add(num)
                    perm.append(num)

                    dfs()

                    visited.remove(num)
                    perm.pop()

        dfs()
        return ans