class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n):
            nums.append(int(str(nums[i])[::-1]))

        return len(set(nums))