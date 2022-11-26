class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        st = []
        ans = []
            
        for i in reversed(range(len(heights))):
            count = 0
            
            while st and st[-1][0] < heights[i]:
                count += 1
                st.pop()
            
            if st:
                ans.append(count + 1)
                
            else:
                ans.append(count)
            st.append((heights[i], i))
            
            
        return ans[::-1]
        
