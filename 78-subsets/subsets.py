class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        st = []

        def dfs(idx):
            if idx == len(nums):
                ans.append(st[:])
                return

            # take
            st.append(nums[idx])
            dfs(idx + 1)
            st.pop()

            # not take
            dfs(idx + 1)


        dfs(0)

        return ans