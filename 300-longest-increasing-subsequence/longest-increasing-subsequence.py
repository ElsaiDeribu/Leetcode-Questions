class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        ans = []

        for n in nums:
            if not ans or n > ans[-1]:
                ans.append(n)
            else:
                ans[bisect_left(ans,n)] = n

        return len(ans)



        