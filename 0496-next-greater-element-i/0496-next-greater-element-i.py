class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nextGreatest = defaultdict(int)
        
        st = []
        
        for i in range(len(nums2)):
            
            while st and st[-1] < nums2[i]:
                
                nextGreatest[st[-1]] = nums2[i]
                st.pop()
            
            st.append(nums2[i])
            
            
        for i in range(len(nums1)):
            if nums1[i] in nextGreatest.keys():
                nums1[i] = nextGreatest[nums1[i]]
                
            else:
                nums1[i] = -1
                
                
        return nums1