class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        for i in range(len(nums)):
            nums[i] = int(nums[i])
            
        nums = sorted(nums, reverse = True)   
        
        
        return str(nums[k - 1])