class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        
     
        temp = [0] * len(s)
        
        curr = 1
        for i in range(len(s)):
            
            if s[i].isdigit():
                curr -= 1
                curr *= int(s[i])
                
            temp[i] = curr
            curr += 1
            
        print(temp)
        for i in range(len(s) - 1 , -1 , -1):
            if s[i].isdigit(): 
                 k = k % (temp[i] // int(s[i]))
                   
            elif temp[i] == k or k == 0:
                    return s[i]
            
            
        