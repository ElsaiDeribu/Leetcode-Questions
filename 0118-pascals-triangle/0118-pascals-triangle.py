class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        def build(row):
            
            if row == 1:
                return [[1]]
            
            res = build(row - 1)
            ans = []
            temp = res[-1]
            ans.append(1)
            
            for i in range(len(temp) - 1): 
                ans.append(temp[i] + temp[i + 1])
                
            ans.append(1)
            res.append(ans)
            
            return res
        
        
        return build(numRows)
                
            