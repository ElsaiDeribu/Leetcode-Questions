class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        l , r = m  - 1, n - 1
        update = len(nums1) - 1

        while l >= 0 or r >= 0:

            if (l < 0 ) or (r >= 0 and nums1[l] < nums2[r]):
                nums1[update] = nums2[r]
                update -= 1
                r -= 1
 
            else:
                nums1[update] = nums1[l]
                update -= 1
                l -= 1

        



