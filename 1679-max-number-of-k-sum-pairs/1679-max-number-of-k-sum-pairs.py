class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = len(nums) - 1
        count = 0
        nums.sort()
        
        while left < right:
            
            if (nums[left] + nums[right] < k):
                
                left += 1 
                
            if (nums[left] + nums[right] > k):
                
                right -= 1 
            
            if (nums[left] + nums[right]) == k and left < right:
                
                right -= 1
                left += 1
                count += 1
                
        return count
        