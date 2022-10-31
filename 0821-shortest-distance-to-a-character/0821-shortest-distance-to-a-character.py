class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        reqIndex = None
        ans = [0] * len(s)
        
        for i in range(len(s)):
            if s[i] == c:
                reqIndex = i
            elif reqIndex != None:
                ans[i] = i - reqIndex
            else:
                ans[i] = 10**5
                
        reqIndex = None
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                reqIndex = i
            elif reqIndex:
                ans[i] = min(ans[i], reqIndex - i)
        
        return ans