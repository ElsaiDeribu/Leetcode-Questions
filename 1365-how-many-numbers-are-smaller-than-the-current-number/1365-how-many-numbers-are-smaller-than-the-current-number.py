class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
            
        
        nums2 = nums[:]
        dic = {}

        nums2.sort()
        
        for i in range(len(nums2)):
            
            if nums2[i] not in dic:
                
                dic[nums2[i]] = i
         
        for i in range(len(nums)):
            nums[i] = dic[nums[i]]
        
        return nums