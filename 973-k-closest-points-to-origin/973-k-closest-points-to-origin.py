class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        answer = []
        
        for i in range(len(points)):
            points[i] = ( math.sqrt(pow(points[i][0],2) + pow(points[i][1],2)), points[i])
            
        points.sort()
        
        for i in range(k):
            answer.append(points[i][1])
            
        return answer
        