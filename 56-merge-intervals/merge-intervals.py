class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        st = []
        intervals.sort()

        for i in range(len(intervals)):

            if not st:
                st.append(intervals[i])

            else:

                while st and st[-1][1] >= intervals[i][0]:
                    last = st.pop()

                    intervals[i][0] = min(last[0], intervals[i][0])
                    intervals[i][1] = max(last[1], intervals[i][1])

                st.append(intervals[i])
        

        return st