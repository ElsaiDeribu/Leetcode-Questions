class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        st = []
        points.sort()

        for i in range(len(points)):

            if st and st[-1][1] >= points[i][0]:
                    last = st.pop()

                    left = points[i][0]
                    right = min(last[1], points[i][1])

                    st.append([left, right])
            else:
                st.append(points[i]) 



        return len(st)