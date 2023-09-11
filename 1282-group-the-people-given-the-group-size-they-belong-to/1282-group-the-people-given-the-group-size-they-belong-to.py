class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        
        for idx, val in enumerate(groupSizes):
            groupSizes[idx] = (val, idx) 
            
        groupSizes.sort()
        
        j = i = 0
        
        while j < len(groupSizes):
            
            temp = []
            curr = groupSizes[j][0]
            
            while len(temp) < curr:
                temp.append(groupSizes[i][1])
                i += 1
                
            ans.append(temp)
            
            j = i
            
        return ans
        
        