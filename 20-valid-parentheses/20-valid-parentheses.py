class Solution:
    def isValid(self, s: str) -> bool:
        
        
        st = []
        temp = []
        
        dic = {'(':')', '[':']', '{':'}'}
        
        for i in range(len(s)):
            
            if s[i] in dic.values():
                
                while st and dic[st[-1]] != s[i]:
                    if st[-1] in dic.keys() :
                        return False
                        
                    temp.append(st.pop())
                
                if st and dic[st[-1]] == s[i]:
                    st.pop()
                else:
                    return False
                    
                for i in temp:
                    st.append(i)
                    
                temp = []
            else:
                st.append(s[i]) 
   
                
        if st  :
            return False
        else:
            return True
                
                
    
        