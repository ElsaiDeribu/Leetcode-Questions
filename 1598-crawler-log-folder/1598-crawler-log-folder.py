class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        st = []
        
        for i in range(len(logs)):
            if logs[i] != "../" and logs[i] != "./":
                st.append(logs[i])
                
            elif st and logs[i] == "../":
                st.pop()
        
        return len(st)
            
        