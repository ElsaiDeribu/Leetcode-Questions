class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
#         heap = []
#         for i in nums:
#             heappush(heap, -i)
#         ans = 0
        
#         while k:
#             ans = heappop(heap)
#             k -= 1
            
#         return -ans


        #sorting solution
    
        nums = sorted(nums, reverse = True)
        print(nums)    
        return nums[k - 1]
