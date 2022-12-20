class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        smallest = [-1 , float("inf")]
        
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                manhattanDistance = abs(x - points[i][0]) + abs(y - points[i][1])
                if manhattanDistance < smallest[1]:
                    smallest[1] = manhattanDistance
                    smallest[0] = i
                
        return smallest[0]