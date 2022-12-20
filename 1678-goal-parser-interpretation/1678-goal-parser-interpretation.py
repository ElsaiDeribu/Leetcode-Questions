class Solution:
    def interpret(self, command: str) -> str:
        
        st = []
        ans = ""
        
        for i in range(len(command)):
            
            st.append(command[i])
            temp = ''.join(st)

            if temp == 'G':
                ans += 'G'
                st = []
                
            elif temp =="()":
                ans += 'o'
                st = []
                
            elif temp == "(al)":
                ans += 'al'
                st = []
            
            
        return ans