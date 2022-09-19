class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(nums) - 1
        
        for i in range(len(nums)):
            nums[i] = (nums[i], i)
            
        nums.sort()
        
        while start < end:
            
            if nums[start][0] + nums[end][0] > target: end -= 1
                
            elif nums[start][0] + nums[end][0] < target: start += 1
                
            else:
                
                return [nums[start][1], nums[end][1]]
        