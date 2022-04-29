class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0 
        j = 1 
        while j < len(nums):
            if nums[i] ==0 and nums[j] != 0:
                nums[j],nums[i] = nums[i], nums[j]
                j += 1
                i += 1
            if j < len(nums):
                if nums[j] == 0 and nums[i] == 0:
                    j+=1

            if nums[i] != 0 and nums[j] == 0:
                i+=1
                
            if nums[i] !=0 and nums[j] != 0:
                j += 1
                i += 1

        return nums
        
      
        