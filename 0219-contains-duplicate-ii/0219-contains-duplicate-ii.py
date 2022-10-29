class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        
        windowItems = defaultdict(int)
        
        l = 0
        r = 0
        
        while r < len(nums):
            
            while abs(r - l) > k:
                windowItems[nums[l]] -= 1
                l += 1
            
            windowItems[nums[r]] += 1
            
            if windowItems[nums[r]] == 2:
                return True

            r += 1
            
        return False

               
