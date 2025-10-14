class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        if 2 * k > len(nums):
            return False

        flag = True

        for l in range(len(nums) - 2 * k + 1):
            flag = True

            for a in range(l + 1, l + k):
                if nums[a - 1] >= nums[a]:
                    flag = False
                    break


            for b in range(l + k + 1, l + (k * 2)):
               if nums[b - 1] >= nums[b]:
                    flag = False
                    break

            if flag:
                return True 


        
        return flag
        
        