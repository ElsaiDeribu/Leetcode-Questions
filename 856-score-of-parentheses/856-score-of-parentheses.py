class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        st = []
        score = 0
        
        for i in s:
            
            if i == '(':
                st.append(score)
                score = 0
                
            else:
                
                score = st.pop() + max(score*2, 1)
                
        return score
        
        