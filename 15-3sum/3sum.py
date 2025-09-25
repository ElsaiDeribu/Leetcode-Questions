class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        nums.sort()

        for i in range(len(nums)):
            j , k = i + 1, len(nums) - 1

            while j < k:
                if nums[j] + nums[k] + nums[i] < 0: j += 1
                elif nums[j] + nums[k] + nums[i] > 0: k -= 1

                elif nums[j] + nums[k] + nums[i] == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

        
        return list(ans)