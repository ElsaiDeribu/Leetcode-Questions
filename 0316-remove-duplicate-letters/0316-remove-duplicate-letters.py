class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        
        st = []
        visited = set()
        count = Counter(s)
        
        for i in range(len(s)):
            
            if s[i] not in visited:
                
                while st and st[-1] >= s[i] and count[st[-1]] > 0:
                    visited.remove(st.pop())

                st.append(s[i])
                count[s[i]] -= 1
                visited.add(s[i])
                
            else:
                count[s[i]] -= 1
                
                
        return ''.join(st)


            