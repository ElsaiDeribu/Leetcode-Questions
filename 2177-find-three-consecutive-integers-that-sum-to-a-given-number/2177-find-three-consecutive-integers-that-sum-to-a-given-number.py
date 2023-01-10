class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        
        if num % 3 != 0:
            return []
        
        midleNum = num // 3
        
        return [midleNum - 1, midleNum, midleNum + 1]
    
    
        
        
        
        
        
            
            
            
        
        
        