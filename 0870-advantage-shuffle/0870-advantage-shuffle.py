class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(nums2)):
            nums2[i] = (nums2[i], i)
        
        nums1.sort()
        nums2.sort()
        
        p1 = p2 = 0
        ans = {}
        temp = []
        
        while p1 < len(nums1) and p2 < len(nums2):
            
            if nums1[p1] > nums2[p2][0]:
                ans[nums2[p2][1]] = nums1[p1]
                p1 += 1
                p2 += 1
                
            else: 
                temp.append(nums1[p1])
                p1 += 1
              
        temp.extend(nums1[p1:])
        
        for i in range(len(nums2)):
            if i in ans:
                nums2[i] = ans[i]
            else:
                nums2[i] = temp.pop()
        
        
        return nums2
        
        
            
            