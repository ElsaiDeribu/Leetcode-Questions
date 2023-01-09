class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        
        for i in range(len(nums)): 
            nums[i] = (nums[i], i)
            
        nums.sort()
        
        left = []
        right = []
        
        
        i = 0
        pivotCount = 0
        leftFinished = False
        
        
        while i < len(nums):
            
            while i < len(nums) and nums[i][0] == pivot:
                pivotCount += 1
                leftFinished = True
                i += 1
            
            if i < len(nums) and leftFinished:
                right.append(nums[i])
            elif i < len(nums):
                left.append(nums[i])
                
            
            i += 1
            
            
        left = list( map( lambda x: x[0], sorted(left, key = lambda x: x[1])))
        right = list(map(lambda x: x[0], sorted(right, key = lambda x: x[1])))
        mid = [pivot] * pivotCount
        
        
        return left + mid + right
        
        
        