class Solution:
    def isValid(self, s: str) -> bool:

        map = {"(":")", "{":"}", "[":"]"}
        st = []


        for idx, val in enumerate(s):

            if val in map:
                st.append(val)

            else:
                if st and  map[st[-1]] == val:
                    st.pop()

                else:
                    return False

        
        return True if not st else False
                
                
        