class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[1])
        print(intervals)
        ans = []
        res = 0

        for i in intervals:
            if not ans:
                ans.append(i)
                continue

            a, _ = i

            if ans[-1][0] > a or ans[-1][1] > a:

                res += 1

            else:
                ans.append(i)

        return res


        