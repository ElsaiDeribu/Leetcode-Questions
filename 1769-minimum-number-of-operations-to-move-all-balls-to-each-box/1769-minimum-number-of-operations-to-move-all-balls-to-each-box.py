class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        movesList = [0] * len(boxes)
        
        
        prefixMoves = [0] * len(boxes)
        postfixMoves = [0] * len(boxes)
        
        movesRequired = 0
        movesTillNow = 0
        for i in range(len(boxes)):
            prefixMoves[i] = movesTillNow
            movesRequired += int(boxes[i])
            movesTillNow += movesRequired
        
        movesRequired = 0
        movesTillNow = 0
        
        for i in range(len(boxes) -1 ,-1, -1):
            postfixMoves[i] = movesTillNow
            movesRequired += int(boxes[i])
            movesTillNow += movesRequired
            
        for i in range(len(movesList)):
            movesList[i] = prefixMoves[i] + postfixMoves[i]
            
            
        return movesList