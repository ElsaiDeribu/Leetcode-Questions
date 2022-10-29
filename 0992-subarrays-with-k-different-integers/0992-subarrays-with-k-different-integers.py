class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def helper(mx):
            
            subArr = 0
            i = j = 0
            
            windowElements = defaultdict(int)
            
            while j < len(nums):
                
                windowElements[nums[j]] += 1
                
                while len(windowElements) > mx:
                    windowElements[nums[i]] -= 1
                    if windowElements[nums[i]] == 0:
                        windowElements.pop(nums[i])
                    i += 1
                
                subArr += (j - i + 1)
                
                j += 1
            return subArr
        
        return helper(k) - helper(k - 1)
        
        
            