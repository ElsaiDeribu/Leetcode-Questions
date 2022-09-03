class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        ans = []
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            if left == right:
                ans.append(nums[left])
                break
            
            ans.append(nums[left])
            left += 1
            
            ans.append(nums[right])
            right -= 1
            
        return (ans)
        
        
        
        
        

    