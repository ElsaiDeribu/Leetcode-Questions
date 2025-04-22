class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:

        def helper(left, right, drctn):
            cst = 0
            st = []

            for i in range(left, right, drctn):
                num = heights[i]
                if st and st[-1] < num:
                    cst += (num - st[-1])
                    st.append(st[-1])
                    continue

                st.append(num)

            return cst

        min_cst = float("inf")

        for i in range(len(heights)):
            cst_l = helper(i, -1, -1)
            cst_r = helper(i + 1, len(heights), 1)

            min_cst = min(min_cst, cst_l + cst_r)

        return sum(heights) - min_cst


        

        