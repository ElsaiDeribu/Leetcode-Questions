class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        st = []
        
        for i in range(len(num)):
            while st and int(st[-1]) > int(num[i]) and k > 0:
                st.pop()
                k -= 1
            st.append(num[i])
            
        i = 0
        while i < len(st) and st[i] == '0':
            i += 1
        st = st[i:]
        
        
        if len(st) == 1 and k:
            return "0"
        
        if k:
            st = st[:len(st) - k]
        
        return ''.join(st) if len(st) > 0  else "0"
        
        