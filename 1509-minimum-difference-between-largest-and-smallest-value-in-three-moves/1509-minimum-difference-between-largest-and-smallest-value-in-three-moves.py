class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        if len(nums) > 3:
            poss1 = nums[-1] - nums[3]
            poss2 = nums[-2] - nums[2]
            poss3 = nums[-3] - nums[1]
            poss4 = nums[-4] - nums[0]
            return min(poss1, poss2, poss3, poss4)
        
        return 0