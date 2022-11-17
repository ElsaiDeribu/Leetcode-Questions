class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        pIndex = 0
        st = []
        
        for i in range(len(pushed)):
            st.append(pushed[i])
            while st and st[-1] == popped[pIndex]:
                st.pop()
                pIndex += 1
            
        return False if st else True
            
            
        