class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []
        
        for i in range(len(nums) - 2):
            
            if i == 0 or nums[i] != nums[i - 1]:
                
                start = i + 1
                end = len(nums) - 1
                
                while start < end:
                    
                    total = nums[i] + nums[start] + nums[end]
                    
                    if total == 0:
                        
                        ans.append([nums[i], nums[start], nums[end]])
                        
                        
                        while  start + 1 < len(nums)  and (nums[start] == nums[start + 1]) : start += 1
                        while  end > 0 and nums[end] == nums[end - 1]: end -= 1
                        
                        start += 1
                        end -= 1
                        
                    elif total > 0: end -= 1
                        
                    else: start += 1
                        
                        
        return ans
                        
                
                