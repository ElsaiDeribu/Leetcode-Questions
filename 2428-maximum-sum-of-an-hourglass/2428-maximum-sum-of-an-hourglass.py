class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        maximum = 0
        left = 0
        right = 2
        top = 0
        bottom = 2
        
        
        def findSum(l, r, t, b):
            total = sum(grid[t][l: r + 1]) + sum(grid[b][l: r + 1]) + grid[(t + b) // 2][(l + r) // 2]
            return total
        
        
        while right < len(grid[0]):
            top = 0
            bottom = 2
            while bottom < len(grid):
                maximum = max(maximum, findSum(left, right, top, bottom))
                top += 1
                bottom += 1
            right += 1
            left += 1
            
        return maximum
            