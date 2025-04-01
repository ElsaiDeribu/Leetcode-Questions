class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        step = 1
        drctn = "right"
        ans = [[rStart, cStart]]
        
        def check_and_add(r, c):
            if 0 <= r < rows and 0 <= c < cols:
                ans.append([r,c])

        while len(ans) < cols * rows:

            if drctn == "right":
                for s in range(step):
                    cStart += 1
                    check_and_add(rStart, cStart)

                drctn = "down"

            elif drctn == "down":
                for s in range(step):
                    rStart += 1
                    check_and_add(rStart, cStart)

                step += 1
                drctn = "left"

            elif drctn == "left":
                for s in range(step):
                    cStart -= 1
                    check_and_add(rStart, cStart)

                drctn ="up"

            elif drctn == "up" :
                for s in range(step):
                    rStart -= 1
                    check_and_add(rStart, cStart)

                step += 1
                drctn ="right"

        return ans




        