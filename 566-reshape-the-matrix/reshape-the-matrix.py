class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        row = len(mat)
        col = len(mat[0])

        if not r * c == row * col:
            return mat

        flat = []

        for i in range(row):
            for j in range(col):
                flat.append(mat[i][j])

        ans = []
        curr = 0

        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(flat[curr])
                curr += 1

            ans.append(temp)

        return ans

                

        