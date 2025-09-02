class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:


        if r * c != len(mat) * len(mat[0]):
            return mat

        ans = [[0] * c for _ in range(r)]


        for i in range(len(mat)):
            for j in range(len(mat[0])):

                ord = i * len(mat[0]) + j

                row = ord // c
                col = ord % c

                ans[row][col] = mat[i][j]


        return ans
        