class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        @cache
        def dp(i, j):
            
            if i >= len(nums1) or j >= len(nums2):
                return float("-inf")
            
            res = float("-inf")
            res = max(res, dp(i + 1, j + 1) + (nums1[i] * nums2[j]), dp(i + 1, j), dp(i, j + 1), (nums1[i] * nums2[j]))
                    
            return res 
  
         
        return dp(0, 0)
        
        