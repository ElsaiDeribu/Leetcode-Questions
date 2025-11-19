class Solution:
    def calculate(self, s: str) -> int:

        def cal(val):
            res = 0
            operation = 1
            for v in val:
                if v not in "+-": res += (operation * int(v))
                elif v == "+": operation = 1
                elif v == "-": operation = -1

            return str(res)

        num = ""
        st = []

        for val in s:
            if val.isdigit():
                num += val


            elif val in "+-(":
                if num: st.append(num);num = ""
                st.append(val)


            elif val == ")":
                temp = deque([])

                if num: st.append(num);num = ""

                while st[-1] != "(":
                    temp.appendleft(st.pop())

                st.pop()
                st.append(cal(temp))

        if num:
            st.append(num)

        return int(cal(st))





            