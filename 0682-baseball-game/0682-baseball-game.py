class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        st =  []
        
        for i in range(len(operations)):
            
            if operations[i] == 'C':
                st.pop()
                
            elif operations[i] == 'D':
                
                st.append(2 * st[-1])
            elif operations[i] == '+':
                op1 = st[-1]
                op2 = st[-2]
                st.append(op1 + op2)
                
            else:
                st.append(int(operations[i]))
            
            
        return sum(st)

                
        