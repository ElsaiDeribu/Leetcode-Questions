class Solution:
    def isValid(self, s: str) -> bool:

        st = []
        pairs = {"[":"]", "{":"}", "(":")"}


        for char in s:

            if char not in pairs:
                if st and pairs[st[-1]] == char:
                    st.pop()
                else:
                    return False
            else:
                st.append(char)


        return False if st else True