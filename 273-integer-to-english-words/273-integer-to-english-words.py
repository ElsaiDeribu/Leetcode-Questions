class Solution:
    def numberToWords(self, num: int) -> str:
        
        dic = {0:'', 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven",                 12:"Twelve", 13:"Thirteen", 14: "Fourteen", 15:"Fifteen",16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
        
        dic1 = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety" }
        dic2 = {3:"Hundred", 4:"Thousand", 7:"Million", 10:"Billion"}
        
        
        lengthOfDigit = len(str(num))
        
        if num == 0:
            return "Zero"
        
        def getTwoDigits(digits):
            length = len(str(digits))
            if length == 1 or (length == 2 and int(str(digits)[0]) == 1):
                return dic[digits]

            if length == 2 and int(str(digits)[0]) > 1:
                
                return (dic1[int(str(digits)[0])] + " " + dic[int(str(digits)[1])]).strip()
            
        def getThreeDigits(digits):
             length = len(str(digits))
             if length <= 2:
                return getTwoDigits(digits).strip()
     
             return (dic[int(str(digits)[0])] + " " + dic2[3] +  " " + getTwoDigits(int(str(digits)[1:]))).strip() 
            
        def getFourToSixDigits(digits):
            length = len(str(digits))
                
            if length <= 2:
                 return getTwoDigits(digits).strip()
        
            if length== 3:
                 return getThreeDigits(digits).strip()
            
            n = 0
            if length == 5:
                n = 2
            elif length == 6:
                n = 3
                
            if n == 0:
                return (dic[int(str(digits)[0])] + " " + dic2[4] +" " + getThreeDigits(int(str(digits)[1:]))).strip()
            elif n == 2:
                return (getTwoDigits(int(str(digits)[0:n])) + " " + dic2[4] +" " + getThreeDigits(int(str(digits)[2:]))).strip()
            elif n == 3:
                 return (getThreeDigits(int(str(digits)[0:n])) + " " + dic2[4] +" " + getThreeDigits(int(str(digits)[3:]))).strip()
            
            
        def getSevenToNineDigits(digits):
            length = len(str(digits))
            if length <= 2:
                return getTwoDigits(digits).strip()
        
            if length == 3:
                return getThreeDigits(digits).strip()
        
            if 4 <= length <= 6: 
                return getFourToSixDigits(digits).strip()
            
            n = 0 
            if length == 8:
                n = 2
            elif length == 9:
                n = 3
                
            if n == 0:
                return (dic[int(str(digits)[0])] + " " + dic2[7] +" " + getFourToSixDigits(int(str(digits)[1:]))).strip()
            elif n == 2:
                return (getTwoDigits(int(str(digits)[0:n])) + " " + dic2[7] +" " +  getFourToSixDigits(int(str(digits)[2:]))).strip()
            elif n == 3:
                 return (getThreeDigits(int(str(digits)[0:n])) + " " + dic2[7] +" " + getFourToSixDigits(int(str(digits)[3:]))).strip()
            

        if lengthOfDigit <= 2:
            return getTwoDigits(num).strip()
        
        if lengthOfDigit == 3:
            return getThreeDigits(num).strip()
        
        if 4 <= lengthOfDigit <= 6: 
            return getFourToSixDigits(num).strip()
        
        if 7 <= lengthOfDigit <= 9:
            return  getSevenToNineDigits(num).strip()
        if 9 < lengthOfDigit:
    
            return (dic[int(str(num)[0])] +" " +dic2[10]+" "+  getSevenToNineDigits(int(str(num)[1:]))).strip()
        


        
    
            
        
        