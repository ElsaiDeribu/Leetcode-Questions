class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        
        seen = defaultdict(int)

        for idx, num in enumerate(nums):

            wanted = target - num

            if wanted in seen:
                return [seen[wanted], idx]

            seen[num] = idx
        
        