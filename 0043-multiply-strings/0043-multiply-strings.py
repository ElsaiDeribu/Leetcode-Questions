class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        reversed_num1 = num1[::-1]
        reversed_num2 = num2[::-1]
        zero = ''
        product_rows = []
        
        for i in range(len(reversed_num1)):
            sProd = ""
            remainder = ""
            for j in range(len(reversed_num2)):
                
                if remainder:
                    prod = str(int(reversed_num1[i]) * int(reversed_num2[j]) + int(remainder))
                    remainder = ""
                else:
                    prod = str(int(reversed_num1[i]) * int(reversed_num2[j]))
                    
                if j < len(reversed_num2) - 1 and len(prod) >= 2 :
                    remainder = prod[0]
                    prod = prod[1]
                    
                sProd = prod + sProd
            
            if i:
                zero += '0'
                product_rows.append(sProd + zero)
            
            else:
                product_rows.append(sProd)
            
        return str(sum(map(int,product_rows) ))