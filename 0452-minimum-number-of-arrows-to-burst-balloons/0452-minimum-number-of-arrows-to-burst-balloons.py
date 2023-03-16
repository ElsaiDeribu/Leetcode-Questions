class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        arrows = 1
        curr = float('inf')
        
        for i in range(len(points)):
      
            if  points[i][0] > curr:
                arrows += 1
                curr = points[i][1]
                
            else:
                curr = min(curr, points[i][1])
                
                
        return arrows
            
                
        