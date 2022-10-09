class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        
        remainders = defaultdict(int)
        count = 0
        subArrSum = nums[0]
        
        remainders[subArrSum % k] += 1
        
        
        for i in range(1, len(nums)):
            subArrSum += nums[i]
            remainders[subArrSum % k] += 1
            
        for j in remainders.keys():
            if j == 0:
                count += ((remainders[j] * (remainders[j] - 1)) / 2) + remainders[j]
            else:   
                count += ((remainders[j] * (remainders[j] - 1)) / 2)
                
        for i in nums:
            if i % k == 0:
                count -= 1
                
        return True if count else False
        