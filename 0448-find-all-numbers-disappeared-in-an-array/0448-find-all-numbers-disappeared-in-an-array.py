class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        
        ans = []
        
        for i in range(len(nums)):
            
            while nums[i] - 1 != i:
                if nums[nums[i] - 1] == nums[i]:
                    break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                
                
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                ans.append(i + 1)
                
                
        return ans
            