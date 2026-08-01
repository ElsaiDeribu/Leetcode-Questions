class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # TC: O(n · 2ⁿ)
        # SC: O(n · 2ⁿ)

        # ans = []
        # st = []

        # def dfs(idx):

        #     if idx == len(nums):
        #         ans.append(st[:])
        #         return

        #     # take
        #     st.append(nums[idx])
        #     dfs(idx + 1)
        #     st.pop()

        #     # not take
        #     dfs(idx + 1)

        # dfs(0)


        # return ans
        
        

        
        # TC: O(n · 2ⁿ)
        # SC: O(n · 2ⁿ)

        ans = []
        path = []
        n = len(nums)

        def dfs(start):
            ans.append(path[:])     # O(n) copy — recorded at every call, not just leaves

            for i in range(start, n):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return ans