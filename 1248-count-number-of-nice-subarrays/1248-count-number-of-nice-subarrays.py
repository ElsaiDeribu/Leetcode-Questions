class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        prefix = defaultdict(int)
        prefix[0] = 1
        sum = 0
        count = 0
        
        for i in range(len(nums)):
            if nums[i] % 2:
                nums[i] = 1
            else:
                nums[i] = 0
                
                
        for i in range(len(nums)):  
            sum += nums[i]
           
            if sum - k in prefix: 
                count += prefix[sum - k]
                
            prefix[sum] += 1
        
        
        return count
            
                
        
        
        
        