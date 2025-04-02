class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        cache = [0] * n

        for i in range(n - 1, -1, -1):

            points, brain = questions[i]
            
            next_i = i + 1 + brain

            take = points + (cache[next_i] if next_i < n else 0  )
            not_take = cache[i + 1] if i + 1 < n else 0

            cache[i] = max(take, not_take)

        return cache[0]