class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        top = left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        direction = "right"
        ans = []

        while left <= right and bottom >= top:

            if direction == "right":
                for c in range(left, right + 1):
                    ans.append(matrix[top][c])
                top += 1
                direction = "down"

            elif direction == "down":
                for r in range(top, bottom + 1):
                    ans.append(matrix[r][right])

                right -= 1
                direction = "left"

            elif direction == "left":
                for c in range(right, left - 1, -1):
                    ans.append(matrix[bottom][c])

                bottom -= 1
                direction = "up"
            
            elif direction == "up":
                for r in range(bottom, top - 1, -1):
                    ans.append(matrix[r][left])
                
                left += 1
                direction = "right"

        return ans



        




        