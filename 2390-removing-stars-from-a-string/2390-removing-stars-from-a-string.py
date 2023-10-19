class Solution:
    def removeStars(self, s: str) -> str:
        
        st = []
        
        for i in range(len(s)):
            
            if s[i] == "*":
                if st:
                    st.pop()
            else:
                st.append(s[i])
        
        return ''.join(st)
        