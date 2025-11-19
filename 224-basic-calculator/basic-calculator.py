class Solution:
    def calculate(self, s: str) -> int:

        num = 0
        st = []
        total = 0
        sign = 1

        for val in s:
            if val.isdigit():
                num = ((num * 10) + int(val))

            elif val in "-+":
                total += (sign * num)
                num = 0
                sign = -1 if val == "-" else 1

            elif val == "(":
                st.append(total)
                st.append(sign)
                total = 0
                sign = 1


            elif val == ")":
                total += (sign * num)
                num = 0
                total *= st.pop()
                total += st.pop()


        return total + sign * num

                







