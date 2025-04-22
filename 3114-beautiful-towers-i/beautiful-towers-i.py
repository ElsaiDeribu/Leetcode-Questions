class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:

        def helper(arr):
            cst = 0
            st = []

            for num in arr:
                if st and st[-1] < num:
                    cst += (num - st[-1])
                    st.append(st[-1])
                    continue

                st.append(num)

            return cst

        min_cst = float("inf")

        for i in range(len(heights)):
            cst_l = helper(heights[i::-1])
            cst_r = helper(heights[i + 1:])

            min_cst = min(min_cst, cst_l + cst_r)

        return sum(heights) - min_cst


        

        