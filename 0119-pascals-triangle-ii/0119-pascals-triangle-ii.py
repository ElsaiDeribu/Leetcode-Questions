class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        def recur(row):
            if row == 0:
                return [1]
            
            res = recur(row - 1)
            ans = [1]
            
            for i in range(1, len(res)):
                ans.append(res[i] + res[i - 1])
                
            ans.append(1)
            
            return ans
        
        return recur(rowIndex)
            