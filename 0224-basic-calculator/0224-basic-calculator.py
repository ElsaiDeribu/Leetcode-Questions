class Solution:
    def calculate(self, s: str) -> int:
            
            sign = 1
            total = 0
            st = []
            i = 0
            
            while i < len(s):
                
                if s[i] == "(":
                    st.append(total)
                    st.append(sign)
                    # st.append("(")
                    sign = 1
                    total = 0
                    
                elif s[i] in "+-":
                    if s[i] == "+":
                        sign = 1
                    else:
                        sign = -1
                
                elif s[i] == ")":
                    stackedSign = st.pop()
                    stackedNumber = st.pop()
                    total = stackedNumber + (stackedSign * total)
                    
                elif s[i] != " ":
                    start = i
                    while i < len(s) and s[i].isdigit():
                        i += 1
                    
                    number = s[start: i]
                    total = total + (sign * int(number))
                    continue
                    
                i += 1
                        
            return total
            