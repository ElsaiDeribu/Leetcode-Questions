class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        
        deq = deque([])
        ans = float("-inf")
        
        for i in range(len(nums)):
            while deq and deq[0][1] < i - k :
                deq.popleft()
                
            prevMax = max(deq[0][0] if deq else 0, 0)
            
            maximum = nums[i] + prevMax 

            while deq and deq[-1][0] < maximum :
                deq.pop()
                
            deq.append((maximum, i))
             
            ans = max(ans, maximum)
        
        return ans
        
        
        
        
        
        
        
#         # @cache
#         def dp(prev, curr):
#             if curr >= len(nums):
#                 return 0
            
#             if prev == None or curr - prev <= k:
                
#                 take = dp(curr, curr + 1) + nums[curr]
#                 notTake = dp(prev, curr + 1)
#                 # print(prev, curr)
#                 # print(take, notTake) 
#                 return max(take, notTake)
            
#             else:
                
#                 return dp(prev, curr + 1)
        
#         allNeg = True
        
#         for num in nums:
#             if num > 0:
#                 allNeg = False
                
#         if allNeg:
#             return max(nums)
        
#         return dp(None,0)