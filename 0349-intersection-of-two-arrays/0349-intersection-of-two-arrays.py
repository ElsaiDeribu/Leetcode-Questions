class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        
        cnums1 = Counter(nums1)
        cnums2 = Counter(nums2)
        
        
        for i in cnums1:
            
            if cnums2[i]:
                ans.append(i)
                
        return ans
            
        