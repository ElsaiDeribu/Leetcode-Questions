class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        st = []
        
        for i in range(len(s)):
            
            if s[i] != ')':
                
                st.append(s[i])
                
            else:
                temp = []
                
                while st[-1] != '(':
                    temp.append(st[-1])
                    st.pop()
                    
                st.pop()
                    
                for i in temp:
                    st.append(i)
          
        
        return ''.join(st)