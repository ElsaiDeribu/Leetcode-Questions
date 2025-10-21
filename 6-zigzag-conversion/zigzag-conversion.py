class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        n = len(s)
        p = 0
        c = 0
        mat = [[] for _ in range(numRows) ]


        while p < n:
            for r in range(0, numRows):
                if p < n:
                    mat[r].append(s[p])
                    p += 1
                else:
                    break
            c += 1

            for r in range(numRows - 2, 0, -1):
                if p < n:
                    mat[r].append(s[p])
                    p += 1
                    c += 1
                else:
                    break

     
        return ''.join(''.join(row) for row in mat)

            




