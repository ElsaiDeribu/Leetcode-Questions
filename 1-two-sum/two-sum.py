class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        dct = defaultdict()

        for i in range(len(nums)):
            res = target - nums[i]

            if res in dct:
                return [dct[res], i]

            dct[nums[i]] = i
