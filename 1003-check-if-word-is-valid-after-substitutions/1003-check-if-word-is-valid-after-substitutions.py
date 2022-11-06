class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []
        
        for i in range(len(s)):
            
            if s[i] == 'c' and len(st) >= 2:
                b = st.pop()
                a = st.pop()
                
                if b != "b" or a != "a":
                    st.append(a)
                    st.append(b)
                    st.append(s[i])
                
            else:
                st.append(s[i])
          
        return False if st else True
