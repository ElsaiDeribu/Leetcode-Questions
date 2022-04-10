class Solution(object):
    def kthLargestNumber(self, nums, k):
        
            nums = list(map(int, nums))
            nums.sort()
            nums_rev = nums[::-1]

            return str(nums_rev[k-1])

     
        