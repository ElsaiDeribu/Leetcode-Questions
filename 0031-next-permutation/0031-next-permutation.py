class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 1
        
        while i > -1:
            
            if i - 1 > -1 and nums[i - 1] < nums[i]:
                
                break
                
            i -= 1
            
        if i == -1:
            nums.sort()
            return 
        
        
        indexToReplace = i - 1
        minReplacementIndex= i
        
        for j in range(i, len(nums)):
            
            if nums[j] > nums[indexToReplace] and nums[j] < nums[minReplacementIndex]:
                minReplacementIndex= j
                
                
        nums[indexToReplace], nums[minReplacementIndex] = nums[minReplacementIndex], nums[indexToReplace]
            
                
        for k in range(i, len(nums)): 
            for t in range(k + 1, len(nums)):
                
                if nums[k] > nums[t]:
                    nums[k], nums[t] = nums[t], nums[k]
                
                
                
                
            
            
            
        
                    
        