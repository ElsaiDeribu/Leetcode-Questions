class Solution:
    def compress(self, chars: List[str]) -> int:
        
        
        builderIdx, left, right = 0, 0, 0
        
        
        while right < len(chars):
            chrCount = 0
            
            while right < len(chars) and chars[left] == chars[right]:
                chrCount += 1
                right += 1
                
            chars[builderIdx] = chars[left]
            builderIdx += 1

            if chrCount > 1:
                
                temp = str(chrCount)
                for i in range(len(temp)):
                    chars[builderIdx] = temp[i]
                    builderIdx += 1
                    
            left = right   
            
        chars = chars[:builderIdx]
        
        return len(chars)
            
        
        
        
        
                
                
                
            
            
            
        