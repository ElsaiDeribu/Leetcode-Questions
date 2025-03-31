class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ans = [[0] * n for _ in range(n)]

        top = left = 0
        bottom = right = n - 1
        direction = "right"
        curr = 1

        while left <= right and bottom >= top:

            if direction == "right":
                for c in range(left, right + 1):
                    ans[top][c] = curr
                    curr += 1

                direction = "down"
                top += 1
            
            elif direction == "down":
                for r in range(top, bottom + 1):
                    ans[r][right] = curr
                    curr += 1

                direction = "left"
                right -= 1

            elif direction == "left":
                for c in range(right, left - 1, -1):
                    ans[bottom][c] = curr
                    curr += 1

                direction = "up"
                bottom -= 1

            elif direction == "up":
                for r in range(bottom, top - 1, -1):
                    ans[r][left] = curr
                    curr += 1

                direction = "right"
                left += 1

        return ans

