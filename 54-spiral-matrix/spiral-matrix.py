class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []

        l, t = 0, 0
        r, b = len(matrix[0]) - 1, len(matrix) - 1

        d = "r"

        while l <= r and t <= b:

            
            if d == "r":

                for i in range(l, r + 1):
                    ans.append(matrix[t][i])

                t += 1
                d = "d"

            elif d == "d":
                for i in range(t, b + 1):
                    ans.append(matrix[i][r])

                r -= 1
                d = "l"

            elif d == "l":
                for i in range(r, l - 1, -1):
                    ans.append(matrix[b][i])

                b -= 1
                d = "u"


            else:
                for i in range(b, t - 1, -1):
                    ans.append(matrix[i][l])

                l += 1
                d = "r"


        return ans
                


        