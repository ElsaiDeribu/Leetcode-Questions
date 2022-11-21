class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path2 = path.split('/')
        st = []
        
        for i in range(len(path2)):
            if path2[i] == "..":
                if st:
                    st.pop()
                else: continue
                
            elif path2[i] == "." or path2[i] == "":
                continue
                
            else:
                st.append(path2[i])
        
        # print(st)
        return '/' + '/'.join(st)
            
            