class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        st = []

        def dfs(idx):
    
            ans.append(st[::])

            for i in range(idx, len(nums)):
                st.append(nums[i])
                dfs(i + 1)
                st.pop()

        dfs(0)

        return ans