class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        n = str(n)
        digits = []
        
        def isUnder32bit(num):
            if num in range(-2 ** 31, (2**31) ):
                return num
            return -1
        
        
        for i in range(len(n)):
            
            digits.append(int(n[i]))
        
        
        for i in range(len(n) - 1, -1, -1):
            
            if i - 1 > -1 and n[i - 1] < n[i]:
                break
        
        
        if i == 0:
            digits.sort()
            return -1
            
        indexToReplace = i - 1
        leastReplacementIndex = i
        
        for k in range(i + 1, len(digits)):
            if digits[k] > digits[indexToReplace] and digits[k] < digits[leastReplacementIndex]:
                leastReplacementIndex = k
                
        digits[indexToReplace], digits[leastReplacementIndex] = digits[leastReplacementIndex], digits[indexToReplace]
        
        for j in range(indexToReplace + 1, len(digits)):
            for t in range(j+1, len(digits)):
                if digits[t] < digits[j]:
                    
                    digits[t], digits[j] = digits[j], digits[t]
                
                
        ans =  int(''.join(map(str, digits)))
        
        
        return isUnder32bit(ans)
        
        
        
      
        
        