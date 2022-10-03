class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        count = Counter(nums)
        
        for i in range(len(nums) + 1):
            count[i] -= 1
            
        for i in count.keys():
            if count[i] == -1:
                return i
        
        
        
#         nums.sort()
#         for i in range(len(nums) + 1):
#             if i == len(nums):
#                 return i
            
#             if nums[i] != i:
#                 return i
        