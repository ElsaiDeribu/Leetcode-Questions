class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[1])
        last_interval = [None, None]
        res = 0

        for start, end in intervals:
            if last_interval[0] != None and (last_interval[0] > start or last_interval[1] > start):
                res += 1

            else:
                last_interval[0], last_interval[1] = start, end


        return res


        