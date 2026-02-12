class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        n1, n2, update = m - 1, n - 1, len(nums1) - 1

        while n1 >= 0 or n2 >= 0:

            if n2 < 0 or (n1 >= 0 and nums1[n1] > nums2[n2]):
                nums1[update] = nums1[n1]
                n1 -= 1
            else:
                nums1[update] = nums2[n2]
                n2 -= 1
                
            update -= 1