class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 1
        r = l
        visited = defaultdict(int)
        
        visited[nums[0]] = 1
        
        while l < len(nums):
            r = l
            
            if visited[nums[l]] >= 2:
                
                while r < len(nums) and visited[nums[r]] >= 2:
                    r += 1
                    
                if r >= len(nums):
                    return l
                else:
                    nums[l], nums[r] = nums[r], nums[l]
                    
            visited[nums[l]] += 1
            
            l += 1
            
        