class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        sStack= []
        tStack = []
        
        for i in range(len(s)):
            if sStack and s[i] == "#":
                sStack.pop()
            elif s[i] != "#":
                sStack.append(s[i])
                
                
        for i in range(len(t)):
            if tStack and t[i] == "#":
                tStack.pop()
            elif t[i] != "#":
                tStack.append(t[i])
                
        return tStack == sStack