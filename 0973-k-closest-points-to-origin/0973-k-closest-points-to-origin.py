class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        for i in range(len(points)):
            
            distance = sqrt((points[i][0]**2) + (points[i][1])**2 )
            
            points[i] = (distance, points[i])
            
        points.sort()
        ans = []
        
        for i in range(k):
            ans.append(points[i][1])
            
        return ans
            
        