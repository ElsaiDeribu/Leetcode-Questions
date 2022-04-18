class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"*","/","+","-"}
        st = []
        for i in range(len(tokens)):
            if tokens[i] in operators :
                result = 0
                operand1 = st[-1]
                st.pop(-1)
                operand2 = st[-1]
                st.pop(-1)
                if tokens[i] == "*":
                    result = operand2 * operand1
                elif tokens[i] == "/":
                    result = operand2 / operand1
                    if result > 0:
                        result = floor(result)
                    else:
                        result = ceil(result)
                elif tokens[i] == "-":
                    result = operand2 - operand1
                elif tokens[i] == "+" :
                    result = operand2 + operand1    
                st.append(result)
            else: 
                st.append(int(tokens[i]))
                
        return  st[-1]