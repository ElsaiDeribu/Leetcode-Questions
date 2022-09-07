class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        start = 0
        end = len(grid[0]) - 1
        count = 0
        
        for i in range(len(grid)):
            
            if grid[i][0] < 0:
                count += len(grid[0])
                continue
                
            if grid[i][-1] >= 0:
                continue
                
            while start != end - 1:
                
                # mid = math.ceil(start + end / 2)
                mid = (start + end )//2 

                
                if grid[i][mid] < 0:
                    end = mid
                else:
                    start = mid
                    
                    
            count += (len(grid[0]) - end)
            
            start = 0
            end = len(grid[0]) - 1
            
            
        return (count)
            
            
            
        
        

    
    
