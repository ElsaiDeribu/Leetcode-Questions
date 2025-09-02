class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for row in matrix:

            idx = bisect_left(row ,target)

            if 0 <= idx < len(row) and row[idx] == target:
                return True


        return False