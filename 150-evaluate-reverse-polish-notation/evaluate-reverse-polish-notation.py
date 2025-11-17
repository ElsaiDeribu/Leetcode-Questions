class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                op1 = st.pop()
                op2 = st.pop()
                if token == "/":
                    st.append(str(int(op2) / int(op1)).split('.')[0])

                else:   
                    st.append(str(eval(op2 + token + op1)))

            else:
                st.append(token)


        return int(st[-1])