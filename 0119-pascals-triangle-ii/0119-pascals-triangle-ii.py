class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        def helper(currRow):
            
            if currRow == 0:
                return [1]
            if currRow == 1:
                return [1, 1]
            
            prior = helper(currRow - 1)
            
            result = [1] * (len(prior) + 1)
            
            left, right = 0, 1
            
            for i in range(1, len(result) - 1):
                result[i] = prior[left] +  prior[right]
                left += 1
                right += 1
                
            return result 
        
        return helper(rowIndex)
            
            
            
            
        