class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        lis = [1] * len(nums)
        count = [1] * len(nums)
        
        for i in range(1, len(nums)):
            
            longest = 0
            
            for j in range(i):
                
                if nums[j] < nums[i]:
                    if lis[j] > longest:
                        longest = lis[j]
                        count[i] = count[j]
                        
                    elif lis[j] == longest:
                        count[i] += count[j]
                        
            lis[i] = longest + 1
 
        lngstIdx = 0    
        for i in range(len(lis)):
            if lis[i] > lis[lngstIdx]:
                lngstIdx = i
        
        ans = 0
        for i in range(len(count)):
            if lis[i] == lis[lngstIdx]:
                ans += count[i]
                
        return ans
            
            
                
                
                
                
        
        
        
        