class Solution:
    def check(self, nums: List[int]) -> bool:

        updates = 0
        n = len(nums)

        for i in range(n):

            if nums[i] > nums[(i + 1) % n]:
                updates += 1
                if updates > 1:
                    return False

        return True

                
