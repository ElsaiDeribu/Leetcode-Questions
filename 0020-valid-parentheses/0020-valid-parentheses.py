class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []
        
        dic = {'(':')', '{':'}', '[':']'}
        
        
        for i in range(len(s)):
            
            if s[i] in dic.keys():
                st.append(s[i])
            
            else:
                
                if st and dic[st[-1]] == s[i]:
                    st.pop()
                    
                    
                else:
                    return False
                
                
                
        return False if st else True
            
                
            