class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                op2 = st.pop()
                op1 = st.pop()

                if token == "+":
                    st.append(op1 + op2)
                elif token == "-":
                    st.append(op1 - op2)
                elif token == "*":
                    st.append(op1 * op2)
                elif token == "/":
                    st.append(int(op1 / op2))
            else:
                st.append(int(token))


        return st[0]

        