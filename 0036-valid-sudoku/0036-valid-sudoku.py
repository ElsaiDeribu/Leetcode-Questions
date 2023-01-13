class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        
        sectionMids = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        
        
        def checkSection(index):

            valuesInSection = set()
            currVal = board[index[0]][index[1]]
            valuesInSection.add(currVal) if currVal != "." else None
            
            if currVal in rows[index[0]] or currVal in cols[index[1]]:
                return False
            
            rows[index[0]].add(currVal) if currVal != "." else None
            cols[index[1]].add(currVal) if currVal != "." else None
            
            for direction in directions:
                row = index[0] + direction[0]
                col = index[1] + direction[1]
                
                currVal = board[row][col] 
                
                if currVal in valuesInSection:
                    return False
                
                if currVal in rows[row] or currVal in cols[col]:
                    return False
                
                rows[row].add(currVal) if currVal != "." else None
                cols[col].add(currVal) if currVal != "." else None
                valuesInSection.add(board[row][col]) if currVal != "." else None
            

#             if not valuesInSection:
#                 return False
            
            return True
            
            
        for mid in sectionMids:
            res = checkSection(mid)
            
            if res == False:
                return False

            
        return True
            
