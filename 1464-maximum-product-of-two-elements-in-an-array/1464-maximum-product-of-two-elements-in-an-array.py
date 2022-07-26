class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        nums.sort()
        
        return  (nums[len(nums)-1]-1)*(nums[len(nums) - 2]-1)
        
#         ans = []
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 heappush(ans, -(nums[i]-1)*(nums[j]-1))
                
                
#         return -heappop(ans)
        
        