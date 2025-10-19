class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals.sort()
        ans = []

        for x, y in intervals:

            if ans and x <= ans[-1][1]:
                ans[-1][1] = max(y, ans[-1][1])

            else:
                ans.append([x,y])

        return ans
        