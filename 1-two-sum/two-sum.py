class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = defaultdict(int)


        for idx in range(len(nums)):

            wanted = target - nums[idx]

            if wanted in seen:
                return [seen[wanted], idx]

            seen[nums[idx]] = idx

        