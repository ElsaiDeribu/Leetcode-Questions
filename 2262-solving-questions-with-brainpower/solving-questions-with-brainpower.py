class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @cache
        def dp(idx):

            if idx >= len(questions):
                return 0

            return max(dp(idx + questions[idx][1] + 1) + questions[idx][0], dp(idx + 1))


        return dp(0) 