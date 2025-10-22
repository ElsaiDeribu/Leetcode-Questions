class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}


        for idx, val in enumerate(nums):
            if target - val in dic:
                return [idx, dic[target - val]]

            dic[val] = idx

        