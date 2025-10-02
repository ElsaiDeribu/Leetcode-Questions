class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        streak = 0
        
        for r in range(len(nums)):

            if nums[l] != nums[r]:
                if streak >= 2 :
                    l += 1
                    nums[l] = nums[l - 1]

                l += 1
                nums[l] = nums[r]

                streak = 1
    
            else:
                streak += 1


        if streak >= 2:
            l += 1
            nums[l] = nums[l - 1]

        return l + 1
        