class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        st = []
        count = 0
        ans = ''
      
        
        for i in range(len(s)):
            
            if st and st[-1][0] == s[i]:
                st[-1][1] += 1
                if st[-1][1] == k:
                    st.pop()
                continue
                
            st.append([s[i], 1])
            
            
                    
        for i in range(len(st)):
            while st[i][1]:
                ans += st[i][0]
                st[i][1] -= 1
                
        return ans
            
            