class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        st = []
        visited = defaultdict(int)
        freq = Counter(s)
        
        
        for i in s:
            if visited[i] == 1:
                freq[i] -= 1
                continue
            
            while st and st[-1] > i and freq[st[-1]] >= 1 :
                visited[st[-1]] = 0
                st.pop()
                
                
            # if visited[i] == 0:
            st.append(i)
            visited[i] = 1
            freq[i] -= 1
                
            # else:
            #     freq[i] -= 1

                
        return ''.join(st)