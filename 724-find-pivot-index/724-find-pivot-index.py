class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        sumOfNumbersBefore= 0
        print(total)
        
        for i in range(len(nums)):
            if sumOfNumbersBefore == (total - (sumOfNumbersBefore + nums[i])):
                return i
            sumOfNumbersBefore += nums[i]
            
        return -1
            
            
            
          