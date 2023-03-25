class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        ans = []
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[nums[i] - 1] == nums[i]:
                    break
                
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                ans.append(nums [i])
                ans.append(i + 1)
              
        print(nums) 
        
        return ans