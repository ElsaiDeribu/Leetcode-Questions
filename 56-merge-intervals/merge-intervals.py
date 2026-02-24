class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        st = []
        intervals.sort()

        for i in range(len(intervals)):

            if st and st[-1][1] >= intervals[i][0]:

                st[-1][1] = max(st[-1][1], intervals[i][1])

            else:

                st.append(intervals[i])
        

        return st