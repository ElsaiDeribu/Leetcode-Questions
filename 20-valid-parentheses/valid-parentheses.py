class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {"{":"}", "(":")", "[":"]"}
        st = []

        for bra in s:
            if bra not in pairs:
                if st and pairs[st[-1]] == bra:
                    st.pop()
                else: 
                    return False
            else:
                st.append(bra)

        if st: return False
        
        return True

                


