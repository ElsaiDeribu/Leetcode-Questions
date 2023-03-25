class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        left = m - 1
        right = n - 1
        mid  = len(nums1) - 1
        
        while left >= 0 or right >= 0:
            
            if right < 0 or (left >= 0 and nums1[left] >= nums2[right]): 
                nums1[mid] = nums1[left]
                left -= 1
                mid -= 1
                
            else:
                
                nums1[mid] = nums2[right]
                right -= 1
                mid -= 1
                
                
                
        
            
            
        
        
        
        