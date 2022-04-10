class Solution(object):
    def targetIndices(self, nums, target):
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                 if nums[i] > nums[j]:
                         nums[i], nums[j] = nums[j], nums[i]
                
        occurence =[]
        for ii in  range(len(nums)): 
            if nums[ii] == target:
                occurence.append(ii)
        return occurence