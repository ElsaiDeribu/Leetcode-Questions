class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        
        
        for i in n1.keys():
            
            if i in n2:
                quantity = min(n2[i], n1[i])
                
                for j in range(quantity):
                    ans.append(i)
                    
        return ans