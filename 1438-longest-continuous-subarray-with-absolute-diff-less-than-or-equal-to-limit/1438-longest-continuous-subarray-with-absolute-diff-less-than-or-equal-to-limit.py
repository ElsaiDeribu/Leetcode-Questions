class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = 0
        j = 0
        longest = 0
        maximum = nums[i] 
        minimum = nums[j]
        stackincreasing = []
        stackdecreasing= []
        if len(nums) == 1:
            return 1
     
        while j < len(nums):
            while j < len(nums) + 1 and  maximum - minimum  <= limit:
                longest = max(longest, j - i)
                if j < len(nums):
                    
                    while stackincreasing and stackincreasing[-1] > nums[j]:
                        stackincreasing.pop()
                        
                    stackincreasing.append(nums[j])
                    
                    while stackdecreasing and stackdecreasing[-1] < nums[j]:
                        stackdecreasing.pop()
                        
                    stackdecreasing.append(nums[j])
                    
                maximum = stackdecreasing[0]
                minimum = stackincreasing[0]
                    
                    # if nums[j] > maximum:
                    #     maximum = nums[j]
                    # elif nums[j] < minimum:
                    #     minimum = nums[j]
                
                # maximum = max(nums[i:j+1]) 
                # minimum = min(nums[i:j+1])
                j += 1
            
            while i < j and maximum - minimum  > limit :
                removed = nums[i]
                i += 1
                
                if stackincreasing and removed == stackincreasing[0]:
                    stackincreasing.pop(0)
                    minimum = stackincreasing[0] 
                if stackdecreasing and removed == stackdecreasing[0]:
                    stackdecreasing.pop(0)
                    maximum = stackdecreasing[0]

        return longest
                
        