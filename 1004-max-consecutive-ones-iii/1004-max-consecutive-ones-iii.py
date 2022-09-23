class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        right = 0
        left = 0
        largest = 0
        
        while right < len(nums):
            
            if nums[right] == 0 :
                k -= 1

            while k < 0 :      
                if nums[left] == 0:
                    k += 1
                left += 1
             
            largest = max(largest, right - left + 1)                   
            right += 1
                    
        return largest