class Solution:
    def decodeString(self, s: str) -> str:
        
        
        ans = []
        
        def recur(start):
            
            i = start
            temp = []
            num = 0
            
            while i < len(s):
                
                if s[i].isnumeric():
                    num = num * 10 + int(s[i])
                  
                elif s[i] == "[":
                    
                    result, currIndex = recur(i + 1)
                    i = currIndex 
                    
                    temp.append(result * num)
                    num = 0
                    
                elif s[i] == "]":
                    
                    break
                    
                else:
                    temp.append(s[i])
                  
                i += 1
            
            
            return ("".join(temp), i)

                
        return recur(0)[0]
        
        
