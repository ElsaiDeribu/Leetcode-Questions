class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        
        for i in range(len(s)):
            
            if st and st[-1] == s[i]:
                st.pop()
                continue
            st.append(s[i])
            
        return ''.join(st)
        