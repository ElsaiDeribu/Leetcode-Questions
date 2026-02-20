class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:


        i = 0
        ans = []


        while i < len(nums):

            l = i

            while i + 1 < len(nums) and nums[i + 1] - nums[i] == 1:
                i += 1

            if i == l:
                ans.append(str(nums[l]))

            else:
                a = str(nums[l])
                b = "->"
                c = str(nums[i])
                ans.append(a + b + c)

            i += 1

        return ans

            

