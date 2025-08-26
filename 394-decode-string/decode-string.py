class Solution:
    def decodeString(self, s: str) -> str:
        

        st = []

        for i in range(len(s)):

 
            if s[i] == "]":
                temp = []
                n = []

                while st[-1].isalpha():
                    temp.append(st.pop()) 

                st.pop()

                while st and st[-1].isnumeric():
                    n.append(st.pop())

                n = ''.join(n[::-1])

                st += (temp[::-1] * int(n))

            else:
                st.append(s[i])


        return ''.join(st)