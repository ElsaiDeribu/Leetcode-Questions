class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []

        for i in range(len(nums)):

            if i > 0 and nums[i - 1] == nums[i]: continue

            j , k = i + 1, len(nums) - 1

            while j < k:
                total = nums[j] + nums[k] + nums[i]
                if total < 0: j += 1
                elif total > 0: k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]: j += 1
                    while j < k and nums[k - 1] == nums[k]: k -= 1
                    j += 1
                    k -= 1
        
        return ans