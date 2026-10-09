class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operation = ["+","-", "*","/"]
        st = []


        for char in tokens:
            if char in operation:
                op2, op1 = st.pop(), st.pop()

                if char == "+":
                    st.append(op1 + op2)
                elif char == "-":
                    st.append(op1 - op2)
                elif char == "*":
                    st.append(op1 * op2)
                else:
                    res = op1 / op2
                    st.append(int(res))

            else:
                st.append(int(char))


        return st[-1]