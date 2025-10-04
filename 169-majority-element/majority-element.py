class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        count = 0
        num = None

        for n in nums:

            if count == 0:
                num = n
            
            count += 1 if n == num else -1

        return num