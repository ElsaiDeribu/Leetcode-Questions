class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[1])
        prev_end = float("-inf")
        res = 0

        for start, end in intervals:
            if prev_end > start:
                res += 1
            else:
                prev_end = end

        return res


        