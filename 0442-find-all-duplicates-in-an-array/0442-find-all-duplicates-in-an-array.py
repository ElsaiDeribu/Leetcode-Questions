class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        ans = set()
        
        
        for i in range(len(nums)):
            while nums[i] - 1 != i:
                if nums[nums[i] - 1] == nums[i]:
                    ans.add(nums[i])
                    break
                
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        
        return ans