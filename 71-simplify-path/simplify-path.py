class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.split("/")

        st = []


        for direc in path:
            if direc and direc != ".":
                if direc == "..":
                    if st: st.pop() 

                else:
                    st.append(direc)

        return '/' + '/'.join(st)

        