class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        
        maximum = [0] * len(nums)
        deq = deque([])
        ans = float("-inf")
        
        for i in range(len(nums)):
            while deq and deq[0][1] < i - k :
                deq.popleft()
                
            prevMax = max(deq[0][0] if deq else 0, 0)
            
            maximum[i] = nums[i] + prevMax 

            while deq and deq[-1][0] < maximum[i] :
                deq.pop()
                
            deq.append((maximum[i], i))
             
            ans = max(ans, maximum[i])
        
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