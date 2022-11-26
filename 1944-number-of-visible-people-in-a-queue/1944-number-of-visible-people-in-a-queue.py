class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        st = []
        ans = [0] * len(heights)
            
        for i in range(len(heights) - 1, -1, -1):
            count = 0
            
            while st and st[-1] < heights[i]:
                count += 1
                st.pop()
            
            if st:
                ans[i] = count + 1
            else:
                ans[i] = count
                
            st.append(heights[i])
            
            
        return ans
        
