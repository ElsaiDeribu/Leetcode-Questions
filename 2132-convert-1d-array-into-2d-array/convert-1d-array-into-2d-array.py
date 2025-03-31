class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
 
        if not len(original) == m * n:
            return []

        ans = []

        for row in range(m):
            ans.append(original[row * n : row * n + n])

        return ans
        