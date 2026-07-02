class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # (min bar in section) * (width fo section/number of bars)

        st = []
        ans = 0

        for idx, height in enumerate(heights):

            left = idx
            while st and st[-1][1] > height:

                l, h = st.pop()

                ans = max(ans, (idx - l) * h)

                left = l

                
            st.append((left, height))


        for left, height in st:

            ans = max(ans, (len(heights) - left) * height)

        
        return ans