class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        nums.sort()
        
        l = 0
        r = len(nums) - 1
        
        
        while l <= r:
            
            if l == r:
                ans.append(nums[r])
                break
                    
            ans.append(nums[l])
            l += 1
            
            ans.append(nums[r])
            r -= 1
            
            
            
        return ans