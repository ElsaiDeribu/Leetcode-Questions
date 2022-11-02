class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        st = []
        
        operations = {"*","/","-","+"}
        
        for i in range(len(tokens)):
            
            if tokens[i] in operations:
                operand2 = st.pop()
                operand1 = st.pop()
                
                if tokens[i] == "+":
                    result = operand1 + operand2
                elif tokens[i] == "-":
                    result = operand1 - operand2
                elif tokens[i] == "/":
                    result = operand1 / operand2
                    
                    if result < 0 :
                        result = math.ceil(result)
                    else:
                        result = math.floor(result)
                        
                elif tokens[i] == "*":
                    result = operand1 * operand2
                
                st.append(result)
                
            else:
                st.append(int(tokens[i]))
        
        
        return st[0]