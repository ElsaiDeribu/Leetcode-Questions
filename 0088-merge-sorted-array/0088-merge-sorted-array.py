class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        l = m - 1
        r = n - 1
        k = len(nums1) - 1
        
        while r >= 0 or l >= 0:
          
            if r >= 0 and (l < 0 or nums1[l] < nums2[r]):
                nums1[k] = nums2[r]
                r -= 1
                k -= 1
            else:
                nums1[k] = nums1[l]
                l -= 1
                k -= 1
         
        
        
        
        
        
        
        
        
        
#         j = 0
#         for i in range(m, len(nums1)):
#             nums1[i] = nums2[j]
#             j += 1
            
#         nums1.sort()
        
        
        
#         ans = []
#         i = 0
#         j = 0
#         while i < m or j < n:
#             if i < m and nums1[i] < nums2[j]:
#                 ans.append(nums1[i])
#                 i += 1
#             else:
#                 ans.append(nums2[j])
#                 j += 1
                
#         print(ans)
        
        