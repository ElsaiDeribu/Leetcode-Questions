class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        st = []
        st.append(-1)
        ans = 0
        

        for i in range(len(s)):
            
            if s[i] == '(':
                
                st.append(i)
            
            if s[i] == ')':
                
                if len(st) > 1:
                    
                    st.pop()
                    ans = max(ans, i - st[-1])

                    
                else:
                    st[0] = i
                    

        return ans
            
        
        