class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
            else:
                k += 1
          
        for i in range(len(nums)):
            for j in range( i + 1, len(nums)):
                if nums[i] == "_" and nums[j] != "_":
                    nums[i], nums[j] = nums[j], nums[i]
                    
        return k    
                    
