class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):

            if i == 0 or not nums[i] == nums[i - 1]:
                
                l, r = i + 1, len(nums) - 1
                wntd = -nums[i]

                while l < r:
                    res = nums[l] + nums[r]

                    if res > wntd: r -= 1
                    elif res < wntd: l += 1
                    else:
                        ans.append([nums[i], nums[l], nums[r]])
                        while r > 0 and nums[r] == nums[r - 1]: r -= 1
                        while l < len(nums) - 1 and nums[l] == nums[l + 1]: l += 1

                        l += 1
                        r -= 1


                    
        return ans



                