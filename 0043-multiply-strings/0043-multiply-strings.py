class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        revnum1 = num1[::-1]
        revnum2 = num2[::-1]
        zero = ''
        productRows = []
        
        for i in range(len(revnum1)):
            sProd = ""
            rem = ""
            for j in range(len(revnum2)):
                
                if rem:
                    prod = str(int(revnum1[i]) * int(revnum2[j]) + int(rem))
                    rem = ""
                else:
                    prod = str(int(revnum1[i]) * int(revnum2[j]))
                    
                if j < len(revnum2) - 1 and len(prod) >= 2 :
                    rem = prod[0]
                    prod = prod[1]
                    
                sProd = prod + sProd
            
            if i:
                zero += '0'
                productRows.append(sProd + zero)
            
            else:
                productRows.append(sProd)
            
        return str(sum(map(int,productRows) ))