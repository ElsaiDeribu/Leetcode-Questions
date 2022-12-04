class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        prefSum = nums[0]
        postSum = sum(nums) - nums[0]
        
        prefAv = prefSum
        postAv = 0 if len(nums) == 1 else postSum // (len(nums) - 1)
        minIndex = 0
        minDiff = abs( prefAv - postAv)
         
        for i in range(1, len(nums)):
            prefSum += nums[i]
            postSum -= nums[i]
            
            prefAv = prefSum // (i + 1)
            postAv =  0 if i == len(nums) - 1 else postSum // (len(nums) - i - 1)
            
            if abs(prefAv - postAv) < minDiff:
                minDiff =abs(prefAv - postAv)
                minIndex = i
            
        return minIndex
        
