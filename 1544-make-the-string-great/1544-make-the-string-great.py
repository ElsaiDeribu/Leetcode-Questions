class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        
        for i in range (len(s)):
            
            if st and st[-1].lower() == s[i].lower():
                if (st[-1].isupper() and s[i].islower()) or (st[-1].islower() and s[i].isupper()):
                    st.pop()
                    continue
            st.append(s[i])
            
            
        return ''.join(st)