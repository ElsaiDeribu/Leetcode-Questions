class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:


        r = 0
        ans = []


        while r < len(nums):

            l = r

            while r + 1 < len(nums) and nums[r + 1] - nums[r] == 1:
                r += 1

            if r == l:
                ans.append(str(nums[l]))

            else:
                a = str(nums[l])
                b = "->"
                c = str(nums[r])
                ans.append(a + b + c)

            r += 1

        return ans

            

