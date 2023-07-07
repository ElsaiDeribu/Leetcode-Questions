class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = []
        
        @cache
        def recur(n):
                
            if n == 1:
                return [1]   
            
            res = recur(n - 1)
            ans.append(res)
            temp= [1]
            
            for i in range(len(res) - 1):
                temp.append(res[i] + res[i + 1])
                
            temp.append(1)

            
            return temp
        
        
        recur(numRows + 1)
        
        return ans
            
            
            
            
        