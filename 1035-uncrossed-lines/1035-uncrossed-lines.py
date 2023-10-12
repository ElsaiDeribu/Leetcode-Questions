class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        @cache
        def dp(p1, p2):
            
            if p1 >= len(nums1) or p2 >= len(nums2):
                return 0
            
            if nums1[p1] == nums2[p2]:
                return dp(p1 + 1, p2 + 1) + 1
            
            else:
                poss1 = dp(p1 + 1, p2)
                poss2 = dp(p1, p2 + 1)
                
                return max(poss1, poss2) 
        
        
        return dp(0, 0)
        
        