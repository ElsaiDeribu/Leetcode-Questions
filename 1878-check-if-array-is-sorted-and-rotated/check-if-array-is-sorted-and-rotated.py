class Solution:
    def check(self, nums: List[int]) -> bool:

        lower_bar = nums[0]
        upper_bar = float("inf")
        updates = 1

        for i in range(1, len(nums)):


            if nums[i] < nums[i - 1]:
                if nums[i] > lower_bar:
                    return False

                if updates:
                    lower_bar = nums[i]
                    upper_bar = nums[0]
                    updates = 0
                else:
                    return False

            if not (lower_bar <= nums[i] <= upper_bar):
                return False

    
            

        return True

        