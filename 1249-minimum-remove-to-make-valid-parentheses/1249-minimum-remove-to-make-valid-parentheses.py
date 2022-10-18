class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        count = Counter(s)
        st = []
        ans = []
        
        
        for i in range(len(s)):
            
            if s[i] == '(':
                if count[')']:
                    ans.append(s[i])
                    st.append(s[i])
                    count[')'] -= 1
            if s[i] == ')':
                
                if st:
                    st.pop()
                    ans.append(s[i])
                else:
                    count[')'] -= 1

                    
                    
            if s[i] != '(' and  s[i] != ')':
                ans.append(s[i])
                
                
        return ''.join(ans)