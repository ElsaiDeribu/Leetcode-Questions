class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        st = []
        NumberOfDigitsToRemove = k
        
        for i in range(len(num)):
            while st and int(num[i]) < st[-1] and  NumberOfDigitsToRemove > 0:
                    st.pop()
                    NumberOfDigitsToRemove -= 1
                

            st.append(int(num[i]))

        while NumberOfDigitsToRemove:
            st.pop()
            NumberOfDigitsToRemove-=1
          
        while len(st) > 1 and st[0] == 0:
            st.pop(0)
        if not st:
            st.append(0)
        
        return ''.join(map(str,st))
        