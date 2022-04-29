class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while s[j].isdigit():
                    j += 1
                st.append(s[i:j])
                i = j
            elif s[i] == "]":
                temp = ""
                while not st[-1].isdigit():
                    if st[-1] == "[":
                        st.pop()
                    if not st[-1].isdigit():
                        temp += st.pop()
                digit = int (st.pop())
                temp = (digit * temp)[::-1]
                for j in temp:
                    st.append(j)
                if i < len(s)-1:
                    i += 1
                else: break
            elif not s[i].isdigit():
                st.append(s[i])
                i += 1

        ans = ''.join(st)
        return ans
